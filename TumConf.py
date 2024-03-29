# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TumConf.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TUMCONF(object):
    def setupUi(self, TUMCONF):
        TUMCONF.setObjectName("TUMCONF")
        TUMCONF.resize(430, 759)
        self.centralwidget = QtWidgets.QWidget(TUMCONF)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnCheckDevice = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCheckDevice.sizePolicy().hasHeightForWidth())
        self.btnCheckDevice.setSizePolicy(sizePolicy)
        self.btnCheckDevice.setObjectName("btnCheckDevice")
        self.horizontalLayout.addWidget(self.btnCheckDevice)
        self.lblDeviceID = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblDeviceID.sizePolicy().hasHeightForWidth())
        self.lblDeviceID.setSizePolicy(sizePolicy)
        self.lblDeviceID.setObjectName("lblDeviceID")
        self.horizontalLayout.addWidget(self.lblDeviceID)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.tabMain = QtWidgets.QTabWidget(self.centralwidget)
        self.tabMain.setObjectName("tabMain")
        self.tabNetwork = QtWidgets.QWidget()
        self.tabNetwork.setObjectName("tabNetwork")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tabNetwork)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnNetLoadConf = QtWidgets.QPushButton(self.tabNetwork)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnNetLoadConf.sizePolicy().hasHeightForWidth())
        self.btnNetLoadConf.setSizePolicy(sizePolicy)
        self.btnNetLoadConf.setObjectName("btnNetLoadConf")
        self.horizontalLayout_2.addWidget(self.btnNetLoadConf)
        self.txtConfPath = QtWidgets.QLineEdit(self.tabNetwork)
        self.txtConfPath.setObjectName("txtConfPath")
        self.horizontalLayout_2.addWidget(self.txtConfPath)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tabNetConf = QtWidgets.QTabWidget(self.tabNetwork)
        self.tabNetConf.setObjectName("tabNetConf")
        self.tabWired = QtWidgets.QWidget()
        self.tabWired.setObjectName("tabWired")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tabWired)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.rbtnIsWiredDHCP = QtWidgets.QRadioButton(self.tabWired)
        self.rbtnIsWiredDHCP.setIconSize(QtCore.QSize(30, 30))
        self.rbtnIsWiredDHCP.setChecked(True)
        self.rbtnIsWiredDHCP.setObjectName("rbtnIsWiredDHCP")
        self.verticalLayout_3.addWidget(self.rbtnIsWiredDHCP)
        self.line_3 = QtWidgets.QFrame(self.tabWired)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_3.addWidget(self.line_3)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_2 = QtWidgets.QLabel(self.tabWired)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.txtWiredIP = QtWidgets.QLineEdit(self.tabWired)
        self.txtWiredIP.setEnabled(True)
        self.txtWiredIP.setObjectName("txtWiredIP")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtWiredIP)
        self.label_3 = QtWidgets.QLabel(self.tabWired)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.txtWiredMask = QtWidgets.QLineEdit(self.tabWired)
        self.txtWiredMask.setObjectName("txtWiredMask")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtWiredMask)
        self.label_4 = QtWidgets.QLabel(self.tabWired)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.txtWiredGateway = QtWidgets.QLineEdit(self.tabWired)
        self.txtWiredGateway.setObjectName("txtWiredGateway")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txtWiredGateway)
        self.label_5 = QtWidgets.QLabel(self.tabWired)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.txtWiredDNS = QtWidgets.QLineEdit(self.tabWired)
        self.txtWiredDNS.setObjectName("txtWiredDNS")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txtWiredDNS)
        self.verticalLayout_3.addLayout(self.formLayout_2)
        self.tabNetConf.addTab(self.tabWired, "")
        self.tabWifi = QtWidgets.QWidget()
        self.tabWifi.setObjectName("tabWifi")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tabWifi)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_4.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_10 = QtWidgets.QLabel(self.tabWifi)
        self.label_10.setObjectName("label_10")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.label_11 = QtWidgets.QLabel(self.tabWifi)
        self.label_11.setObjectName("label_11")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.txtWifiSSID = QtWidgets.QLineEdit(self.tabWifi)
        self.txtWifiSSID.setObjectName("txtWifiSSID")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtWifiSSID)
        self.txtWifiPassword = QtWidgets.QLineEdit(self.tabWifi)
        self.txtWifiPassword.setObjectName("txtWifiPassword")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtWifiPassword)
        self.verticalLayout_4.addLayout(self.formLayout_4)
        self.line = QtWidgets.QFrame(self.tabWifi)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)
        self.rbtnIsWifiDHCP = QtWidgets.QRadioButton(self.tabWifi)
        self.rbtnIsWifiDHCP.setIconSize(QtCore.QSize(30, 30))
        self.rbtnIsWifiDHCP.setChecked(True)
        self.rbtnIsWifiDHCP.setObjectName("rbtnIsWifiDHCP")
        self.verticalLayout_4.addWidget(self.rbtnIsWifiDHCP)
        self.line_4 = QtWidgets.QFrame(self.tabWifi)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_4.addWidget(self.line_4)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_3.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_6 = QtWidgets.QLabel(self.tabWifi)
        self.label_6.setObjectName("label_6")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(self.tabWifi)
        self.label_7.setObjectName("label_7")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtWidgets.QLabel(self.tabWifi)
        self.label_8.setObjectName("label_8")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.label_9 = QtWidgets.QLabel(self.tabWifi)
        self.label_9.setObjectName("label_9")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.txtWifiIP = QtWidgets.QLineEdit(self.tabWifi)
        self.txtWifiIP.setObjectName("txtWifiIP")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtWifiIP)
        self.txtWifiMask = QtWidgets.QLineEdit(self.tabWifi)
        self.txtWifiMask.setObjectName("txtWifiMask")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtWifiMask)
        self.txtWifiGateway = QtWidgets.QLineEdit(self.tabWifi)
        self.txtWifiGateway.setObjectName("txtWifiGateway")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txtWifiGateway)
        self.txtWifiDNS = QtWidgets.QLineEdit(self.tabWifi)
        self.txtWifiDNS.setObjectName("txtWifiDNS")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txtWifiDNS)
        self.verticalLayout_4.addLayout(self.formLayout_3)
        self.tabNetConf.addTab(self.tabWifi, "")
        self.tabMobile = QtWidgets.QWidget()
        self.tabMobile.setObjectName("tabMobile")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tabMobile)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_12 = QtWidgets.QLabel(self.tabMobile)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_5.addWidget(self.label_12)
        self.line_2 = QtWidgets.QFrame(self.tabMobile)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_5.addWidget(self.line_2)
        self.rbtnCMNET = QtWidgets.QRadioButton(self.tabMobile)
        self.rbtnCMNET.setObjectName("rbtnCMNET")
        self.verticalLayout_5.addWidget(self.rbtnCMNET)
        self.rbtnCMCC = QtWidgets.QRadioButton(self.tabMobile)
        self.rbtnCMCC.setObjectName("rbtnCMCC")
        self.verticalLayout_5.addWidget(self.rbtnCMCC)
        self.rbtnUNICOM = QtWidgets.QRadioButton(self.tabMobile)
        self.rbtnUNICOM.setChecked(True)
        self.rbtnUNICOM.setObjectName("rbtnUNICOM")
        self.verticalLayout_5.addWidget(self.rbtnUNICOM)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.tabNetConf.addTab(self.tabMobile, "")
        self.verticalLayout.addWidget(self.tabNetConf)
        self.btnNetDownloadConf = QtWidgets.QPushButton(self.tabNetwork)
        self.btnNetDownloadConf.setObjectName("btnNetDownloadConf")
        self.verticalLayout.addWidget(self.btnNetDownloadConf)
        self.txtLog = QtWidgets.QPlainTextEdit(self.tabNetwork)
        self.txtLog.setReadOnly(True)
        self.txtLog.setObjectName("txtLog")
        self.verticalLayout.addWidget(self.txtLog)
        self.btnReboot = QtWidgets.QPushButton(self.tabNetwork)
        self.btnReboot.setObjectName("btnReboot")
        self.verticalLayout.addWidget(self.btnReboot)
        self.tabMain.addTab(self.tabNetwork, "")
        self.tabOther = QtWidgets.QWidget()
        self.tabOther.setObjectName("tabOther")
        self.tabMain.addTab(self.tabOther, "")
        self.verticalLayout_2.addWidget(self.tabMain)
        TUMCONF.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(TUMCONF)
        self.statusbar.setObjectName("statusbar")
        TUMCONF.setStatusBar(self.statusbar)
        self.actionTool = QtWidgets.QAction(TUMCONF)
        self.actionTool.setObjectName("actionTool")

        self.retranslateUi(TUMCONF)
        self.tabMain.setCurrentIndex(0)
        self.tabNetConf.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TUMCONF)

    def retranslateUi(self, TUMCONF):
        _translate = QtCore.QCoreApplication.translate
        TUMCONF.setWindowTitle(_translate("TUMCONF", "传输单元配置工具"))
        self.btnCheckDevice.setText(_translate("TUMCONF", "检查设备"))
        self.lblDeviceID.setText(_translate("TUMCONF", "None"))
        self.btnNetLoadConf.setText(_translate("TUMCONF", "从设备加载配置"))
        self.txtConfPath.setText(_translate("TUMCONF", "/usr/bin/conf/parser.json"))
        self.rbtnIsWiredDHCP.setText(_translate("TUMCONF", "动态IP(DHCP)"))
        self.label_2.setText(_translate("TUMCONF", "IP地址"))
        self.label_3.setText(_translate("TUMCONF", "子网掩码"))
        self.label_4.setText(_translate("TUMCONF", "默认网关"))
        self.label_5.setText(_translate("TUMCONF", "DNS"))
        self.tabNetConf.setTabText(self.tabNetConf.indexOf(self.tabWired), _translate("TUMCONF", "有线"))
        self.label_10.setText(_translate("TUMCONF", "SSID"))
        self.label_11.setText(_translate("TUMCONF", "密码"))
        self.rbtnIsWifiDHCP.setText(_translate("TUMCONF", "动态IP(DHCP)"))
        self.label_6.setText(_translate("TUMCONF", "IP地址"))
        self.label_7.setText(_translate("TUMCONF", "子网掩码"))
        self.label_8.setText(_translate("TUMCONF", "默认网关"))
        self.label_9.setText(_translate("TUMCONF", "DNS"))
        self.tabNetConf.setTabText(self.tabNetConf.indexOf(self.tabWifi), _translate("TUMCONF", "Wi-Fi"))
        self.label_12.setText(_translate("TUMCONF", "网络类型"))
        self.rbtnCMNET.setText(_translate("TUMCONF", "电信"))
        self.rbtnCMCC.setText(_translate("TUMCONF", "移动"))
        self.rbtnUNICOM.setText(_translate("TUMCONF", "联通"))
        self.tabNetConf.setTabText(self.tabNetConf.indexOf(self.tabMobile), _translate("TUMCONF", "移动网络"))
        self.btnNetDownloadConf.setText(_translate("TUMCONF", "下发配置至设备"))
        self.btnReboot.setText(_translate("TUMCONF", "重启设备"))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tabNetwork), _translate("TUMCONF", "网络功能"))
        self.tabMain.setTabText(self.tabMain.indexOf(self.tabOther), _translate("TUMCONF", "其他"))
        self.actionTool.setText(_translate("TUMCONF", "Tool"))


