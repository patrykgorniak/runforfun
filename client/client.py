#!/usr/bin/env python3

from PySide.QtGui import QApplication, QWidget
from ui_rff import Ui_Form

import sys
import httplib2
from urllib.parse import urlencode
import json

URL="http://127.0.0.1:8000/rff/?"
METHOD="GET"

fHttp=httplib2.Http()

def request(url, method, body):
    if 'service' not in body:
        body = {'service': 'datasport', 'action': 'get_events'}
    resp,content = fHttp.request(URL+urlencode(body),method)
    return content.decode()



class MainWindow(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.connectSlots()
        self.initialize()

    def connectSlots(self):
        self.bSend.clicked.connect(self.bSendClicked)
        self.bSave.clicked.connect(self.bSaveClicked)

    def bSendClicked(self):
        args = {'service': self.cbServices.currentText(), 'action': self.cbActions.currentText() }
        self.tbResults.clear()
        self.tbResults.setPlainText(request(URL, METHOD, args))

    def bSaveClicked(self):
        text = self.tbResults.toPlainText()
        if text != "":
            if text.startswith('user'):
                self.tbAddParams.setText(text.split(';')[0])


    def initialize(self):
        self.cbServices.addItem("datasport")
        self.cbActions.addItem("get_events")
        self.cbActions.addItem("login")




def main():
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    app.exec_()

if __name__ == "__main__":
    main()