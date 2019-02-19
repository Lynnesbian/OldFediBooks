# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FediBooks/gui/unlock.ui',
# licensing of 'FediBooks/gui/unlock.ui' applies.
#
# Created: Tue Feb 19 16:37:30 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(368, 228)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
		self.verticalLayout.setObjectName("verticalLayout")
		self.label = QtWidgets.QLabel(self.centralwidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
		self.label.setSizePolicy(sizePolicy)
		font = QtGui.QFont()
		font.setPointSize(24)
		self.label.setFont(font)
		self.label.setTextFormat(QtCore.Qt.AutoText)
		self.label.setScaledContents(True)
		self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
		self.label.setObjectName("label")
		self.verticalLayout.addWidget(self.label)
		self.label_2 = QtWidgets.QLabel(self.centralwidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
		self.label_2.setSizePolicy(sizePolicy)
		self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
		self.label_2.setWordWrap(True)
		self.label_2.setObjectName("label_2")
		self.verticalLayout.addWidget(self.label_2)
		self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
		self.lineEdit.setObjectName("lineEdit")
		self.verticalLayout.addWidget(self.lineEdit)
		spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.verticalLayout.addItem(spacerItem)
		self.hbx_button_box = QtWidgets.QHBoxLayout()
		self.hbx_button_box.setObjectName("hbx_button_box")
		self.btn_cancel = QtWidgets.QPushButton(self.centralwidget)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap("."), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.btn_cancel.setIcon(icon)
		self.btn_cancel.setObjectName("btn_cancel")
		self.hbx_button_box.addWidget(self.btn_cancel)
		self.btn_help = QtWidgets.QPushButton(self.centralwidget)
		self.btn_help.setIcon(icon)
		self.btn_help.setObjectName("btn_help")
		self.hbx_button_box.addWidget(self.btn_help)
		spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.hbx_button_box.addItem(spacerItem1)
		self.btn_ok = QtWidgets.QPushButton(self.centralwidget)
		self.btn_ok.setIcon(icon)
		self.btn_ok.setObjectName("btn_ok")
		self.hbx_button_box.addWidget(self.btn_ok)
		self.verticalLayout.addLayout(self.hbx_button_box)
		MainWindow.setCentralWidget(self.centralwidget)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Enter Password", None, -1))
		self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Enter Password", None, -1))
		self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p>FediBooks is currently locked with a password. Please enter your FediBooks password to decrypt the database and continue.</p></body></html>", None, -1))
		self.lineEdit.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "Password", None, -1))
		self.btn_cancel.setText(QtWidgets.QApplication.translate("MainWindow", "&Cancel", None, -1))
		self.btn_help.setText(QtWidgets.QApplication.translate("MainWindow", "&Help", None, -1))
		self.btn_ok.setText(QtWidgets.QApplication.translate("MainWindow", "&Unlock", None, -1))

