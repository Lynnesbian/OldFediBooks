# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/dlg_wzd_error.ui',
# licensing of 'gui/dlg_wzd_error.ui' applies.
#
# Created: Sat Feb  9 11:28:23 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
	def setupUi(self, Dialog):
		Dialog.setObjectName("Dialog")
		Dialog.resize(400, 189)
		Dialog.setModal(True)
		self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
		self.verticalLayout.setObjectName("verticalLayout")
		self.label = QtWidgets.QLabel(Dialog)
		self.label.setWordWrap(True)
		self.label.setObjectName("label")
		self.verticalLayout.addWidget(self.label)
		self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName("buttonBox")
		self.verticalLayout.addWidget(self.buttonBox)

		self.retranslateUi(Dialog)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

	def retranslateUi(self, Dialog):
		Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Error", None, -1))
		self.label.setText(QtWidgets.QApplication.translate("Dialog", "There were some problems with the data you entered. Please rectify the following issues and try again.", None, -1))

