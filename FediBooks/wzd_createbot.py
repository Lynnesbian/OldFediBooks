#!/usr/bin/env python3
# Copyright (C)2019 Lynnesbian (https://fedi.lynnesbian.space/@LynnearSoftware)

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from PySide2.QtWidgets import QApplication, QMainWindow, QDialog
from PySide2.QtCore import QFile, Signal, Slot, QObject, QThread

import requests
from Misskey import Misskey
import diaspy

import sys, re, json, urllib
import xml.etree.ElementTree as ElementTree
from http import server
from multiprocessing import Pipe

from .functions import *
from .fixtodon import Fixtodon
from .uic.ui_wzd_createbot import Ui_wzdCreateBot
from .uic.ui_dlg_wzd_error import Ui_dlgWzdError

class dlgWzdError(QDialog):
	def __init__(self):
		super(dlgWzdError, self).__init__()
		self.ui = Ui_dlgWzdError()
		self.ui.setupUi(self)

	def rejected(self):
		self.accepted # :blobderpy:

	def accepted(self):
		self.done(1)

	def present(self, text):
		self.ui.label.setText("There were some problems with the data you entered. Please rectify the following issues and try again.\n\n{}\n\nIf you believe this to be a problem with FediBooks itself, please open a GitHub issue, or notify Lynne (@LynnearSoftware.fedi.lynnesbian.space)".format(text))
		self.exec()

class srvOauthResponseServer(server.BaseHTTPRequestHandler):
	def __init__(self, thr, *args):
		self.thr = thr
		server.BaseHTTPRequestHandler.__init__(self, *args)

	def do_GET(self):
		self.send_response(200)
		self.end_headers()
		p = urllib.parse.parse_qs(self.path[2:])
		if "code" in p or "token" in p:
			#this is the response we're looking for
			self.thr.params = p
			

class thrOauthResponseServer(QThread):
	send_code = Signal(str)
	# send_error = Signal(str)
	send_true = Signal(bool)
	send_port = Signal(int)
	
	def __init__(self, wzd, port = 0):
		self.wzd = wzd
		self.params = None
		self.port = port
		super(thrOauthResponseServer, self).__init__()

	def __del__(self):
		self.exiting = True
		self.wait()

	def run(self):
		# i've encountered a very, very strange bug
		# the whole program will freeze while waiting to receive the port number.
		# send_port.emit() will do nothing, and the program won't respond until this thread ends.
		# so it's necessary to return the port, and then start the server up again later with the same port.
		# why? i don't know
		# i tried to debug this issue using python's trace module, but when using python3 -m trace, the error disappears

		server_address = ('127.0.0.1', self.port)
		def handler(*args):
			srvOauthResponseServer(None, *args)
		httpd = server.ThreadingHTTPServer(server_address, handler)
		if self.port == 0:
			self.send_port.emit(httpd.server_port)
			return

		while self.params == None or ("code" not in self.params and "token" not in self.params):
			httpd.handle_request()
		print(self.params)
		self.send_code.emit(self.params)

class thrOauthCodeRequester(QThread):
	send_url = Signal(str)
	send_error = Signal(str)

	def __init__(self, wzd):
		self.wzd = wzd
		super(thrOauthCodeRequester, self).__init__()

	def __del__(self):
		self.exiting = True
		self.wait()

	def run(self):
		if self.wzd.instance['type'] in ['mastodon', 'pleroma']:
			# mastodon/pleroma
			try:
				client = Fixtodon(client_id = self.wzd.app['credentials']['app_id'],
					client_secret = self.wzd.app['credentials']['app_secret'],
					api_base_url=self.wzd.instance['url']
				)
				self.send_url.emit(client.auth_request_url(scopes=self.wzd.app['permissions']))
			except:
				self.send_error.emit("An error ocurred while requesting authorisation.")
			return

		elif self.wzd.instance['type'] == 'misskey':
			# misskey
			try:
				client = Misskey(instanceAddress = self.wzd.instance['url'],
					appSecret = self.wzd.app['credentials']['app_secret'],
					appId = self.wzd.app['credentials']['app_id']
				)
				self.wzd.app['credentials']['api_token'] = Misskey.auth_session_generate(
					instanceAddress="https://misskey.xyz", 
					appSecret = self.wzd.app['credentials']['app_secret']
				)
			except:
				self.send_error.emit("An error ocurred while requesting authorisation.")
			return
		

class thrWzdPageValidator(QThread):
	send_true = Signal(bool)
	send_text = Signal(str)
	update_pbr = Signal(int, str)
	set_pbr_visibility = Signal(bool)

	def __init__(self, wzd):
		self.wzd = wzd
		super(thrWzdPageValidator, self).__init__()

	def __del__(self):
		self.exiting = True
		self.wait()

	def run(self):
		pn = self.wzd.page_name()

		if pn == "choose_an_instance":
			steps = ["Connecting", "Verifying", "Checking instance type"]
			self.wzd.app = None # if we had an app before, it's invalid now, because we're changing instances

			# CONNECTING

			self.set_pbr_visibility.emit(True)
			self.update_pbr.emit(1, steps[0])
			self.wzd.instance = {
				"name":None,
				"type":None,
				"version":None,
				"webfinger_uri":None,
			}
			try:
				self.wzd.instance['name'] = re.search(r"(?:https?:\/\/)?((?:\w+\.)+\w+)\/?", self.wzd.ui.txt_instance.text()).group(1)
			except:
				self.send_text.emit("The instance URL you provided is not a valid URL.")
				return
			# valid URL, check if it's actually an instance
			# afaik the best way to do this is to check for a host-meta file containing a link rel="lrdd"
			# mastodon refuses to federate with non-HTTPS websites, and you can set up HTTPS for free in ten minutes, so there's really no reason not to enforce it
			try:
				r = requests.get("https://{}/.well-known/host-meta".format(self.wzd.instance['name']), timeout=30)
			except requests.exceptions.Timeout:
				self.send_text.emit("Timed out while trying to load {}. Is the instance down?").format(self.wzd.instance['name'])
				return
			except requests.exceptions.SSLError:
				self.send_text.emit("An SSL error ocurred. Has the HTTPS certificate for {} expired?").format(self.wzd.instance['name'])
				return
			except:
				self.send_text.emit("An unknown error ocurred while trying to validate {}.").format(self.wzd.instance['name'])
				return

			# VERIFYING

			self.update_pbr.emit(2, steps[1])

			# the webfinger URI tells us two very important things:
			# where to find a given user's activitypub outbox, and
			# the true base URL of a given instance
			# for example, mastodon lets you run an instance at subdomain.example.com but still appear as @user@example.com. we need subdomain.example.com.
			self.wzd.instance['webfinger_uri'] = None
			try:
				xml = ElementTree.fromstring(r.text)
				for child in xml:
					if child.tag.lower() in [r"{http://docs.oasis-open.org/ns/xri/xrd-1.0}link", "link"]:
						if child.attrib['rel'] == 'lrdd':
							self.wzd.instance['webfinger_uri'] = child.attrib['template']
							
			except:
				self.send_text.emit("Failed to parse host-meta as XML")
				return
			
			if self.wzd.instance['webfinger_uri'] == None:
				self.send_text.emit("host-meta did not specify WebFinger URI.")
				return

			# use the webfinger URI to determine the instance's actual URL
			self.wzd.instance['url'] = re.search(r"^(https:\/\/[^/]+)", self.wzd.instance['webfinger_uri']).group(1)

			# it's probably a fediverse instance! now we check nodeinfo

			self.update_pbr.emit(3, steps[2])

			# first, the standard way, used by pleroma, misskey, friendica, osada, hubzilla, ganggo, diaspora, and more!
			try:
				r = requests.get("https://{}/.well-known/nodeinfo".format(self.wzd.instance['name']))
				r.raise_for_status()
			except requests.exceptions.HTTPError: 
				# no nodeinfo file! this part is the mastodon way, used by mastodon!
				# (it might also be GNU social, but we'll cross that bridge when we come to it)
				# (it could also be a different type of website altogether -- trying to use "google.com" will also lead down this path)
				if "server" in r.headers and r.headers['server'].lower() == "mastodon":
					self.wzd.instance['type'] = "mastodon" # it could also be glitch-soc but they're the same for the purposes of this program
					# we'll leave the version number blank for now and get it later when we use Mastodon.py
					self.send_true.emit(True)
					return
				else:
					try:
						r = requests.get("https://{}/api/v1/instance")
						j = r.json()
						if re.search(r"^(\d+\.)+\d$", j['version']) != None:
							# its probably mastodon
							# this will handle e.g. 2.1.2.3.4 or 21.2.4 but not commit numbers, which mastodon hopefully doesn't use haha
							# man, if only there was some type of standard
							self.wzd.instance['type'] = "mastodon"
							self.wzd.instance['version'] = j['version']
							self.send_true.emit(True)
							return
						else:
							self.send_text.emit("This instance type is not supported by FediBooks.")
							return
					except:
						# TODO: check for GNU social
						self.send_text.emit("This instance type is not supported by FediBooks.")
						return
					pass
			
			try:
				j = r.json()
			except: 
				self.send_text.emit("Failed to parse nodeinfo as JSON.")
				return

			try:
				for link in j['links']:
					if link['rel'] == "http://nodeinfo.diaspora.software/ns/schema/2.0":
						# look for nodeinfo v2.0 links. TODO: find out if anyone uses 1.0, if they do, add support
						r = requests.get(link['href'])
						j = r.json()
						self.wzd.instance['type'] = j['software']['name'].lower()
						self.wzd.instance['version'] = j['software']['version'].lower()
			except:
				self.send_text.emit("Couldn't load or parse nodeinfo.")
				return

			if self.wzd.instance['type'] != None:
				self.send_true.emit(True)
				return
			else:
				self.send_text.emit("An unknown error ocurred.")
				return
			# end choose_an_instance

		elif pn == "registering_app":
			if self.wzd.app != None:
				# we already have an app, no need to register a new one
				# TODO: if the existing app is invalid somehow, remove it
				self.send_true.emit(True)
				return
			else:
				app = {
					"type": self.wzd.instance['type'],
					"url": self.wzd.instance['url'],
					"credentials": {
						"app_secret": None,
						"app_id": None,
						"access_token": None
					}
				}
				# for information on why FediBooks requests the permissions it does, see https://github.com/Lynnesbian/FediBooks/blob/master/MANUAL.md# permissions
				if self.wzd.instance['type'] in ["mastodon", "pleroma"]:
					# pleroma supports the mastodon API so we'll use that
					# however, Mastodon.py is a bit fucky-wucky, and makes the same mistake as toot! did by converting post IDs to integers, which breaks with pleroma's new, non-integer IDs.
					app["type"] = "mastodon" # overwrite type with "mastodon" in case this is a pleroma instance
					try:
						app['permissions'] = ["read:accounts", "read:follows", "read:notifications", "read:statuses", "write:media", "write:statuses"]
						app["credentials"]["app_id"], app["credentials"]["app_secret"] = Fixtodon.create_app(
							client_name = "FediBooks",
							api_base_url = self.wzd.instance['url'],
							scopes = app['permissions'],
							website = "https://github.com/Lynnesbian/FediBooks"
						)
						self.wzd.app = app
						self.send_true.emit(True)
						return
					except:
						self.send_text.emit("Failed to create {} app.".format(i.title()))
						return
				elif self.wzd.instance['type'] == "misskey":
					try:
						app['permissions'] = ["account-read", "account/read", "drive-write", "following-read", "following-write", "note-read", "note-write", "notification-read"]
						mk_app = Misskey.create_app(
							instanceAddress = self.wzd.instance['url'],
							appName = "FediBooks",
							description = "https://github.com/Lynnesiban/FediBooks",
							permission = app['permissions']
						)
						# PROTIP: the misskey documentation won't tell you much about what this call returns -- it just tells you that you'll get three strings, an array, and a string that can sometimes be null. see here: https://misskey.xyz/docs/en-US/api/endpoints/app/create
						# however, this is wrong. these docs don't tell you that you'll get information such as createdAt or iconUrl, so the docs are no help
						# but by creating an app and dumping the json it returns, we can roughly figure out what's gonig on
						# here's an example:
						# {"createdAt": "2019-02-11T06:08:23.522Z", "userId": null, "name": "test", "description": "test", "permission": ["account-read", "account/read", "note-read", "note-write", "notification-read"], "callbackUrl": null, "secret": "[SECRET GOES HERE]", "id": "[ID GOES HERE]", "iconUrl": "https://misskey.xyz/files/app-default.jpg"}
						# all of that is fairly self-explanatory
						# i don't really know why there's a userId but apart from that it's fairly self-explanatory.
						# self-explanatory is NOT a substitute for documentation, and i have to say that i won't be working particularly hard to support software that provides no support of its own.

						app['credentials']['app_id'] = mk_app['id']
						app['credentials']['app_secret'] = mk_app['secret']
						self.wzd.app = app
						self.send_true.emit(True)
					except:
						self.send_text.emit("Failed to create Misskey app.")
						return

				else:
					# no need to create an app (in fact, it's not even possible. although it will eventually possible for diaspora.)
					self.wzd.app = None
					self.send_true.emit(True)
					return

		# end registering_app

		elif pn == "authorise_fedibooks":
			self.set_pbr_visibility(True)
			if self.wzd.instance['type'] in ["mastodon", "pleroma", "misskey"]:
				if self.wzd.instance['type'] == "misskey":
					# misskey
					pass
				else:
					# mastodon/pleroma
					pass
				pass
			else:
				# username/password
				if self.wzd.instance['type'] == "diaspora":
					# verify that the credentials are correct
					connection = diaspy.connection.Connection(
						pod = self.wzd.instance['url'],
						username = self.ui.txt_username.text(),
						password = self.ui.txt_password.text()
					)
					try:
						connection.login()
					except diaspy.errors.LoginError:
						self.send_text("Login failed. Did you make a typo?")
					
					# diaspy.streams.Activity(connection).post()

		#end authorise_fedibooks

		else:
			self.send_true.emit(True)
			return

class wzdCreateBot(QMainWindow):
	def __init__(self):
		super(wzdCreateBot, self).__init__()
		self.ui = Ui_wzdCreateBot()
		self.ui.setupUi(self)
		self.page_count = self.ui.stk_main.count()
		self.server_port = None
		self.app = None
		self.on_stk_main_currentChanged()

		#########################
		#     TESTING STUFF     #
		# REMOVE WHEN RELEASING #
		#########################
		if testing_mode():
			self.ui.txt_instance.setText("fedi.lynnesbian.space")

	# FUNCTIONS

	@Slot(str)
	@Slot(bool)
	def validate_page_result(self, response):
		self.set_control_buttons_enabled(True)
		self.ui.stk_main.setEnabled(True)
		self.ui.btn_next.setFocus()

		if response is True:
			index = self.ui.stk_main.currentIndex()
			self.ui.stk_main.setCurrentIndex(index + 1)
		else:
			dialogue = dlgWzdError()
			dialogue.present(response)
			self.reset_page()

	@Slot(bool)
	def set_pbr_visibility(self, visible):
		if self.page_name() == "choose_an_instance":
			self.ui.pbr_instance.setVisible(visible)
		elif self.page_name() == "authorise_fedibooks":
			self.ui.pbr_authorisation.setVisible(visible)

	@Slot(int, str)
	def set_pbr_state(self, progress, text):
		pbr = None
		if self.page_name() == "choose_an_instance":
			pbr = self.ui.pbr_instance

		pbr.setValue(progress)
		pbr.setFormat(text)

	def validate_page(self):
		self.validator = thrWzdPageValidator(self)
		self.validator.send_true.connect(self.validate_page_result)
		self.validator.send_text.connect(self.validate_page_result)
		self.validator.update_pbr.connect(self.set_pbr_state)
		self.validator.set_pbr_visibility.connect(self.set_pbr_visibility)
		self.validator.start()
		
	def next_page(self):
		self.set_control_buttons_enabled(False)
		self.ui.stk_main.setEnabled(False)
		self.validate_page()
		# thread.join(30)
			
	def previous_page(self):
		if self.page_name() == "authorise_fedibooks" and self.app != None:
			# we've already registered, skip this page
			self.ui.stk_main.setCurrentIndex(self.ui.stk_main.currentIndex() - 1)
			self.previous_page()
			return
		index = self.ui.stk_main.currentIndex()
		self.ui.stk_main.setCurrentIndex(index - 1)

	def page_name(self):
		return self.ui.stk_main.currentWidget().objectName()

	def reset_page(self):
		if self.page_name() == "choose_an_instance":
			self.ui.pbr_instance.setFormat("Ready")
			self.ui.pbr_instance.setValue(0)
		self.set_pbr_visibility(False)

	def set_control_buttons_enabled(self, state):
		self.ui.btn_next.setEnabled(state)
		self.ui.btn_back.setEnabled(state)

	@Slot(str)
	def open_oauth_page(self, url):
		open_url(url)

	# EVENT HANDLERS
	# GENERAL
	@Slot()
	def on_btn_cancel_pressed(self):
		print("cancel")
	@Slot()
	def on_btn_help_pressed(self):
		page = self.page_name().replace("_", "-")
		if page in ["welcome", "done"]:
			# no specific help for these pages, just direct to the general wizard help instead
			page = "bot-creation-wizard"
		open_url("https://github.com/Lynnesbian/FediBooks/tree/master/MANUAL.md# {}".format(page))
	@Slot()
	def on_btn_back_pressed(self):
		self.previous_page()
	@Slot()
	def on_btn_next_pressed(self):
		self.next_page()

	@Slot(int)
	def on_stk_main_currentChanged(self, page=None):
		# print(self.ui.stk_main.currentWidget().objectName())
		if self.ui.stk_main.currentIndex() == self.page_count - 1:
			self.ui.btn_next.setText("Finish")
		else:
			self.ui.btn_next.setText("Next")

		self.ui.btn_back.setEnabled(self.ui.stk_main.currentIndex() != 0)

		if self.page_name() == "registering_app":
			self.set_control_buttons_enabled(False)
			s = thrOauthResponseServer(self)
			s.send_code.connect(self.code_received)
			s.send_port.connect(self.port_opened)
			s.start()

		if self.page_name() == "authorise_fedibooks":
			# self.app = None
			if self.app == None:
				self.ui.stk_authorise_fedibooks.setCurrentIndex(1)
			else:
				self.ui.stk_authorise_fedibooks.setCurrentIndex(0)

		self.reset_page()
		# print(self.page_name())

	# CREATE ACCOUNT

	@Slot()
	def on_btn_create_account_pressed(self):
		i = self.instance['type']
		u = self.instance['url']
		# v = self.instance['version']
		if i == "mastodon":
			open_url("{}/auth/sign_up".format(u))
		elif i == "pleroma":
			open_url("{}/registration".format(u))
		elif i in ["hubzilla", "osada"]: # not supported yet but may as well prepare for it
			open_url("{}/register".format(u))
		elif i == "diaspora":
			open_url("{}/users/sign_up".format(u))
		else:
			open_url(u)

	# CREATE APP

	@Slot(int)
	def port_opened(self, port):
		self.server_port = port
		print(port)
		self.next_page()

	# AUTHENTICATION

	@Slot()
	def on_btn_auth_code_pressed(self):
		print("beep")
		self.requester = thrOauthCodeRequester(self)
		self.requester.send_url.connect(self.open_oauth_page)
		self.requester.send_error.connect(self.validate_page_result)
		self.requester.start()

	@Slot(str)
	def code_received(self, code):
		# auth code recieved
		pass

