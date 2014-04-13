# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/rff.ui'
#
# Created: Sun Apr 13 21:08:04 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1020, 732)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.cbServices = QtGui.QComboBox(Form)
        self.cbServices.setObjectName("cbServices")
        self.horizontalLayout_3.addWidget(self.cbServices)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.cbActions = QtGui.QComboBox(Form)
        self.cbActions.setObjectName("cbActions")
        self.horizontalLayout_3.addWidget(self.cbActions)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.tbAddParams = QtGui.QLineEdit(Form)
        self.tbAddParams.setObjectName("tbAddParams")
        self.horizontalLayout_2.addWidget(self.tbAddParams)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tbResults = QtGui.QPlainTextEdit(Form)
        self.tbResults.setObjectName("tbResults")
        self.verticalLayout.addWidget(self.tbResults)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.bSend = QtGui.QPushButton(Form)
        self.bSend.setObjectName("bSend")
        self.horizontalLayout.addWidget(self.bSend)
        self.bSave = QtGui.QPushButton(Form)
        self.bSave.setMaximumSize(QtCore.QSize(100, 16777215))
        self.bSave.setObjectName("bSave")
        self.horizontalLayout.addWidget(self.bSave)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Run for fun app test", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Service:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Action:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Additional arguments:", None, QtGui.QApplication.UnicodeUTF8))
        self.bSend.setText(QtGui.QApplication.translate("Form", "Send", None, QtGui.QApplication.UnicodeUTF8))
        self.bSave.setText(QtGui.QApplication.translate("Form", "Save", None, QtGui.QApplication.UnicodeUTF8))

