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

import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile
import webbrowser  

from .uic.ui_wzd_createbot import Ui_wzdCreateBot

class wzdCreateBot(QMainWindow):
	def __init__(self):
		super(wzdCreateBot, self).__init__()
		self.ui = Ui_wzdCreateBot()
		self.ui.setupUi(self)
		self.pageCount = self.ui.stackedWidget.count()

	# FUNCTIONS
	def validate_page(self):
		return "Example"
		# return True
	def next_page(self):
		index = self.ui.stackedWidget.currentIndex()
		if self.validate_page() is True:
			self.ui.stackedWidget.setCurrentIndex(index + 1)
	def previous_page(self):
		index = self.ui.stackedWidget.currentIndex()
		self.ui.stackedWidget.setCurrentIndex(index - 1)

	# EVENT HANDLERS
	def btn_cancel_pressed(self):
		print("cancel")
	def btn_help_pressed(self):
		webbrowser.open(
			"https://github.com/Lynnesbian/FediBooks/tree/master/MANUAL.md#{}".format(
				self.ui.stackedWidget.currentWidget().objectName().replace("_", "-")), new=2, autoraise=True)
	def btn_back_pressed(self):
		self.previous_page()
	def btn_next_pressed(self):
		self.next_page()
	def stk_index_changed(self):
		print(self.ui.stackedWidget.currentWidget().objectName())
		if self.ui.stackedWidget.currentIndex() == self.pageCount - 1:
			self.ui.btn_next.setText("Finish")
		else:
			self.ui.btn_next.setText("Next")

		self.ui.btn_back.setEnabled(self.ui.stackedWidget.currentIndex() != 0)