# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/botoverview.ui',
# licensing of 'gui/botoverview.ui' applies.
#
# Created: Sat Feb  9 01:57:31 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(579, 386)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
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
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidgetPage1 = QtWidgets.QWidget()
        self.tabWidgetPage1.setObjectName("tabWidgetPage1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tabWidgetPage1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.tabWidgetPage1)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.tabWidgetPage1)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("."), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_3.addWidget(self.pushButton_5)
        self.pushButton_7 = QtWidgets.QPushButton(self.tabWidgetPage1)
        self.pushButton_7.setIcon(icon)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_3.addWidget(self.pushButton_7)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.tabWidget.addTab(self.tabWidgetPage1, "")
        self.tabWidgetPage2 = QtWidgets.QWidget()
        self.tabWidgetPage2.setObjectName("tabWidgetPage2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tabWidgetPage2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.tabWidgetPage2)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.tabWidgetPage2)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.tabWidgetPage2)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.tabWidget.addTab(self.tabWidgetPage2, "")
        self.tabWidgetPage3 = QtWidgets.QWidget()
        self.tabWidgetPage3.setObjectName("tabWidgetPage3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tabWidgetPage3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.tabWidgetPage3)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.tabWidgetPage3)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.tabWidgetPage3)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.tabWidget.addTab(self.tabWidgetPage3, "")
        self.tabWidgetPage4 = QtWidgets.QWidget()
        self.tabWidgetPage4.setObjectName("tabWidgetPage4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tabWidgetPage4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.tabWidgetPage4)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.tabWidgetPage4)
        self.pushButton_6.setIcon(icon)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_6.addWidget(self.pushButton_6)
        self.tabWidget.addTab(self.tabWidgetPage4, "")
        self.tabWidgetPage5 = QtWidgets.QWidget()
        self.tabWidgetPage5.setObjectName("tabWidgetPage5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tabWidgetPage5)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.tabWidgetPage5)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_7.addWidget(self.label_6)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_8 = QtWidgets.QPushButton(self.tabWidgetPage5)
        self.pushButton_8.setIcon(icon)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_4.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.tabWidgetPage5)
        self.pushButton_9.setCheckable(True)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_4.addWidget(self.pushButton_9)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.tabWidget.addTab(self.tabWidgetPage5, "")
        self.tabWidgetPage6 = QtWidgets.QWidget()
        self.tabWidgetPage6.setObjectName("tabWidgetPage6")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tabWidgetPage6)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_7 = QtWidgets.QLabel(self.tabWidgetPage6)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_8.addWidget(self.label_7)
        self.pushButton_10 = QtWidgets.QPushButton(self.tabWidgetPage6)
        self.pushButton_10.setIcon(icon)
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_8.addWidget(self.pushButton_10)
        self.tabWidget.addTab(self.tabWidgetPage6, "")
        self.tabWidgetPage7 = QtWidgets.QWidget()
        self.tabWidgetPage7.setObjectName("tabWidgetPage7")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.tabWidgetPage7)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_8 = QtWidgets.QLabel(self.tabWidgetPage7)
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_9.addWidget(self.label_8)
        self.lineEdit = QtWidgets.QLineEdit(self.tabWidgetPage7)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_9.addWidget(self.lineEdit)
        self.progressBar = QtWidgets.QProgressBar(self.tabWidgetPage7)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_9.addWidget(self.progressBar)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_12 = QtWidgets.QPushButton(self.tabWidgetPage7)
        self.pushButton_12.setIcon(icon)
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout_5.addWidget(self.pushButton_12)
        self.pushButton_11 = QtWidgets.QPushButton(self.tabWidgetPage7)
        self.pushButton_11.setIcon(icon)
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout_5.addWidget(self.pushButton_11)
        self.pushButton_13 = QtWidgets.QPushButton(self.tabWidgetPage7)
        self.pushButton_13.setIcon(icon)
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout_5.addWidget(self.pushButton_13)
        self.verticalLayout_9.addLayout(self.horizontalLayout_5)
        self.tabWidget.addTab(self.tabWidgetPage7, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Bot Overview", None, -1))
        self.label_13.setText(QtWidgets.QApplication.translate("MainWindow", "Bot Overview", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Managing [bot name]", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p>[bot name] is <span style=\" font-weight:600;\">active</span>, and replies are <span style=\" font-weight:600;\">enabled</span>. Its most recent post was 12 minutes ago.</p><p>[bot name] posts <span style=\" font-weight:600;\">every 30 minutes</span>. Filtering is <span style=\" font-weight:600;\">disabled</span>. There are <span style=\" font-weight:600;\">0</span> custom posting rules, and <span style=\" font-weight:600;\">0</span> custom reply rules.</p></body></html>", None, -1))
        self.pushButton_5.setText(QtWidgets.QApplication.translate("MainWindow", "Deactivate", None, -1))
        self.pushButton_7.setText(QtWidgets.QApplication.translate("MainWindow", "Specify rules", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage1), QtWidgets.QApplication.translate("MainWindow", "Status", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p>The database your bot uses to post contains <span style=\" font-weight:600;\">0</span> entries. This is below the recommended minimum of <span style=\" font-weight:600;\">100</span>. Your bot may fail to post, or post repetitive content. The database for all bots is <span style=\" font-weight:600;\">32KiB</span> in size.</p></body></html>", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "Open database location", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("MainWindow", "Browse", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage2), QtWidgets.QApplication.translate("MainWindow", "Database", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p>Replies are currently <span style=\" font-weight:600;\">enabled</span> and <span style=\" font-weight:600;\">working</span>. You have <span style=\" font-weight:600;\">0</span> active reply rules.</p></body></html>", None, -1))
        self.pushButton_3.setText(QtWidgets.QApplication.translate("MainWindow", "Disable replies", None, -1))
        self.pushButton_4.setText(QtWidgets.QApplication.translate("MainWindow", "Specify rules", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage3), QtWidgets.QApplication.translate("MainWindow", "Replies", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p>Your bot is currently learning from <span style=\" font-weight:600;\">1</span> source. </p></body></html>", None, -1))
        self.pushButton_6.setText(QtWidgets.QApplication.translate("MainWindow", "Manage sources", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage4), QtWidgets.QApplication.translate("MainWindow", "Sources", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p>Your bot <span style=\" font-weight:600;\">does not</span> use content warnings when it posts. It <span style=\" font-weight:600;\">does not</span> learn from posts with content warnings.</p></body></html>", None, -1))
        self.pushButton_8.setText(QtWidgets.QApplication.translate("MainWindow", "Set content warning", None, -1))
        self.pushButton_9.setText(QtWidgets.QApplication.translate("MainWindow", "Learn from CW\'d posts", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage5), QtWidgets.QApplication.translate("MainWindow", "Content warnings", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p>Your bot posts every <span style=\" font-weight:600;\">30 minutes</span>, and learns from its sources every <span style=\" font-weight:600;\">30 minutes</span>.</p></body></html>", None, -1))
        self.pushButton_10.setText(QtWidgets.QApplication.translate("MainWindow", "Customise", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage6), QtWidgets.QApplication.translate("MainWindow", "Timing", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p>You can use this page to test your bot, or to manually create posts.</p></body></html>", None, -1))
        self.pushButton_12.setText(QtWidgets.QApplication.translate("MainWindow", "Generate", None, -1))
        self.pushButton_11.setText(QtWidgets.QApplication.translate("MainWindow", "Post", None, -1))
        self.pushButton_13.setText(QtWidgets.QApplication.translate("MainWindow", "Chat", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage7), QtWidgets.QApplication.translate("MainWindow", "Testing", None, -1))
