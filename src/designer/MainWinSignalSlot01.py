# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWinSignalSlot01.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.closeWinBtn = QtWidgets.QPushButton(Form)
        self.closeWinBtn.setGeometry(QtCore.QRect(120, 110, 75, 23))
        self.closeWinBtn.setObjectName("closeWinBtn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.closeWinBtn.setText(_translate("Form", "关闭窗口"))

