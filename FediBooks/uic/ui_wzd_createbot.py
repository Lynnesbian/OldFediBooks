# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/wzd_createbot.ui',
# licensing of 'gui/wzd_createbot.ui' applies.
#
# Created: Mon Feb 11 17:57:20 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_wzdCreateBot(object):
	def setupUi(self, wzdCreateBot):
		wzdCreateBot.setObjectName("wzdCreateBot")
		wzdCreateBot.resize(576, 456)
		self.centralwidget = QtWidgets.QWidget(wzdCreateBot)
		self.centralwidget.setObjectName("centralwidget")
		self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.centralwidget)
		self.verticalLayout_13.setSpacing(0)
		self.verticalLayout_13.setObjectName("verticalLayout_13")
		self.verticalLayout = QtWidgets.QVBoxLayout()
		self.verticalLayout.setObjectName("verticalLayout")
		self.stkMain = QtWidgets.QStackedWidget(self.centralwidget)
		self.stkMain.setObjectName("stkMain")
		self.welcome = QtWidgets.QWidget()
		self.welcome.setObjectName("welcome")
		self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.welcome)
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		self.label = QtWidgets.QLabel(self.welcome)
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
		self.label_2 = QtWidgets.QLabel(self.welcome)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
		self.label_2.setSizePolicy(sizePolicy)
		self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
		self.label_2.setWordWrap(True)
		self.label_2.setObjectName("label_2")
		self.verticalLayout_2.addWidget(self.label_2)
		self.pushButton_12 = QtWidgets.QPushButton(self.welcome)
		self.pushButton_12.setObjectName("pushButton_12")
		self.verticalLayout_2.addWidget(self.pushButton_12)
		spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.verticalLayout_2.addItem(spacerItem)
		self.stkMain.addWidget(self.welcome)
		self.choose_an_instance = QtWidgets.QWidget()
		self.choose_an_instance.setObjectName("choose_an_instance")
		self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.choose_an_instance)
		self.verticalLayout_3.setObjectName("verticalLayout_3")
		self.label_3 = QtWidgets.QLabel(self.choose_an_instance)
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
		self.verticalLayout_3.addWidget(self.label_3)
		self.label_4 = QtWidgets.QLabel(self.choose_an_instance)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
		self.label_4.setSizePolicy(sizePolicy)
		self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
		self.label_4.setWordWrap(True)
		self.label_4.setObjectName("label_4")
		self.verticalLayout_3.addWidget(self.label_4)
		self.txt_instance = QtWidgets.QLineEdit(self.choose_an_instance)
		self.txt_instance.setObjectName("txt_instance")
		self.verticalLayout_3.addWidget(self.txt_instance)
		self.pbr_instance = QtWidgets.QProgressBar(self.choose_an_instance)
		self.pbr_instance.setMinimum(0)
		self.pbr_instance.setMaximum(3)
		self.pbr_instance.setProperty("value", 0)
		self.pbr_instance.setObjectName("pbr_instance")
		self.verticalLayout_3.addWidget(self.pbr_instance)
		spacerItem1 = QtWidgets.QSpacerItem(20, 101, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.verticalLayout_3.addItem(spacerItem1)
		self.stkMain.addWidget(self.choose_an_instance)
		self.create_account = QtWidgets.QWidget()
		self.create_account.setObjectName("create_account")
		self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.create_account)
		self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout_4.setObjectName("verticalLayout_4")
		self.stkCreateAccount = QtWidgets.QStackedWidget(self.create_account)
		self.stkCreateAccount.setObjectName("stkCreateAccount")
		self.page_3 = QtWidgets.QWidget()
		self.page_3.setObjectName("page_3")
		self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page_3)
		self.verticalLayout_9.setObjectName("verticalLayout_9")
		self.label_5 = QtWidgets.QLabel(self.page_3)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
		self.label_5.setSizePolicy(sizePolicy)
		font = QtGui.QFont()
		font.setPointSize(24)
		self.label_5.setFont(font)
		self.label_5.setTextFormat(QtCore.Qt.AutoText)
		self.label_5.setScaledContents(True)
		self.label_5.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
		self.label_5.setObjectName("label_5")
		self.verticalLayout_9.addWidget(self.label_5)
		self.label_6 = QtWidgets.QLabel(self.page_3)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
		self.label_6.setSizePolicy(sizePolicy)
		self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
		self.label_6.setWordWrap(True)
		self.label_6.setObjectName("label_6")
		self.verticalLayout_9.addWidget(self.label_6)
		self.btn_create_account = QtWidgets.QPushButton(self.page_3)
		self.btn_create_account.setObjectName("btn_create_account")
		self.verticalLayout_9.addWidget(self.btn_create_account)
		self.stkCreateAccount.addWidget(self.page_3)
		self.page_4 = QtWidgets.QWidget()
		self.page_4.setObjectName("page_4")
		self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.page_4)
		self.verticalLayout_8.setObjectName("verticalLayout_8")
		self.label_9 = QtWidgets.QLabel(self.page_4)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
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
		self.verticalLayout_8.addWidget(self.label_9)
		self.label_22 = QtWidgets.QLabel(self.page_4)
		self.label_22.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
		self.label_22.setWordWrap(True)
		self.label_22.setObjectName("label_22")
		self.verticalLayout_8.addWidget(self.label_22)
		self.stkCreateAccount.addWidget(self.page_4)
		self.verticalLayout_4.addWidget(self.stkCreateAccount)
		spacerItem2 = QtWidgets.QSpacerItem(20, 117, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.verticalLayout_4.addItem(spacerItem2)
		self.stkMain.addWidget(self.create_account)
		self.registering_fedibooks = QtWidgets.QWidget()
		self.registering_fedibooks.setObjectName("registering_fedibooks")
		self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.registering_fedibooks)
		self.verticalLayout_12.setObjectName("verticalLayout_12")
		self.label_24 = QtWidgets.QLabel(self.registering_fedibooks)
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
		self.verticalLayout_12.addWidget(self.label_24)
		self.label_25 = QtWidgets.QLabel(self.registering_fedibooks)
		self.label_25.setWordWrap(True)
		self.label_25.setObjectName("label_25")
		self.verticalLayout_12.addWidget(self.label_25)
		self.pbr_registering_app = QtWidgets.QProgressBar(self.registering_fedibooks)
		self.pbr_registering_app.setMinimum(0)
		self.pbr_registering_app.setMaximum(0)
		self.pbr_registering_app.setProperty("value", 0)
		self.pbr_registering_app.setTextVisible(True)
		self.pbr_registering_app.setObjectName("pbr_registering_app")
		self.verticalLayout_12.addWidget(self.pbr_registering_app)
		spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.verticalLayout_12.addItem(spacerItem3)
		self.stkMain.addWidget(self.registering_fedibooks)
		self.authorise_fedibooks = QtWidgets.QWidget()
		self.authorise_fedibooks.setObjectName("authorise_fedibooks")
		self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.authorise_fedibooks)
		self.verticalLayout_5.setObjectName("verticalLayout_5")
		self.label_7 = QtWidgets.QLabel(self.authorise_fedibooks)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
		self.label_7.setSizePolicy(sizePolicy)
		font = QtGui.QFont()
		font.setPointSize(24)
		self.label_7.setFont(font)
		self.label_7.setTextFormat(QtCore.Qt.AutoText)
		self.label_7.setScaledContents(True)
		self.label_7.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
		self.label_7.setObjectName("label_7")
		self.verticalLayout_5.addWidget(self.label_7)
		self.stackedWidget = QtWidgets.QStackedWidget(self.authorise_fedibooks)
		self.stackedWidget.setObjectName("stackedWidget")
		self.oauth = QtWidgets.QWidget()
		self.oauth.setObjectName("oauth")
		self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.oauth)
		self.verticalLayout_14.setSpacing(6)
		self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout_14.setObjectName("verticalLayout_14")
		self.label_8 = QtWidgets.QLabel(self.oauth)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
		self.label_8.setSizePolicy(sizePolicy)
		self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
		self.label_8.setWordWrap(True)
		self.label_8.setObjectName("label_8")
		self.verticalLayout_14.addWidget(self.label_8)
		self.btn_auth_code = QtWidgets.QPushButton(self.oauth)
		self.btn_auth_code.setObjectName("btn_auth_code")
		self.verticalLayout_14.addWidget(self.btn_auth_code)
		self.txt_auth_code = QtWidgets.QLineEdit(self.oauth)
		self.txt_auth_code.setObjectName("txt_auth_code")
		self.verticalLayout_14.addWidget(self.txt_auth_code)
		self.stackedWidget.addWidget(self.oauth)
		self.username_password = QtWidgets.QWidget()
		self.username_password.setObjectName("username_password")
		self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.username_password)
		self.verticalLayout_15.setObjectName("verticalLayout_15")
		self.label_26 = QtWidgets.QLabel(self.username_password)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
		self.label_26.setSizePolicy(sizePolicy)
		self.label_26.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
		self.label_26.setWordWrap(True)
		self.label_26.setObjectName("label_26")
		self.verticalLayout_15.addWidget(self.label_26)
		self.lineEdit_2 = QtWidgets.QLineEdit(self.username_password)
		self.lineEdit_2.setObjectName("lineEdit_2")
		self.verticalLayout_15.addWidget(self.lineEdit_2)
		self.lineEdit = QtWidgets.QLineEdit(self.username_password)
		self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
		self.lineEdit.setObjectName("lineEdit")
		self.verticalLayout_15.addWidget(self.lineEdit)
		spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.verticalLayout_15.addItem(spacerItem4)
		self.stackedWidget.addWidget(self.username_password)
		self.verticalLayout_5.addWidget(self.stackedWidget)
		self.progressBar_2 = QtWidgets.QProgressBar(self.authorise_fedibooks)
		self.progressBar_2.setProperty("value", 24)
		self.progressBar_2.setObjectName("progressBar_2")
		self.verticalLayout_5.addWidget(self.progressBar_2)
		spacerItem5 = QtWidgets.QSpacerItem(20, 61, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.verticalLayout_5.addItem(spacerItem5)
		self.stkMain.addWidget(self.authorise_fedibooks)
		self.select_sources = QtWidgets.QWidget()
		self.select_sources.setObjectName("select_sources")
		self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.select_sources)
		self.verticalLayout_10.setObjectName("verticalLayout_10")
		self.label_17 = QtWidgets.QLabel(self.select_sources)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
		self.label_17.setSizePolicy(sizePolicy)
		font = QtGui.QFont()
		font.setPointSize(24)
		self.label_17.setFont(font)
		self.label_17.setTextFormat(QtCore.Qt.AutoText)
		self.label_17.setScaledContents(True)
		self.label_17.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
		self.label_17.setObjectName("label_17")
		self.verticalLayout_10.addWidget(self.label_17)
		self.label_18 = QtWidgets.QLabel(self.select_sources)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
		self.label_18.setSizePolicy(sizePolicy)
		self.label_18.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
		self.label_18.setWordWrap(True)
		self.label_18.setObjectName("label_18")
		self.verticalLayout_10.addWidget(self.label_18)
		self.tbl_sources = QtWidgets.QTableWidget(self.select_sources)
		self.tbl_sources.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
		self.tbl_sources.setObjectName("tbl_sources")
		self.tbl_sources.setColumnCount(2)
		self.tbl_sources.setRowCount(0)
		item = QtWidgets.QTableWidgetItem()
		self.tbl_sources.setHorizontalHeaderItem(0, item)
		item = QtWidgets.QTableWidgetItem()
		self.tbl_sources.setHorizontalHeaderItem(1, item)
		self.verticalLayout_10.addWidget(self.tbl_sources)
		self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_5.setObjectName("horizontalLayout_5")
		self.btn_source_delete = QtWidgets.QPushButton(self.select_sources)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap("."), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.btn_source_delete.setIcon(icon)
		self.btn_source_delete.setObjectName("btn_source_delete")
		self.horizontalLayout_5.addWidget(self.btn_source_delete)
		self.btn_add_fedi = QtWidgets.QPushButton(self.select_sources)
		self.btn_add_fedi.setIcon(icon)
		self.btn_add_fedi.setObjectName("btn_add_fedi")
		self.horizontalLayout_5.addWidget(self.btn_add_fedi)
		self.btn_add_text = QtWidgets.QPushButton(self.select_sources)
		self.btn_add_text.setIcon(icon)
		self.btn_add_text.setObjectName("btn_add_text")
		self.horizontalLayout_5.addWidget(self.btn_add_text)
		self.verticalLayout_10.addLayout(self.horizontalLayout_5)
		spacerItem6 = QtWidgets.QSpacerItem(20, 8, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.verticalLayout_10.addItem(spacerItem6)
		self.stkMain.addWidget(self.select_sources)
		self.configure_your_bot = QtWidgets.QWidget()
		self.configure_your_bot.setObjectName("configure_your_bot")
		self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.configure_your_bot)
		self.verticalLayout_11.setObjectName("verticalLayout_11")
		self.label_19 = QtWidgets.QLabel(self.configure_your_bot)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
		self.label_19.setSizePolicy(sizePolicy)
		font = QtGui.QFont()
		font.setPointSize(24)
		self.label_19.setFont(font)
		self.label_19.setTextFormat(QtCore.Qt.AutoText)
		self.label_19.setScaledContents(True)
		self.label_19.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
		self.label_19.setObjectName("label_19")
		self.verticalLayout_11.addWidget(self.label_19)
		self.label_20 = QtWidgets.QLabel(self.configure_your_bot)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
		self.label_20.setSizePolicy(sizePolicy)
		self.label_20.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
		self.label_20.setWordWrap(True)
		self.label_20.setObjectName("label_20")
		self.verticalLayout_11.addWidget(self.label_20)
		self.gridLayout_2 = QtWidgets.QGridLayout()
		self.gridLayout_2.setContentsMargins(-1, -1, -1, 0)
		self.gridLayout_2.setHorizontalSpacing(0)
		self.gridLayout_2.setObjectName("gridLayout_2")
		self.label_10 = QtWidgets.QLabel(self.configure_your_bot)
		self.label_10.setObjectName("label_10")
		self.gridLayout_2.addWidget(self.label_10, 0, 0, 1, 1)
		self.label_16 = QtWidgets.QLabel(self.configure_your_bot)
		self.label_16.setObjectName("label_16")
		self.gridLayout_2.addWidget(self.label_16, 1, 0, 1, 1)
		self.btn_learn_from_cw_posts = QtWidgets.QPushButton(self.configure_your_bot)
		self.btn_learn_from_cw_posts.setMinimumSize(QtCore.QSize(200, 0))
		self.btn_learn_from_cw_posts.setBaseSize(QtCore.QSize(0, 0))
		self.btn_learn_from_cw_posts.setObjectName("btn_learn_from_cw_posts")
		self.gridLayout_2.addWidget(self.btn_learn_from_cw_posts, 0, 2, 1, 1)
		spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.gridLayout_2.addItem(spacerItem7, 0, 1, 1, 1)
		self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")
		self.spn_post_check_frequency = QtWidgets.QSpinBox(self.configure_your_bot)
		self.spn_post_check_frequency.setMinimum(5)
		self.spn_post_check_frequency.setMaximum(360)
		self.spn_post_check_frequency.setSingleStep(5)
		self.spn_post_check_frequency.setProperty("value", 60)
		self.spn_post_check_frequency.setObjectName("spn_post_check_frequency")
		self.horizontalLayout_2.addWidget(self.spn_post_check_frequency)
		self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 2, 1, 1)
		self.verticalLayout_11.addLayout(self.gridLayout_2)
		self.gridLayout = QtWidgets.QGridLayout()
		self.gridLayout.setHorizontalSpacing(0)
		self.gridLayout.setObjectName("gridLayout")
		self.btn_enable_reply_service = QtWidgets.QPushButton(self.configure_your_bot)
		self.btn_enable_reply_service.setCheckable(True)
		self.btn_enable_reply_service.setChecked(True)
		self.btn_enable_reply_service.setObjectName("btn_enable_reply_service")
		self.gridLayout.addWidget(self.btn_enable_reply_service, 1, 2, 1, 1)
		self.label_23 = QtWidgets.QLabel(self.configure_your_bot)
		self.label_23.setObjectName("label_23")
		self.gridLayout.addWidget(self.label_23, 1, 0, 1, 1)
		spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.gridLayout.addItem(spacerItem8, 1, 1, 1, 1)
		self.label_11 = QtWidgets.QLabel(self.configure_your_bot)
		self.label_11.setObjectName("label_11")
		self.gridLayout.addWidget(self.label_11, 2, 0, 1, 1)
		self.txt_cw = QtWidgets.QLineEdit(self.configure_your_bot)
		self.txt_cw.setObjectName("txt_cw")
		self.gridLayout.addWidget(self.txt_cw, 2, 2, 1, 1)
		self.label_21 = QtWidgets.QLabel(self.configure_your_bot)
		self.label_21.setObjectName("label_21")
		self.gridLayout.addWidget(self.label_21, 0, 0, 1, 1)
		self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_3.setObjectName("horizontalLayout_3")
		self.btn_post_frequency = QtWidgets.QSpinBox(self.configure_your_bot)
		self.btn_post_frequency.setMinimum(5)
		self.btn_post_frequency.setMaximum(360)
		self.btn_post_frequency.setSingleStep(5)
		self.btn_post_frequency.setProperty("value", 30)
		self.btn_post_frequency.setObjectName("btn_post_frequency")
		self.horizontalLayout_3.addWidget(self.btn_post_frequency)
		self.gridLayout.addLayout(self.horizontalLayout_3, 0, 2, 1, 1)
		self.verticalLayout_11.addLayout(self.gridLayout)
		spacerItem9 = QtWidgets.QSpacerItem(20, 51, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.verticalLayout_11.addItem(spacerItem9)
		self.stkMain.addWidget(self.configure_your_bot)
		self.attribution_important = QtWidgets.QWidget()
		self.attribution_important.setObjectName("attribution_important")
		self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.attribution_important)
		self.verticalLayout_7.setObjectName("verticalLayout_7")
		self.label_15 = QtWidgets.QLabel(self.attribution_important)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
		self.label_15.setSizePolicy(sizePolicy)
		font = QtGui.QFont()
		font.setPointSize(24)
		self.label_15.setFont(font)
		self.label_15.setTextFormat(QtCore.Qt.AutoText)
		self.label_15.setScaledContents(True)
		self.label_15.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
		self.label_15.setObjectName("label_15")
		self.verticalLayout_7.addWidget(self.label_15)
		self.label_14 = QtWidgets.QLabel(self.attribution_important)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
		self.label_14.setSizePolicy(sizePolicy)
		self.label_14.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
		self.label_14.setWordWrap(True)
		self.label_14.setObjectName("label_14")
		self.verticalLayout_7.addWidget(self.label_14)
		self.lineEdit_4 = QtWidgets.QLineEdit(self.attribution_important)
		self.lineEdit_4.setReadOnly(True)
		self.lineEdit_4.setObjectName("lineEdit_4")
		self.verticalLayout_7.addWidget(self.lineEdit_4)
		self.btn_view_license = QtWidgets.QPushButton(self.attribution_important)
		self.btn_view_license.setObjectName("btn_view_license")
		self.verticalLayout_7.addWidget(self.btn_view_license)
		spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.verticalLayout_7.addItem(spacerItem10)
		self.stkMain.addWidget(self.attribution_important)
		self.done = QtWidgets.QWidget()
		self.done.setObjectName("done")
		self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.done)
		self.verticalLayout_6.setObjectName("verticalLayout_6")
		self.label_13 = QtWidgets.QLabel(self.done)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
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
		self.verticalLayout_6.addWidget(self.label_13)
		self.label_12 = QtWidgets.QLabel(self.done)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
		self.label_12.setSizePolicy(sizePolicy)
		self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
		self.label_12.setWordWrap(True)
		self.label_12.setObjectName("label_12")
		self.verticalLayout_6.addWidget(self.label_12)
		self.stkMain.addWidget(self.done)
		self.verticalLayout.addWidget(self.stkMain)
		self.verticalLayout_13.addLayout(self.verticalLayout)
		self.hbx_button_box = QtWidgets.QHBoxLayout()
		self.hbx_button_box.setObjectName("hbx_button_box")
		self.btn_cancel = QtWidgets.QPushButton(self.centralwidget)
		self.btn_cancel.setIcon(icon)
		self.btn_cancel.setObjectName("btn_cancel")
		self.hbx_button_box.addWidget(self.btn_cancel)
		self.btn_help = QtWidgets.QPushButton(self.centralwidget)
		self.btn_help.setIcon(icon)
		self.btn_help.setObjectName("btn_help")
		self.hbx_button_box.addWidget(self.btn_help)
		spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.hbx_button_box.addItem(spacerItem11)
		self.btn_back = QtWidgets.QPushButton(self.centralwidget)
		self.btn_back.setIcon(icon)
		self.btn_back.setObjectName("btn_back")
		self.hbx_button_box.addWidget(self.btn_back)
		self.btn_next = QtWidgets.QPushButton(self.centralwidget)
		self.btn_next.setIcon(icon)
		self.btn_next.setAutoDefault(True)
		self.btn_next.setDefault(True)
		self.btn_next.setObjectName("btn_next")
		self.hbx_button_box.addWidget(self.btn_next)
		self.verticalLayout_13.addLayout(self.hbx_button_box)
		wzdCreateBot.setCentralWidget(self.centralwidget)

		self.retranslateUi(wzdCreateBot)
		self.stkMain.setCurrentIndex(4)
		self.stkCreateAccount.setCurrentIndex(0)
		self.stackedWidget.setCurrentIndex(0)
		QtCore.QMetaObject.connectSlotsByName(wzdCreateBot)

	def retranslateUi(self, wzdCreateBot):
		wzdCreateBot.setWindowTitle(QtWidgets.QApplication.translate("wzdCreateBot", "Bot Creation Wizard", None, -1))
		self.label.setText(QtWidgets.QApplication.translate("wzdCreateBot", "Welcome", None, -1))
		self.label_2.setText(QtWidgets.QApplication.translate("wzdCreateBot", "<html><head/><body><p>This wizard will guide you through the process of creating your own ebooks bot. You will be asked to select an instance, a username, and a list of users to learn from.</p><p>Click <span style=\" font-weight:600;\">Next</span> to continue.</p></body></html>", None, -1))
		self.pushButton_12.setText(QtWidgets.QApplication.translate("wzdCreateBot", "Import existing bot from mstdn-ebooks", None, -1))
		self.label_3.setText(QtWidgets.QApplication.translate("wzdCreateBot", "Choose an Instance", None, -1))
		self.label_4.setText(QtWidgets.QApplication.translate("wzdCreateBot", "<html><head/><body><p>Please specify the instance you\'d like your bot to run on. It doesn\'t have to be the same instance that your account is on. <span style=\" font-weight:600;\">botsin.space</span> is an instance designed with the intention of hosting bots.</p><p>When you\'ve chosen an instance, click <span style=\" font-weight:600;\">Next</span> to continue.</p></body></html>", None, -1))
		self.txt_instance.setText(QtWidgets.QApplication.translate("wzdCreateBot", "botsin.space", None, -1))
		self.label_5.setText(QtWidgets.QApplication.translate("wzdCreateBot", "Create an Account", None, -1))
		self.label_6.setText(QtWidgets.QApplication.translate("wzdCreateBot", "<html><head/><body><p>If you <span style=\" font-weight:600;\">don\'t have an account for your bot yet</span>, ou now need to create an account on <span style=\" font-weight:600;\">botsin.space</span> for your bot to use. Click the button below to open the account creation page. Once you\'ve successfully created the account <span style=\" font-weight:600;\">and confirmed the email </span>(if necessary), click <span style=\" font-weight:600;\">Next</span> to proceed. If you are currently signed in to an account on this instance, you will either need to <span style=\" font-weight:600;\">log out</span> or <span style=\" font-weight:600;\">sign up in a different browser or a private window</span>.</p><p>If you <span style=\" font-weight:600;\">already have an account you\'d like to use for the bot</span>, click <span style=\" font-weight:600;\">Next</span>.</p></body></html>", None, -1))
		self.btn_create_account.setText(QtWidgets.QApplication.translate("wzdCreateBot", "Open account creation page", None, -1))
		self.label_9.setText(QtWidgets.QApplication.translate("wzdCreateBot", "Unsupported Instance Type", None, -1))
		self.label_22.setText(QtWidgets.QApplication.translate("wzdCreateBot", "<html><head/><body><p>Unfortunately, FediBooks does not yet support posting to accounts hosted on [instance name] instances. While <span style=\" font-weight:600;\">posting from these instances is unsupported</span>, it is hightly likely that <span style=\" font-weight:600;\">you will still be able to learn from posts on instances of this type</span>.</p><p>Click <span style=\" font-weight:600;\">Back</span> to choose a new instance for FediBooks to use.</p></body></html>", None, -1))
		self.label_24.setText(QtWidgets.QApplication.translate("wzdCreateBot", "Registering App", None, -1))
		self.label_25.setText(QtWidgets.QApplication.translate("wzdCreateBot", "<html><head/><body><p>Please wait while your copy of FediBooks registers itself with [instance name]. This is a necessary step of authentication and <span style=\" font-weight:600;\">no action is required</span>.</p></body></html>", None, -1))
		self.pbr_registering_app.setFormat(QtWidgets.QApplication.translate("wzdCreateBot", "test", None, -1))
		self.label_7.setText(QtWidgets.QApplication.translate("wzdCreateBot", "Authorise FediBooks", None, -1))
		self.label_8.setText(QtWidgets.QApplication.translate("wzdCreateBot", "<html><head/><body><p>FediBooks needs access to the account you\'d like to use for your bot. Click the button below to open the authorisation prompt, and allow access to the account. If you accidentally reject access, click the button again.<br/></p><p>When you\'ve authorised access to the account, you will be given a code. Copy that code and paste it in the box below the button, then click <span style=\" font-weight:600;\">Next</span> to continue.</p></body></html>", None, -1))
		self.btn_auth_code.setText(QtWidgets.QApplication.translate("wzdCreateBot", "Request access", None, -1))
		self.txt_auth_code.setPlaceholderText(QtWidgets.QApplication.translate("wzdCreateBot", "Authorisation code", None, -1))
		self.label_26.setText(QtWidgets.QApplication.translate("wzdCreateBot", "<html><head/><body><p>FediBooks needs access to the account you\'d like to use for your bot. Enter your username and password below, then click <span style=\" font-weight:600;\">Next</span> to continue.</p></body></html>", None, -1))
		self.lineEdit_2.setPlaceholderText(QtWidgets.QApplication.translate("wzdCreateBot", "Username", None, -1))
		self.lineEdit.setPlaceholderText(QtWidgets.QApplication.translate("wzdCreateBot", "Password", None, -1))
		self.progressBar_2.setFormat(QtWidgets.QApplication.translate("wzdCreateBot", "Validating", None, -1))
		self.label_17.setText(QtWidgets.QApplication.translate("wzdCreateBot", "Select Sources", None, -1))
		self.label_18.setText(QtWidgets.QApplication.translate("wzdCreateBot", "<html><head/><body><p>FediBooks needs at least one source to model its posts from. These can either be fediverse accounts or text files (seperated by linebreaks).</p><p>Add at least one source, then click <span style=\" font-weight:600;\">Next</span>.</p></body></html>", None, -1))
		self.tbl_sources.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("wzdCreateBot", "Type", None, -1))
		self.tbl_sources.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("wzdCreateBot", "Name", None, -1))
		self.btn_source_delete.setText(QtWidgets.QApplication.translate("wzdCreateBot", "Delete", None, -1))
		self.btn_add_fedi.setText(QtWidgets.QApplication.translate("wzdCreateBot", "Add fediverse account", None, -1))
		self.btn_add_text.setText(QtWidgets.QApplication.translate("wzdCreateBot", "Add text file", None, -1))
		self.label_19.setText(QtWidgets.QApplication.translate("wzdCreateBot", "Configure your Bot", None, -1))
		self.label_20.setText(QtWidgets.QApplication.translate("wzdCreateBot", "<html><head/><body><p>You may set up the options for how your bot should work here, such as how often it should post, whether it should reply, etc. You can also leave them as they are for now and configure them later. Advanced options, like custom reply rules, can be configured later.</p><p>Click <span style=\" font-weight:600;\">Next</span> to continue when ready.</p></body></html>", None, -1))
		self.label_10.setText(QtWidgets.QApplication.translate("wzdCreateBot", "Learn from CW\'d posts", None, -1))
		self.label_16.setText(QtWidgets.QApplication.translate("wzdCreateBot", "Check for new posts every", None, -1))
		self.btn_learn_from_cw_posts.setText(QtWidgets.QApplication.translate("wzdCreateBot", "Enable", None, -1))
		self.spn_post_check_frequency.setSuffix(QtWidgets.QApplication.translate("wzdCreateBot", " mins", None, -1))
		self.btn_enable_reply_service.setText(QtWidgets.QApplication.translate("wzdCreateBot", "Enable", None, -1))
		self.label_23.setText(QtWidgets.QApplication.translate("wzdCreateBot", "Reply service", None, -1))
		self.label_11.setText(QtWidgets.QApplication.translate("wzdCreateBot", "CW for created posts", None, -1))
		self.txt_cw.setPlaceholderText(QtWidgets.QApplication.translate("wzdCreateBot", "Leave blank for none", None, -1))
		self.label_21.setText(QtWidgets.QApplication.translate("wzdCreateBot", "Create a new post every", None, -1))
		self.btn_post_frequency.setSuffix(QtWidgets.QApplication.translate("wzdCreateBot", " mins", None, -1))
		self.label_15.setText(QtWidgets.QApplication.translate("wzdCreateBot", "Attribution (Important)", None, -1))
		self.label_14.setText(QtWidgets.QApplication.translate("wzdCreateBot", "<html><head/><body><p>This software is licensed under the <span style=\" font-weight:600;\">GNU Affero General Public License (version 3)</span>, meaning that you must provide attribution.</p><p>Please <span style=\" font-weight:600;\">copy the link below and make it available somewhere from your bot\'s user page</span>, such as in the bio, on a pinned post, or similar, and <span style=\" font-weight:600;\">make it clear that this is a link to the source code of the bot</span>.</p><p>Once you have added the text in the box below somewhere to your bot\'s page, along with an explanation of what the link is for, click <span style=\" font-weight:600;\">Next</span> to continue. This step is not optional.</p><p>A button to view the full text of the license is provided below for convenience.</p></body></html>", None, -1))
		self.lineEdit_4.setText(QtWidgets.QApplication.translate("wzdCreateBot", "https://github.com/Lynnesbian/FediBooks", None, -1))
		self.btn_view_license.setText(QtWidgets.QApplication.translate("wzdCreateBot", "View the full text of the license", None, -1))
		self.label_13.setText(QtWidgets.QApplication.translate("wzdCreateBot", "Done!", None, -1))
		self.label_12.setText(QtWidgets.QApplication.translate("wzdCreateBot", "<html><head/><body><p>Your bot has been set up and configured, and is ready to learn from the sources provided. </p><p>Click <span style=\" font-weight:600;\">Finish</span> to complete the setup process. Your bot will start learning from the provided sources.</p></body></html>", None, -1))
		self.btn_cancel.setText(QtWidgets.QApplication.translate("wzdCreateBot", "&Cancel", None, -1))
		self.btn_help.setText(QtWidgets.QApplication.translate("wzdCreateBot", "&Help", None, -1))
		self.btn_back.setText(QtWidgets.QApplication.translate("wzdCreateBot", "&Back", None, -1))
		self.btn_next.setText(QtWidgets.QApplication.translate("wzdCreateBot", "&Next", None, -1))

