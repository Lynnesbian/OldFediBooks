# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/wzd_createrule.ui',
# licensing of 'gui/wzd_createrule.ui' applies.
#
# Created: Sun Feb 10 20:10:17 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(633, 487)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
		self.verticalLayout.setSpacing(0)
		self.verticalLayout.setObjectName("verticalLayout")
		self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
		self.stackedWidget.setObjectName("stackedWidget")
		self.page = QtWidgets.QWidget()
		self.page.setObjectName("page")
		self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page)
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		self.label = QtWidgets.QLabel(self.page)
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
		self.verticalLayout_2.addWidget(self.label)
		self.label_2 = QtWidgets.QLabel(self.page)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
		self.label_2.setSizePolicy(sizePolicy)
		self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
		self.label_2.setWordWrap(True)
		self.label_2.setObjectName("label_2")
		self.verticalLayout_2.addWidget(self.label_2)
		spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.verticalLayout_2.addItem(spacerItem)
		self.pushButton_4 = QtWidgets.QPushButton(self.page)
		self.pushButton_4.setObjectName("pushButton_4")
		self.verticalLayout_2.addWidget(self.pushButton_4)
		self.lay_button_box = QtWidgets.QHBoxLayout()
		self.lay_button_box.setObjectName("lay_button_box")
		self.btn_cancel = QtWidgets.QPushButton(self.page)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap("."), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.btn_cancel.setIcon(icon)
		self.btn_cancel.setObjectName("btn_cancel")
		self.lay_button_box.addWidget(self.btn_cancel)
		self.btn_help = QtWidgets.QPushButton(self.page)
		self.btn_help.setIcon(icon)
		self.btn_help.setObjectName("btn_help")
		self.lay_button_box.addWidget(self.btn_help)
		spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.lay_button_box.addItem(spacerItem1)
		self.btn_back = QtWidgets.QPushButton(self.page)
		self.btn_back.setIcon(icon)
		self.btn_back.setObjectName("btn_back")
		self.lay_button_box.addWidget(self.btn_back)
		self.btn_next = QtWidgets.QPushButton(self.page)
		self.btn_next.setIcon(icon)
		self.btn_next.setDefault(True)
		self.btn_next.setObjectName("btn_next")
		self.lay_button_box.addWidget(self.btn_next)
		self.verticalLayout_2.addLayout(self.lay_button_box)
		self.stackedWidget.addWidget(self.page)
		self.page_2 = QtWidgets.QWidget()
		self.page_2.setObjectName("page_2")
		self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_2)
		self.verticalLayout_3.setObjectName("verticalLayout_3")
		self.label_4 = QtWidgets.QLabel(self.page_2)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
		self.label_4.setSizePolicy(sizePolicy)
		font = QtGui.QFont()
		font.setPointSize(24)
		self.label_4.setFont(font)
		self.label_4.setTextFormat(QtCore.Qt.AutoText)
		self.label_4.setScaledContents(True)
		self.label_4.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
		self.label_4.setObjectName("label_4")
		self.verticalLayout_3.addWidget(self.label_4)
		self.label_3 = QtWidgets.QLabel(self.page_2)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
		self.label_3.setSizePolicy(sizePolicy)
		self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
		self.label_3.setWordWrap(True)
		self.label_3.setObjectName("label_3")
		self.verticalLayout_3.addWidget(self.label_3)
		self.tabWidget = QtWidgets.QTabWidget(self.page_2)
		self.tabWidget.setObjectName("tabWidget")
		self.tab = QtWidgets.QWidget()
		self.tab.setObjectName("tab")
		self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab)
		self.verticalLayout_4.setObjectName("verticalLayout_4")
		self.groupBox = QtWidgets.QGroupBox(self.tab)
		self.groupBox.setCheckable(True)
		self.groupBox.setChecked(False)
		self.groupBox.setObjectName("groupBox")
		self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox)
		self.verticalLayout_7.setContentsMargins(0, -1, 0, 0)
		self.verticalLayout_7.setObjectName("verticalLayout_7")
		self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
		self.lineEdit.setObjectName("lineEdit")
		self.verticalLayout_7.addWidget(self.lineEdit)
		self.checkBox = QtWidgets.QCheckBox(self.groupBox)
		self.checkBox.setObjectName("checkBox")
		self.verticalLayout_7.addWidget(self.checkBox)
		self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox)
		self.checkBox_2.setObjectName("checkBox_2")
		self.verticalLayout_7.addWidget(self.checkBox_2)
		self.verticalLayout_4.addWidget(self.groupBox)
		spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.verticalLayout_4.addItem(spacerItem2)
		self.tabWidget.addTab(self.tab, "")
		self.tab_2 = QtWidgets.QWidget()
		self.tab_2.setObjectName("tab_2")
		self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_2)
		self.verticalLayout_5.setObjectName("verticalLayout_5")
		self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
		self.groupBox_2.setCheckable(True)
		self.groupBox_2.setChecked(False)
		self.groupBox_2.setObjectName("groupBox_2")
		self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_2)
		self.verticalLayout_8.setContentsMargins(0, -1, 0, 0)
		self.verticalLayout_8.setObjectName("verticalLayout_8")
		self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
		self.lineEdit_2.setObjectName("lineEdit_2")
		self.verticalLayout_8.addWidget(self.lineEdit_2)
		self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_2)
		self.checkBox_3.setObjectName("checkBox_3")
		self.verticalLayout_8.addWidget(self.checkBox_3)
		self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox_2)
		self.checkBox_4.setObjectName("checkBox_4")
		self.verticalLayout_8.addWidget(self.checkBox_4)
		self.verticalLayout_5.addWidget(self.groupBox_2)
		self.label_11 = QtWidgets.QLabel(self.tab_2)
		self.label_11.setObjectName("label_11")
		self.verticalLayout_5.addWidget(self.label_11)
		spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.verticalLayout_5.addItem(spacerItem3)
		self.tabWidget.addTab(self.tab_2, "")
		self.tab_3 = QtWidgets.QWidget()
		self.tab_3.setObjectName("tab_3")
		self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_3)
		self.verticalLayout_6.setObjectName("verticalLayout_6")
		self.groupBox_3 = QtWidgets.QGroupBox(self.tab_3)
		self.groupBox_3.setCheckable(True)
		self.groupBox_3.setChecked(False)
		self.groupBox_3.setObjectName("groupBox_3")
		self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox_3)
		self.verticalLayout_9.setContentsMargins(0, -1, 0, 0)
		self.verticalLayout_9.setObjectName("verticalLayout_9")
		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.label_7 = QtWidgets.QLabel(self.groupBox_3)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
		self.label_7.setSizePolicy(sizePolicy)
		self.label_7.setObjectName("label_7")
		self.horizontalLayout.addWidget(self.label_7)
		self.timeEdit = QtWidgets.QTimeEdit(self.groupBox_3)
		self.timeEdit.setObjectName("timeEdit")
		self.horizontalLayout.addWidget(self.timeEdit)
		self.label_8 = QtWidgets.QLabel(self.groupBox_3)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
		self.label_8.setSizePolicy(sizePolicy)
		self.label_8.setObjectName("label_8")
		self.horizontalLayout.addWidget(self.label_8)
		self.timeEdit_2 = QtWidgets.QTimeEdit(self.groupBox_3)
		self.timeEdit_2.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(12, 0, 0)))
		self.timeEdit_2.setObjectName("timeEdit_2")
		self.horizontalLayout.addWidget(self.timeEdit_2)
		spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout.addItem(spacerItem4)
		self.verticalLayout_9.addLayout(self.horizontalLayout)
		self.verticalLayout_6.addWidget(self.groupBox_3)
		spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.verticalLayout_6.addItem(spacerItem5)
		self.tabWidget.addTab(self.tab_3, "")
		self.tab_4 = QtWidgets.QWidget()
		self.tab_4.setObjectName("tab_4")
		self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.tab_4)
		self.verticalLayout_10.setObjectName("verticalLayout_10")
		self.groupBox_4 = QtWidgets.QGroupBox(self.tab_4)
		self.groupBox_4.setCheckable(True)
		self.groupBox_4.setChecked(False)
		self.groupBox_4.setObjectName("groupBox_4")
		self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.groupBox_4)
		self.verticalLayout_11.setContentsMargins(0, -1, 0, 0)
		self.verticalLayout_11.setObjectName("verticalLayout_11")
		self.gridLayout = QtWidgets.QGridLayout()
		self.gridLayout.setObjectName("gridLayout")
		self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_4)
		self.lineEdit_5.setObjectName("lineEdit_5")
		self.gridLayout.addWidget(self.lineEdit_5, 1, 2, 1, 1)
		self.label_6 = QtWidgets.QLabel(self.groupBox_4)
		self.label_6.setObjectName("label_6")
		self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
		self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_4)
		self.comboBox_2.setMinimumSize(QtCore.QSize(100, 0))
		self.comboBox_2.setObjectName("comboBox_2")
		self.comboBox_2.addItem("")
		self.comboBox_2.addItem("")
		self.comboBox_2.addItem("")
		self.comboBox_2.addItem("")
		self.gridLayout.addWidget(self.comboBox_2, 1, 1, 1, 1)
		self.label_5 = QtWidgets.QLabel(self.groupBox_4)
		self.label_5.setObjectName("label_5")
		self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
		self.comboBox = QtWidgets.QComboBox(self.groupBox_4)
		self.comboBox.setMinimumSize(QtCore.QSize(100, 0))
		self.comboBox.setObjectName("comboBox")
		self.comboBox.addItem("")
		self.comboBox.addItem("")
		self.comboBox.addItem("")
		self.comboBox.addItem("")
		self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
		self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_4)
		self.lineEdit_4.setObjectName("lineEdit_4")
		self.gridLayout.addWidget(self.lineEdit_4, 0, 2, 1, 1)
		self.verticalLayout_11.addLayout(self.gridLayout)
		self.verticalLayout_10.addWidget(self.groupBox_4)
		spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.verticalLayout_10.addItem(spacerItem6)
		self.tabWidget.addTab(self.tab_4, "")
		self.tab_5 = QtWidgets.QWidget()
		self.tab_5.setObjectName("tab_5")
		self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_5)
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")
		self.checkBox_5 = QtWidgets.QCheckBox(self.tab_5)
		self.checkBox_5.setObjectName("checkBox_5")
		self.horizontalLayout_2.addWidget(self.checkBox_5)
		spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_2.addItem(spacerItem7)
		self.tabWidget.addTab(self.tab_5, "")
		self.verticalLayout_3.addWidget(self.tabWidget)
		self.lineEdit_3 = QtWidgets.QLineEdit(self.page_2)
		self.lineEdit_3.setClearButtonEnabled(True)
		self.lineEdit_3.setObjectName("lineEdit_3")
		self.verticalLayout_3.addWidget(self.lineEdit_3)
		spacerItem8 = QtWidgets.QSpacerItem(20, 36, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.verticalLayout_3.addItem(spacerItem8)
		self.stackedWidget.addWidget(self.page_2)
		self.page_3 = QtWidgets.QWidget()
		self.page_3.setObjectName("page_3")
		self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.page_3)
		self.verticalLayout_12.setObjectName("verticalLayout_12")
		self.label_9 = QtWidgets.QLabel(self.page_3)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
		self.label_9.setSizePolicy(sizePolicy)
		font = QtGui.QFont()
		font.setPointSize(24)
		self.label_9.setFont(font)
		self.label_9.setTextFormat(QtCore.Qt.AutoText)
		self.label_9.setScaledContents(True)
		self.label_9.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
		self.label_9.setObjectName("label_9")
		self.verticalLayout_12.addWidget(self.label_9)
		self.label_10 = QtWidgets.QLabel(self.page_3)
		self.label_10.setWordWrap(True)
		self.label_10.setObjectName("label_10")
		self.verticalLayout_12.addWidget(self.label_10)
		self.tabWidget_2 = QtWidgets.QTabWidget(self.page_3)
		self.tabWidget_2.setObjectName("tabWidget_2")
		self.tab_6 = QtWidgets.QWidget()
		self.tab_6.setObjectName("tab_6")
		self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.tab_6)
		self.verticalLayout_14.setObjectName("verticalLayout_14")
		self.gridLayout_3 = QtWidgets.QGridLayout()
		self.gridLayout_3.setObjectName("gridLayout_3")
		self.lineEdit_8 = QtWidgets.QLineEdit(self.tab_6)
		self.lineEdit_8.setObjectName("lineEdit_8")
		self.gridLayout_3.addWidget(self.lineEdit_8, 0, 1, 1, 1)
		self.lineEdit_9 = QtWidgets.QLineEdit(self.tab_6)
		self.lineEdit_9.setObjectName("lineEdit_9")
		self.gridLayout_3.addWidget(self.lineEdit_9, 1, 1, 1, 1)
		self.label_15 = QtWidgets.QLabel(self.tab_6)
		self.label_15.setObjectName("label_15")
		self.gridLayout_3.addWidget(self.label_15, 0, 0, 1, 1)
		self.label_16 = QtWidgets.QLabel(self.tab_6)
		self.label_16.setObjectName("label_16")
		self.gridLayout_3.addWidget(self.label_16, 1, 0, 1, 1)
		self.verticalLayout_14.addLayout(self.gridLayout_3)
		self.checkBox_8 = QtWidgets.QCheckBox(self.tab_6)
		self.checkBox_8.setObjectName("checkBox_8")
		self.verticalLayout_14.addWidget(self.checkBox_8)
		self.checkBox_9 = QtWidgets.QCheckBox(self.tab_6)
		self.checkBox_9.setObjectName("checkBox_9")
		self.verticalLayout_14.addWidget(self.checkBox_9)
		spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.verticalLayout_14.addItem(spacerItem9)
		self.tabWidget_2.addTab(self.tab_6, "")
		self.tab_7 = QtWidgets.QWidget()
		self.tab_7.setObjectName("tab_7")
		self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.tab_7)
		self.verticalLayout_13.setObjectName("verticalLayout_13")
		self.gridLayout_2 = QtWidgets.QGridLayout()
		self.gridLayout_2.setObjectName("gridLayout_2")
		self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_7)
		self.lineEdit_6.setObjectName("lineEdit_6")
		self.gridLayout_2.addWidget(self.lineEdit_6, 0, 1, 1, 1)
		self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_7)
		self.lineEdit_7.setObjectName("lineEdit_7")
		self.gridLayout_2.addWidget(self.lineEdit_7, 1, 1, 1, 1)
		self.label_13 = QtWidgets.QLabel(self.tab_7)
		self.label_13.setObjectName("label_13")
		self.gridLayout_2.addWidget(self.label_13, 0, 0, 1, 1)
		self.label_14 = QtWidgets.QLabel(self.tab_7)
		self.label_14.setObjectName("label_14")
		self.gridLayout_2.addWidget(self.label_14, 1, 0, 1, 1)
		self.verticalLayout_13.addLayout(self.gridLayout_2)
		self.checkBox_6 = QtWidgets.QCheckBox(self.tab_7)
		self.checkBox_6.setObjectName("checkBox_6")
		self.verticalLayout_13.addWidget(self.checkBox_6)
		self.checkBox_7 = QtWidgets.QCheckBox(self.tab_7)
		self.checkBox_7.setObjectName("checkBox_7")
		self.verticalLayout_13.addWidget(self.checkBox_7)
		self.label_12 = QtWidgets.QLabel(self.tab_7)
		self.label_12.setObjectName("label_12")
		self.verticalLayout_13.addWidget(self.label_12)
		spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.verticalLayout_13.addItem(spacerItem10)
		self.tabWidget_2.addTab(self.tab_7, "")
		self.tab_8 = QtWidgets.QWidget()
		self.tab_8.setObjectName("tab_8")
		self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.tab_8)
		self.verticalLayout_15.setObjectName("verticalLayout_15")
		self.label_17 = QtWidgets.QLabel(self.tab_8)
		self.label_17.setObjectName("label_17")
		self.verticalLayout_15.addWidget(self.label_17)
		self.lineEdit_10 = QtWidgets.QLineEdit(self.tab_8)
		self.lineEdit_10.setObjectName("lineEdit_10")
		self.verticalLayout_15.addWidget(self.lineEdit_10)
		spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.verticalLayout_15.addItem(spacerItem11)
		self.tabWidget_2.addTab(self.tab_8, "")
		self.tab_9 = QtWidgets.QWidget()
		self.tab_9.setObjectName("tab_9")
		self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.tab_9)
		self.verticalLayout_17.setObjectName("verticalLayout_17")
		self.label_19 = QtWidgets.QLabel(self.tab_9)
		self.label_19.setWordWrap(True)
		self.label_19.setObjectName("label_19")
		self.verticalLayout_17.addWidget(self.label_19)
		self.label_20 = QtWidgets.QLabel(self.tab_9)
		self.label_20.setObjectName("label_20")
		self.verticalLayout_17.addWidget(self.label_20)
		self.lineEdit_11 = QtWidgets.QLineEdit(self.tab_9)
		self.lineEdit_11.setObjectName("lineEdit_11")
		self.verticalLayout_17.addWidget(self.lineEdit_11)
		self.checkBox_10 = QtWidgets.QCheckBox(self.tab_9)
		self.checkBox_10.setObjectName("checkBox_10")
		self.verticalLayout_17.addWidget(self.checkBox_10)
		self.label_21 = QtWidgets.QLabel(self.tab_9)
		self.label_21.setObjectName("label_21")
		self.verticalLayout_17.addWidget(self.label_21)
		self.comboBox_3 = QtWidgets.QComboBox(self.tab_9)
		self.comboBox_3.setObjectName("comboBox_3")
		self.comboBox_3.addItem("")
		self.comboBox_3.addItem("")
		self.comboBox_3.addItem("")
		self.comboBox_3.addItem("")
		self.verticalLayout_17.addWidget(self.comboBox_3)
		spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.verticalLayout_17.addItem(spacerItem12)
		self.tabWidget_2.addTab(self.tab_9, "")
		self.tab_10 = QtWidgets.QWidget()
		self.tab_10.setObjectName("tab_10")
		self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.tab_10)
		self.verticalLayout_16.setObjectName("verticalLayout_16")
		self.label_18 = QtWidgets.QLabel(self.tab_10)
		self.label_18.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
		self.label_18.setWordWrap(True)
		self.label_18.setObjectName("label_18")
		self.verticalLayout_16.addWidget(self.label_18)
		self.tabWidget_2.addTab(self.tab_10, "")
		self.verticalLayout_12.addWidget(self.tabWidget_2)
		self.stackedWidget.addWidget(self.page_3)
		self.page_5 = QtWidgets.QWidget()
		self.page_5.setObjectName("page_5")
		self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.page_5)
		self.verticalLayout_19.setObjectName("verticalLayout_19")
		self.label_24 = QtWidgets.QLabel(self.page_5)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
		self.label_24.setSizePolicy(sizePolicy)
		font = QtGui.QFont()
		font.setPointSize(24)
		self.label_24.setFont(font)
		self.label_24.setTextFormat(QtCore.Qt.AutoText)
		self.label_24.setScaledContents(True)
		self.label_24.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
		self.label_24.setObjectName("label_24")
		self.verticalLayout_19.addWidget(self.label_24)
		self.label_25 = QtWidgets.QLabel(self.page_5)
		self.label_25.setObjectName("label_25")
		self.verticalLayout_19.addWidget(self.label_25)
		self.lineEdit_12 = QtWidgets.QLineEdit(self.page_5)
		self.lineEdit_12.setObjectName("lineEdit_12")
		self.verticalLayout_19.addWidget(self.lineEdit_12)
		spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.verticalLayout_19.addItem(spacerItem13)
		self.stackedWidget.addWidget(self.page_5)
		self.page_4 = QtWidgets.QWidget()
		self.page_4.setObjectName("page_4")
		self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.page_4)
		self.verticalLayout_18.setObjectName("verticalLayout_18")
		self.label_22 = QtWidgets.QLabel(self.page_4)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
		self.label_22.setSizePolicy(sizePolicy)
		font = QtGui.QFont()
		font.setPointSize(24)
		self.label_22.setFont(font)
		self.label_22.setTextFormat(QtCore.Qt.AutoText)
		self.label_22.setScaledContents(True)
		self.label_22.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
		self.label_22.setObjectName("label_22")
		self.verticalLayout_18.addWidget(self.label_22)
		self.label_23 = QtWidgets.QLabel(self.page_4)
		self.label_23.setObjectName("label_23")
		self.verticalLayout_18.addWidget(self.label_23)
		self.checkBox_11 = QtWidgets.QCheckBox(self.page_4)
		self.checkBox_11.setObjectName("checkBox_11")
		self.verticalLayout_18.addWidget(self.checkBox_11)
		spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.verticalLayout_18.addItem(spacerItem14)
		self.stackedWidget.addWidget(self.page_4)
		self.verticalLayout.addWidget(self.stackedWidget)
		MainWindow.setCentralWidget(self.centralwidget)

		self.retranslateUi(MainWindow)
		self.stackedWidget.setCurrentIndex(0)
		self.tabWidget.setCurrentIndex(0)
		self.tabWidget_2.setCurrentIndex(0)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Rule Creation Wizard", None, -1))
		self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Welcome", None, -1))
		self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p>This wizard will guide you through the process of creating a <span style=\" font-weight:600;\">custom reply rule</span> for [bot name].</p><p>Click <span style=\" font-weight:600;\">Next</span> to continue.</p></body></html>", None, -1))
		self.pushButton_4.setText(QtWidgets.QApplication.translate("MainWindow", "Create posting rule instead", None, -1))
		self.btn_cancel.setText(QtWidgets.QApplication.translate("MainWindow", "&Cancel", None, -1))
		self.btn_help.setText(QtWidgets.QApplication.translate("MainWindow", "&Help", None, -1))
		self.btn_back.setText(QtWidgets.QApplication.translate("MainWindow", "&Back", None, -1))
		self.btn_next.setText(QtWidgets.QApplication.translate("MainWindow", "&Next", None, -1))
		self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "Select Conditions", None, -1))
		self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p>First, you need to select some <span style=\" font-weight:600;\">conditions</span> for this rule. <span style=\" font-weight:600;\">Condition</span> are what the bot checks for before activating this rule. For example, you might have a rule that says &quot;add an exclamation mark&quot; that is activated when a post meets the <span style=\" font-weight:600;\">conditions</span> of containing the word &quot;pop&quot;, and being after 12:00PM.</p><p>Once you\'ve selected one or more conditions, click <span style=\" font-weight:600;\">Next</span>.</p></body></html>", None, -1))
		self.groupBox.setTitle(QtWidgets.QApplication.translate("MainWindow", "Enable", None, -1))
		self.lineEdit.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "Hello", None, -1))
		self.checkBox.setText(QtWidgets.QApplication.translate("MainWindow", "Case sensitive", None, -1))
		self.checkBox_2.setText(QtWidgets.QApplication.translate("MainWindow", "Match if it\'s part of another word", None, -1))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtWidgets.QApplication.translate("MainWindow", "Content match", None, -1))
		self.groupBox_2.setTitle(QtWidgets.QApplication.translate("MainWindow", "Enable", None, -1))
		self.lineEdit_2.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "[Rr]eg(ular +)?[Ee]x(?:pression)?", None, -1))
		self.checkBox_3.setText(QtWidgets.QApplication.translate("MainWindow", "Case sensitive", None, -1))
		self.checkBox_4.setText(QtWidgets.QApplication.translate("MainWindow", "Multiline", None, -1))
		self.label_11.setText(QtWidgets.QApplication.translate("MainWindow", "Capture groups used here can be accessed in the next step.", None, -1))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtWidgets.QApplication.translate("MainWindow", "RegEx Match", None, -1))
		self.groupBox_3.setTitle(QtWidgets.QApplication.translate("MainWindow", "Enable", None, -1))
		self.label_7.setText(QtWidgets.QApplication.translate("MainWindow", "Between", None, -1))
		self.label_8.setText(QtWidgets.QApplication.translate("MainWindow", "and", None, -1))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtWidgets.QApplication.translate("MainWindow", "Time of day", None, -1))
		self.groupBox_4.setTitle(QtWidgets.QApplication.translate("MainWindow", "Enable", None, -1))
		self.label_6.setText(QtWidgets.QApplication.translate("MainWindow", "from", None, -1))
		self.comboBox_2.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "any username", None, -1))
		self.comboBox_2.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "username containing", None, -1))
		self.comboBox_2.setItemText(2, QtWidgets.QApplication.translate("MainWindow", "username exactly matching", None, -1))
		self.comboBox_2.setItemText(3, QtWidgets.QApplication.translate("MainWindow", "username matching (RegEx)", None, -1))
		self.label_5.setText(QtWidgets.QApplication.translate("MainWindow", "Reply comes from", None, -1))
		self.comboBox.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "any instance", None, -1))
		self.comboBox.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "instance containing", None, -1))
		self.comboBox.setItemText(2, QtWidgets.QApplication.translate("MainWindow", "instance exactly matching", None, -1))
		self.comboBox.setItemText(3, QtWidgets.QApplication.translate("MainWindow", "intance matching (RegEx)", None, -1))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QtWidgets.QApplication.translate("MainWindow", "Reply source", None, -1))
		self.checkBox_5.setText(QtWidgets.QApplication.translate("MainWindow", "Enable (overrides all other conditions)", None, -1))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QtWidgets.QApplication.translate("MainWindow", "Global", None, -1))
		self.lineEdit_3.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "Enter text to test the condition against here", None, -1))
		self.label_9.setText(QtWidgets.QApplication.translate("MainWindow", "Select Action", None, -1))
		self.label_10.setText(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p>Your bot now needs an <span style=\" font-weight:600;\">action</span> to take after the <span style=\" font-weight:600;\">conditions</span> are met. This can be anything from posting a custom message, modifying text, or even not posting at all.</p><p>Unlike conditions, <span style=\" font-weight:600;\">you can only specify one action</span>. The action used is determined by the tab you\'re currently viewing when you click <span style=\" font-weight:600;\">Next</span>.</p></body></html>", None, -1))
		self.lineEdit_8.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "sad", None, -1))
		self.lineEdit_9.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "happy", None, -1))
		self.label_15.setText(QtWidgets.QApplication.translate("MainWindow", "Find", None, -1))
		self.label_16.setText(QtWidgets.QApplication.translate("MainWindow", "Replace with", None, -1))
		self.checkBox_8.setText(QtWidgets.QApplication.translate("MainWindow", "Case sensitive", None, -1))
		self.checkBox_9.setText(QtWidgets.QApplication.translate("MainWindow", "Multiline", None, -1))
		self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), QtWidgets.QApplication.translate("MainWindow", "Find and Replace", None, -1))
		self.lineEdit_6.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "My name is (.*)", None, -1))
		self.lineEdit_7.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "Hello, \\1", None, -1))
		self.label_13.setText(QtWidgets.QApplication.translate("MainWindow", "Find", None, -1))
		self.label_14.setText(QtWidgets.QApplication.translate("MainWindow", "Replace with", None, -1))
		self.checkBox_6.setText(QtWidgets.QApplication.translate("MainWindow", "Case sensitive", None, -1))
		self.checkBox_7.setText(QtWidgets.QApplication.translate("MainWindow", "Multiline", None, -1))
		self.label_12.setText(QtWidgets.QApplication.translate("MainWindow", "Capture groups used in the previous step can be accessed here.", None, -1))
		self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), QtWidgets.QApplication.translate("MainWindow", "RegEx", None, -1))
		self.label_17.setText(QtWidgets.QApplication.translate("MainWindow", "Overwrite generated post with", None, -1))
		self.lineEdit_10.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "I\'m sorry, Dave. I\'m afraid I can\'t toot that.", None, -1))
		self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), QtWidgets.QApplication.translate("MainWindow", "Specify content", None, -1))
		self.label_19.setText(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Use this option with extreme caution.</span> The command will be run as the current user from the current directory. <span style=\" font-weight:600;\">This option can be very dangerous if used improperly.</span></p></body></html>", None, -1))
		self.label_20.setText(QtWidgets.QApplication.translate("MainWindow", "Run this command:", None, -1))
		self.lineEdit_11.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "echo \"Hello there!\"", None, -1))
		self.checkBox_10.setText(QtWidgets.QApplication.translate("MainWindow", "Post the output (stdout)", None, -1))
		self.label_21.setText(QtWidgets.QApplication.translate("MainWindow", "In case of error (non-zero exit code):", None, -1))
		self.comboBox_3.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "Post stdout", None, -1))
		self.comboBox_3.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "Post stderr", None, -1))
		self.comboBox_3.setItemText(2, QtWidgets.QApplication.translate("MainWindow", "Post an error message", None, -1))
		self.comboBox_3.setItemText(3, QtWidgets.QApplication.translate("MainWindow", "Don\'t post anything", None, -1))
		self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_9), QtWidgets.QApplication.translate("MainWindow", "Run command", None, -1))
		self.label_18.setText(QtWidgets.QApplication.translate("MainWindow", "If you choose this option, your bot won\'t post at all if a post meets the specified conditions. It will not create a new post to use instead. If your bot posts every 30 minutes, it won\'t post for another 30 minutes, for example. Use this option with caution.", None, -1))
		self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_10), QtWidgets.QApplication.translate("MainWindow", "Don\'t post", None, -1))
		self.label_24.setText(QtWidgets.QApplication.translate("MainWindow", "Set Rule Name", None, -1))
		self.label_25.setText(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p>Enter a descriptive name for your rule below, then click <span style=\" font-weight:600;\">Next</span> to continue.</p></body></html>", None, -1))
		self.lineEdit_12.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "Ignore posts by @jerk@bad.website", None, -1))
		self.label_22.setText(QtWidgets.QApplication.translate("MainWindow", "Done!", None, -1))
		self.label_23.setText(QtWidgets.QApplication.translate("MainWindow", "Your rule has been created and is ready to be enabled.", None, -1))
		self.checkBox_11.setText(QtWidgets.QApplication.translate("MainWindow", "Enable rule now", None, -1))

