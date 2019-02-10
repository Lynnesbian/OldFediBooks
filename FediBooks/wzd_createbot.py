#!/usr/bin/env python3
# Copyright (C)2019 Lynnesbian (https://fedi.lynnesbian.space/@lynnesbian)

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
from PySide2.QtCore import QFile, Signal, Slot, QObject
import sys, webbrowser, re, threading
import xml.etree.ElementTree as ElementTree
import requests

from .uic.ui_wzd_createbot import Ui_wzdCreateBot
from .uic.ui_dlg_wzd_error import Ui_dlgWzdError

class dlgWzdError(QDialog):
	def __init__(self):
		super(dlgWzdError, self).__init__()
		self.ui = Ui_dlgWzdError()
		self.ui.setupUi(self)

	def accepted(self):
		self.done(1)

	def present(self, text):
		self.ui.label.setText("There were some problems with the data you entered. Please rectify the following issues and try again.\n\n{}\n\nIf you believe this to be an error, please open a GitHub issue, or notify Lynne (@lynnesbian.fedi.lynnesbian.space)".format(text))
		self.exec()

class wzdPageValidationHandler(QObject):
	send_true = Signal(bool)
	send_text = Signal(str)
		
class wzdCreateBot(QMainWindow):
	def __init__(self):
		super(wzdCreateBot, self).__init__()
		self.ui = Ui_wzdCreateBot()
		self.ui.setupUi(self)
		self.pageCount = self.ui.stkMain.count()

	# FUNCTIONS

	@Slot(str)
	@Slot(bool)
	def validate_page_result(self, response):
		if response is True:
			index = self.ui.stkMain.currentIndex()
			self.ui.stkMain.setCurrentIndex(index + 1)
		else:
			dialogue = dlgWzdError()
			dialogue.present(response)
		
		self.ui.btn_next.setEnabled(True)

	def validate_page(self):
		out = wzdPageValidationHandler()
		out.send_true.connect(self.validate_page_result)
		out.send_text.connect(self.validate_page_result)
		pn = self.page_name()

		if pn == "choose_an_instance":
			steps = ["Connecting", "Verifying", "Checking instance type"]

			# CONNECTING

			self.ui.pbr_instance.setFormat(steps[0])
			self.ui.pbr_instance.setValue(1)
			self.ui.pbr_instance.show()
			self.instance = {
				"name":None,
				"type":None,
				"version":None
			}
			try:
				self.instance['name'] = re.search(r"(?:https?:\/\/)?((?:\w+\.)+\w+)\/?", self.ui.txt_instance.text()).group(1)
			except:
				out.send_text.emit("The instance URL you provided is not a valid URL.")
				return
			#valid URL, check if it's actually an instance
			#afaik the best way to do this is to check for a host-meta file containing a link rel="lrdd"
			#mastodon refuses to federate with non-HTTPS websites, and you can set up HTTPS for free in ten minutes, so there's really no reason not to enforce it
			try:
				r = requests.get("https://{}/.well-known/host-meta".format(self.instance), timeout=30)
			except requests.exceptions.Timeout:
				out.send_text.emit("Timed out while trying to load {}. Is the instance down?").format(self.instance)
				return
			except requests.exceptions.SSLError:
				out.send_text.emit("An SSL error ocurred. Has the HTTPS certificate for {} expired?").format(self.instance)
				return
			except:
				out.send_text.emit("An unknown error ocurred while trying to validate {}.").format(self.instance)
				return

			# VERIFYING

			self.ui.pbr_instance.setFormat(steps[1])
			self.ui.pbr_instance.setValue(2)

			self.webfinger_uri = None
			try:
				xml = ElementTree.fromstring(r.text)
				for child in xml:
					if child.tag.lower() in [r"{http://docs.oasis-open.org/ns/xri/xrd-1.0}link", "link"]:
						print(child.attrib)
						if child.attrib['rel'] == 'lrdd':
							self.webfinger_uri = child.attrib['template']
							
			except:
				out.send_text.emit("Failed to parse host-meta as XML")
				return
			
			if self.webfinger_uri == None:
				out.send_text.emit("host-meta did not specify WebFinger URI.")
				return

			#it's probably a fediverse instance! now we check nodeinfo

			#first, the standard way, used by pleroma, misskey, friendica, osada, hubzilla, ganggo, diaspora, and more!
			try:
				r = requests.get("https://{}/.well-known/nodeinfo".format(self.instance))
				r.raise_for_status()
			except requests.exceptions.HTTPError: 
				#no nodeinfo file! this part is the mastodon way, used by mastodon!
				#(it might also be GNU social, but we'll cross that bridge when we come to it)
				if "server" in r.headers and r.headers['server'].lower() == "mastodon":
					self.instance['type'] = "mastodon" #it could also be glitch-soc but they're the same for the purposes of this program
					#we'll leave the version number blank for now and get it later when we use Mastodon.py
				else:
					try:
						r = requests.get("https://{}/api/v1/instance")
						j = r.json()
						if re.search(r"^(\d+\.)+\d$", j['version']) != None:
							#its probably mastodon
							#this will handle e.g. 2.1.2.3.4 or 21.2.4 but not commit numbers, which mastodon hopefully doesn't use haha
							#man, if only there was some type of standard
							self.instance['type'] = "mastodon"
							self.instance['version'] = j['version']
						else:
							out.send_text.emit("The instance type is not supported by FediBooks.")
							return
					except:
						#TODO: check for GNU social
						out.send_text.emit("The instance type is not supported by FediBooks.")
						return
					pass
			
			try:
				j = r.json()
			except: 
				out.send_text.emit("Failed to parse nodeinfo as JSON.")
				return

			try:
				for link in j['links']:
					if link['rel'] == "http://nodeinfo.diaspora.software/ns/schema/2.0":
						r = requests.get(link['href'])
						j = r.json()
						self.instance['type'] = j['software']['name'].lower()
						self.instance['version'] = j['software']['version'].lower()
			except:
				out.send_text.emit("Couldn't load or parse nodeinfo.")
				return

			if self.instance['type'] != None:
				out.send_true.emit(True)
				return
			else:
				out.send_text.emit("An unknown error ocurred.")
				return
			#end choose_an_instance

		else:
			out.send_true.emit(True)
			return
	def next_page(self):
		self.ui.btn_next.setEnabled(False)
		thread = threading.Thread(target=self.validate_page)
		# thread.daemon = True
		thread.start()
			
	def previous_page(self):
		index = self.ui.stkMain.currentIndex()
		self.ui.stkMain.setCurrentIndex(index - 1)

	def page_name(self):
		return self.ui.stkMain.currentWidget().objectName()

	# EVENT HANDLERS
	def btn_cancel_pressed(self):
		print("cancel")
	def btn_help_pressed(self):
		webbrowser.open(
			"https://github.com/Lynnesbian/FediBooks/tree/master/MANUAL.md#{}".format(
				self.page_name().replace("_", "-")), new=2, autoraise=True)
	def btn_back_pressed(self):
		self.previous_page()
	def btn_next_pressed(self):
		self.next_page()
	def stk_index_changed(self):
		print(self.ui.stkMain.currentWidget().objectName())
		if self.ui.stkMain.currentIndex() == self.pageCount - 1:
			self.ui.btn_next.setText("Finish")
		else:
			self.ui.btn_next.setText("Next")

		self.ui.btn_back.setEnabled(self.ui.stkMain.currentIndex() != 0)