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

import sys, faulthandler
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile
import webbrowser  

from FediBooks.uic.ui_mainmenu import Ui_MainMenu
from FediBooks.wzd_createbot import wzdCreateBot

faulthandler.enable()
class MainMenu(QMainWindow):
	def __init__(self):
		super(MainMenu, self).__init__()
		self.ui = Ui_MainMenu()
		self.ui.setupUi(self)
	def btn_botmanager_pressed(self):
		print("bot manager")
	def btn_settings_pressed(self):
		print("settings")
	def btn_donate_pressed(self):
		webbrowser.open("https://github.com/Lynnesbian/FediBooks/tree/master/README.md#Donations", new=2, autoraise=True)
	def btn_quit_pressed(self):
		print("quit")

if __name__ == "__main__":
	app = QApplication(sys.argv)

	# window = MainMenu()
	window = wzdCreateBot()
	window.show()

	sys.exit(app.exec_())