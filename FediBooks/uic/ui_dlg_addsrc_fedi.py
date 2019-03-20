# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FediBooks/gui/dlg_addsrc_fedi.ui',
# licensing of 'FediBooks/gui/dlg_addsrc_fedi.ui' applies.
#
# Created: Wed Mar 20 12:17:35 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_dlgAddSrcFedi(object):
	def setupUi(self, dlgAddSrcFedi):
		dlgAddSrcFedi.setObjectName("dlgAddSrcFedi")
		dlgAddSrcFedi.resize(464, 264)
		self.verticalLayout = QtWidgets.QVBoxLayout(dlgAddSrcFedi)
		self.verticalLayout.setObjectName("verticalLayout")
		self.label_3 = QtWidgets.QLabel(dlgAddSrcFedi)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
		self.label_3.setSizePolicy(sizePolicy)
		font = QtGui.QFont()
		font.setPointSize(24)
		self.label_3.setFont(font)
		self.label_3.setTextFormat(QtCore.Qt.AutoText)
		self.label_3.setScaledContents(True)
		self.label_3.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
		self.label_3.setObjectName("label_3")
		self.verticalLayout.addWidget(self.label_3)
		self.label = QtWidgets.QLabel(dlgAddSrcFedi)
		font = QtGui.QFont()
		font.setPointSize(12)
		self.label.setFont(font)
		self.label.setAlignment(QtCore.Qt.AlignCenter)
		self.label.setObjectName("label")
		self.verticalLayout.addWidget(self.label)
		self.lineEdit = QtWidgets.QLineEdit(dlgAddSrcFedi)
		self.lineEdit.setText("")
		self.lineEdit.setObjectName("lineEdit")
		self.verticalLayout.addWidget(self.lineEdit)
		self.progressBar = QtWidgets.QProgressBar(dlgAddSrcFedi)
		self.progressBar.setMinimum(0)
		self.progressBar.setMaximum(1)
		self.progressBar.setProperty("value", 0)
		self.progressBar.setInvertedAppearance(False)
		self.progressBar.setObjectName("progressBar")
		self.verticalLayout.addWidget(self.progressBar)
		spacerItem = QtWidgets.QSpacerItem(413, 62, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.verticalLayout.addItem(spacerItem)
		self.buttonBox = QtWidgets.QDialogButtonBox(dlgAddSrcFedi)
		self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName("buttonBox")
		self.verticalLayout.addWidget(self.buttonBox)

		self.retranslateUi(dlgAddSrcFedi)
		QtCore.QMetaObject.connectSlotsByName(dlgAddSrcFedi)

	def retranslateUi(self, dlgAddSrcFedi):
		dlgAddSrcFedi.setWindowTitle(QtWidgets.QApplication.translate("dlgAddSrcFedi", "Dialog", None, -1))
		self.label_3.setText(QtWidgets.QApplication.translate("dlgAddSrcFedi", "Add Source", None, -1))
		self.label.setText(QtWidgets.QApplication.translate("dlgAddSrcFedi", "Fediverse account", None, -1))
		self.lineEdit.setPlaceholderText(QtWidgets.QApplication.translate("dlgAddSrcFedi", "@user@instan.ce", None, -1))
		self.progressBar.setFormat(QtWidgets.QApplication.translate("dlgAddSrcFedi", "Verifying", None, -1))

