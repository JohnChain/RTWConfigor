# -*- coding: utf-8 -*-
#!/usr/bin/python3
import json

fileName = "parser.json"

def updateNetwork(mainJson, netJson):
    mainJson["network"] = netJson

def loadJsonFile(fileName):
    with open(fileName, 'r') as f:
        data = json.load(f)
    return data

def writeJsonFile(fileName, data):
    with open(fileName, 'w') as f:
        json.dump(data, f)

def main():
    mainJson = loadJsonFile(fileName)
    mainJson["network"]["type"] = "wifi"
    writeJsonFile(fileName, mainJson)
    mainJson = loadJsonFile(fileName)
    print (mainJson["network"])

    mainJson["network"]["type"] = "wired"
    writeJsonFile(fileName, mainJson)
    mainJson = loadJsonFile(fileName)
    print (mainJson["network"])

if __name__ == "__main__":
    main()