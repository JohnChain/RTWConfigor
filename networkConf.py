# -*- coding: utf-8 -*-
#!/usr/bin/python3
import json
import time
import subprocess

dirNetType = ["wired", "wifi", "mobile"]
dirMobileType = {"telecom":"telecom", "mobile":"mobile", "unicom":"unicom"}

def processCMD(cmdStr):
    p = subprocess.Popen(cmdStr, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    cmdOut = p.stdout.readlines()
    _ = p.wait()
    return cmdOut

def updateNetwork(mainJson, netJson):
    mainJson["network"] = netJson

def loadJsonFile(fileName):
    with open(fileName, 'r') as f:
        data = json.load(f)
    return data

def writeJsonFile(fileName, data):
    with open(fileName, 'w') as f:
        json.dump(data, f)

class NetworkConf:
    def __init__(self, parent=None):
        self.fileName = "parser.json"
        self.netType = "wired"
        self.isDHCP = True
        self.ipAddress = ""
        self.mask = ""
        self.gateway = ""
        self.dns = ""
        self.wifiSSID = ""
        self.wifiPasswd = ""
        self.mobileType = ""

    def genConfStr(self):
        jsonDir = {}
        jsonDir["type"] = self.netType
        if self.netType == dirMobileType["mobile"]:
            jsonDir["mobile"] = self.mobileType
        else:
            if self.netType == "wifi":
                wifiInfo = {}
                wifiInfo["ssid"] = self.wifiSSID
                wifiInfo["password"] = self.wifiPasswd
                jsonDir["wifi"] = wifiInfo
            if self.isDHCP:
                jsonDir["access"] = "dynamic"
            else:
                jsonDir["access"] = "static"
                staticInfo = {}
                staticInfo["inet"] = self.ipAddress
                staticInfo["netmask"] = self.mask
                staticInfo["gateway"] = self.gateway
                staticInfo["dns"] = self.dns
                jsonDir["static"] = staticInfo
                
        print (jsonDir)
        return jsonDir

    def updateNetConf(self, fullJsonDir, subNetDir):
        fullJsonDir["network"] = subNetDir
        fullJsonDir["version"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    def downloadNetConf(self):
        self.fullJson = loadJsonFile(self.fileName)
        subNetDir = self.genConfStr()
        self.updateNetConf(self.fullJson, subNetDir)
        writeJsonFile(self.fileName, self.fullJson)