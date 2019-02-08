# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/mainmenu.ui',
# licensing of 'gui/mainmenu.ui' applies.
#
# Created: Sat Feb  9 01:57:31 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainMenu(object):
    def setupUi(self, MainMenu):
        MainMenu.setObjectName("MainMenu")
        MainMenu.resize(438, 331)
        self.centralwidget = QtWidgets.QWidget(MainMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_13.setFont(font)
        self.label_13.setTextFormat(QtCore.Qt.AutoText)
        self.label_13.setScaledContents(True)
        self.label_13.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_13.setObjectName("label_13")
        self.verticalLayout.addWidget(self.label_13)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.btn_botmanager = QtWidgets.QPushButton(self.centralwidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("."), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_botmanager.setIcon(icon)
        self.btn_botmanager.setObjectName("btn_botmanager")
        self.verticalLayout.addWidget(self.btn_botmanager)
        self.btn_settings = QtWidgets.QPushButton(self.centralwidget)
        self.btn_settings.setIcon(icon)
        self.btn_settings.setObjectName("btn_settings")
        self.verticalLayout.addWidget(self.btn_settings)
        self.btn_donate = QtWidgets.QPushButton(self.centralwidget)
        self.btn_donate.setIcon(icon)
        self.btn_donate.setObjectName("btn_donate")
        self.verticalLayout.addWidget(self.btn_donate)
        self.btn_quit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_quit.setIcon(icon)
        self.btn_quit.setObjectName("btn_quit")
        self.verticalLayout.addWidget(self.btn_quit)
        MainMenu.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainMenu)
        QtCore.QObject.connect(self.btn_botmanager, QtCore.SIGNAL("pressed()"), MainMenu.btn_botmanager_pressed)
        QtCore.QObject.connect(self.btn_settings, QtCore.SIGNAL("pressed()"), MainMenu.btn_settings_pressed)
        QtCore.QObject.connect(self.btn_donate, QtCore.SIGNAL("pressed()"), MainMenu.btn_donate_pressed)
        QtCore.QObject.connect(self.btn_quit, QtCore.SIGNAL("pressed()"), MainMenu.btn_quit_pressed)
        QtCore.QMetaObject.connectSlotsByName(MainMenu)

    def retranslateUi(self, MainMenu):
        MainMenu.setWindowTitle(QtWidgets.QApplication.translate("MainMenu", "Main Menu", None, -1))
        self.label_13.setText(QtWidgets.QApplication.translate("MainMenu", "Main Menu", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainMenu", "<html><head/><body><p>Welcome to FediBooks! You have <span style=\" font-weight:600;\">1</span> bot, <span style=\" font-weight:600;\">1</span> of which is currently active. The database of learned content is currently <span style=\" font-weight:600;\">32KiB</span> in size.</p></body></html>", None, -1))
        self.btn_botmanager.setText(QtWidgets.QApplication.translate("MainMenu", "Bot Manager", None, -1))
        self.btn_settings.setText(QtWidgets.QApplication.translate("MainMenu", "Settings", None, -1))
        self.btn_donate.setText(QtWidgets.QApplication.translate("MainMenu", "Donate", None, -1))
        self.btn_quit.setText(QtWidgets.QApplication.translate("MainMenu", "Quit", None, -1))

