# -*- coding: utf-8 -*-
#!/usr/local/bin/python
from PyQt5 import QtGui, QtWidgets
import sys
import TumConf
from networkConf import *

version = "version: 20190614001"

class ExampleApp(QtWidgets.QMainWindow, TumConf.Ui_TUMCONF):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        self.statusBar().showMessage(version)
        self.registEvent()
        self.initStates()
        self.netConf = NetworkConf()

    def initStates(self):
        self.switchEditable("wired", False)
        self.switchEditable("wifi", False)
        self.switchConfButtons(False)

    def registEvent(self):
        self.btnCheckDevice.clicked.connect(self.checkDevice)
        self.btnNetDownloadConf.clicked.connect(self.netDownloadConf)
        self.btnNetLoadConf.clicked.connect(self.netLoadConf)
        self.btnReboot.clicked.connect(self.rebootDevice)
        self.rbtnIsWiredDHCP.toggled.connect(self.switchWiredDHCP)
        self.rbtnIsWifiDHCP.clicked.connect(self.switchWifiDHCP)
        self.rbtnCMCC.clicked.connect(self.switchMobileType)
        self.rbtnCMNET.clicked.connect(self.switchMobileType)
        self.rbtnUNICOM.clicked.connect(self.switchMobileType)
        self.tabNetConf.currentChanged.connect(self.tabIndexChanged)

    def tabIndexChanged(self):
        index = self.tabNetConf.currentIndex()
        self.netConf.netType = dirNetType[index]

    def printLog(self, msg):
        timeStr = time.strftime("[%Y-%m-%d %H:%M:%S] ", time.localtime())
        self.txtLog.appendPlainText(timeStr + msg)

    def netLoadConf(self):
        filePath = self.txtConfPath.text()
        if filePath != "":
            cmdStr = "pull " + filePath
            cmdOut = processCMD(cmdStr)
            for line in cmdOut:
                self.printLog(line.decode("utf-8"))
            
            #TODO: check pull ok or not
            fileName = filePath.split("/")[-1]
            self.netConf.fileName = fileName
        else:
            self.printLog("未指定配置文件路径")
        self.restoreConf()

    def restoreConf(self):
        fullJson = loadJsonFile(self.netConf.fileName)
        subNetDir = fullJson["network"]
        if subNetDir["type"] == "wired":
            self.tabNetConf.setCurrentIndex(0)
            if subNetDir["access"] == "dynamic":
                self.rbtnIsWiredDHCP.setChecked(True)
                self.switchEditable("wired", False)
            else:
                self.rbtnIsWiredDHCP.setChecked(False)
                self.switchEditable("wired", True)
                self.txtWiredIP.setText(subNetDir["static"]["inet"])
                self.txtWiredMask.setText(subNetDir["static"]["netmask"])
                self.txtWiredGateway.setText(subNetDir["static"]["gateway"])
                self.txtWiredDNS.setText(subNetDir["static"]["dns"])
        elif subNetDir["type"] == "wifi":
            self.tabNetConf.setCurrentIndex(1)
            self.txtWifiSSID.setText(subNetDir["wifi"]["ssid"])
            self.txtWifiPassword.setText(subNetDir["wifi"]["password"])
            if subNetDir["access"] == "dynamic":
                self.rbtnIsWifiDHCP.setChecked(True)
                self.switchEditable("wifi", False)
            else:
                self.rbtnIsWifiDHCP.setChecked(False)
                self.switchEditable("wifi", True)
                self.txtWifiIP.setText(subNetDir["static"]["inet"])
                self.txtWifiMask.setText(subNetDir["static"]["netmask"])
                self.txtWifiGateway.setText(subNetDir["static"]["gateway"])
                self.txtWifiDNS.setText(subNetDir["static"]["dns"])
        else:
            self.tabNetConf.setCurrentIndex(2)
            if subNetDir["mobile"] == dirMobileType["unicom"]:
                self.rbtnCMNET.setChecked(False)
                self.rbtnCMCC.setChecked(False)
                self.rbtnUNICOM.setChecked(True)
            elif subNetDir["mobile"] == dirMobileType["mobile"]:
                self.rbtnCMNET.setChecked(False)
                self.rbtnCMCC.setChecked(True)
                self.rbtnUNICOM.setChecked(False)
            else:
                self.rbtnCMNET.setChecked(True)
                self.rbtnCMCC.setChecked(False)
                self.rbtnUNICOM.setChecked(False)
    def rebootDevice(self):
        cmdStr = "reboot"
        _ = processCMD(cmdStr)
        self.printLog("====== reboot device =======")

    def netDownloadConf(self):
        if self.netConf.netType == "wired":
            if not self.netConf.isDHCP:
                self.netConf.mask = self.txtWiredMask.text()
                self.netConf.ipAddress = self.txtWiredIP.text()
                self.netConf.gateway = self.txtWiredGateway.text()
                self.netConf.dns = self.txtWiredDNS.text()
        elif self.netConf.netType == "wifi":
            self.netConf.wifiSSID = self.txtWifiSSID.text()
            self.netConf.wifiPasswd = self.txtWifiPassword.text()
            if not self.netConf.isDHCP:
                self.netConf.mask = self.txtWifiMask.text()
                self.netConf.ipAddress = self.txtWifiIP.text()
                self.netConf.gateway = self.txtWifiGateway.text()
                self.netConf.dns = self.txtWifiDNS.text()
        else:
            self.switchMobileType()
        self.netConf.downloadNetConf()
        cmdStr = "push " + self.netConf.fileName + " " + self.txtConfPath.text()
        cmdOut = processCMD(cmdStr)
        for line in cmdOut:
            self.printLog(line.decode("utf-8"))

    def switchEditable(self, netType, TF):
        if netType == "wired":
            self.txtWiredMask.setEnabled(TF)
            self.txtWiredIP.setEnabled(TF)
            self.txtWiredGateway.setEnabled(TF)
            self.txtWiredDNS.setEnabled(TF)
        else :
            self.txtWifiMask.setEnabled(TF)
            self.txtWifiIP.setEnabled(TF)
            self.txtWifiGateway.setEnabled(TF)
            self.txtWifiDNS.setEnabled(TF)
    def switchConfButtons(self, TF):
        self.btnNetDownloadConf.setEnabled(TF)
        self.btnNetLoadConf.setEnabled(TF)
        self.btnReboot.setEnabled(TF)

        if TF:
            self.btnCheckDevice.setStyleSheet("background-color: green")
        else:
            self.btnCheckDevice.setStyleSheet("background-color: red")
    
    def switchWiredDHCP(self):
        self.netConf.isDHCP = self.rbtnIsWiredDHCP.isChecked()
        self.switchEditable("wired", not self.netConf.isDHCP)

    def switchWifiDHCP(self):
        self.netConf.isDHCP = self.rbtnIsWifiDHCP.isChecked()
        self.switchEditable("wifi", not self.netConf.isDHCP)

    def switchMobileType(self):
        if self.rbtnCMNET.isChecked():
            self.netConf.mobileType = dirMobileType["telecom"]
        elif self.rbtnCMCC.isChecked():
            self.netConf.mobileType = dirMobileType["mobile"]
        else:
            self.netConf.mobileType = dirMobileType["unicom"]

    def checkDevice(self):
        processCMD("start-server")
        cmdOut = processCMD("devices")
        if len(cmdOut) > 2:
            deviceStrings = cmdOut[1:]
            firstDevice = deviceStrings[0].decode("utf-8")
            deviceSN = firstDevice.split("device")[0]
            if len(deviceSN) > 1:
                self.lblDeviceID.setText(deviceSN)
                self.switchConfButtons(True)
            else:
                self.lblDeviceID.setText("None")
                self.switchConfButtons(False)
            print(deviceSN)
        else:
            self.lblDeviceID.setText("UNKNOW")
            self.switchConfButtons(False)

        for line in cmdOut:
            self.printLog(line.decode("utf-8"))

def main():
    app = QtWidgets.QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()