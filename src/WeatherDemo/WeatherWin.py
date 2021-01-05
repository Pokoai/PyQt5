# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WeatherWin.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(533, 370)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 30, 491, 251))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 30, 54, 12))
        self.label.setObjectName("label")
        self.cityComboBox = QtWidgets.QComboBox(self.groupBox)
        self.cityComboBox.setGeometry(QtCore.QRect(90, 25, 101, 22))
        self.cityComboBox.setObjectName("cityComboBox")
        self.cityComboBox.addItem("")
        self.cityComboBox.addItem("")
        self.cityComboBox.addItem("")
        self.cityComboBox.addItem("")
        self.resultText = QtWidgets.QTextEdit(self.groupBox)
        self.resultText.setGeometry(QtCore.QRect(20, 70, 451, 161))
        self.resultText.setObjectName("resultText")
        self.queryBtn = QtWidgets.QPushButton(Form)
        self.queryBtn.setGeometry(QtCore.QRect(140, 310, 75, 23))
        self.queryBtn.setObjectName("queryBtn")
        self.clearBtn = QtWidgets.QPushButton(Form)
        self.clearBtn.setGeometry(QtCore.QRect(290, 310, 75, 23))
        self.clearBtn.setObjectName("clearBtn")

        self.retranslateUi(Form)
        self.queryBtn.clicked.connect(Form.queryWeather)
        self.clearBtn.clicked.connect(Form.clearResult)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "天气查询"))
        self.groupBox.setTitle(_translate("Form", "查询城市天气"))
        self.label.setText(_translate("Form", "城市："))
        self.cityComboBox.setItemText(0, _translate("Form", "杭州"))
        self.cityComboBox.setItemText(1, _translate("Form", "沈阳"))
        self.cityComboBox.setItemText(2, _translate("Form", "乐安县"))
        self.cityComboBox.setItemText(3, _translate("Form", "安庆"))
        self.queryBtn.setText(_translate("Form", "查询"))
        self.clearBtn.setText(_translate("Form", "清空"))

