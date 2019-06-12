# -*- coding: utf-8 -*-
#!/usr/local/bin/python
from PyQt5 import QtGui, QtWidgets
import sys
import TumConf

class ExampleApp(QtWidgets.QMainWindow, TumConf.Ui_TUMCONF):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        self.registEvent()

    def registEvent(self):
        self.btnCheckDevice.clicked.connect(self.checkDevice)
        #TODO: regist all other hot events

    def checkDevice(self):
        print ("hello will checkDevice")

def main():
    app = QtWidgets.QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()