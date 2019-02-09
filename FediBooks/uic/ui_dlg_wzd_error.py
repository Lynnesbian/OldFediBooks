# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/dlg_wzd_error.ui',
# licensing of 'gui/dlg_wzd_error.ui' applies.
#
# Created: Sat Feb  9 11:51:30 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_dlgWzdError(object):
	def setupUi(self, dlgWzdError):
		dlgWzdError.setObjectName("dlgWzdError")
		dlgWzdError.resize(400, 189)
		dlgWzdError.setModal(True)
		self.verticalLayout = QtWidgets.QVBoxLayout(dlgWzdError)
		self.verticalLayout.setObjectName("verticalLayout")
		self.label = QtWidgets.QLabel(dlgWzdError)
		self.label.setWordWrap(True)
		self.label.setObjectName("label")
		self.verticalLayout.addWidget(self.label)
		self.buttonBox = QtWidgets.QDialogButtonBox(dlgWzdError)
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName("buttonBox")
		self.verticalLayout.addWidget(self.buttonBox)

		self.retranslateUi(dlgWzdError)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), dlgWzdError.accept)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), dlgWzdError.reject)
		QtCore.QMetaObject.connectSlotsByName(dlgWzdError)

	def retranslateUi(self, dlgWzdError):
		dlgWzdError.setWindowTitle(QtWidgets.QApplication.translate("dlgWzdError", "Error", None, -1))
		self.label.setText(QtWidgets.QApplication.translate("dlgWzdError", "There were some problems with the data you entered. Please rectify the following issues and try again.", None, -1))

