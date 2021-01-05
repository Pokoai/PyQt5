# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'matplotlib_pyqt.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(589, 560)
        self.matplotlibwidget_static = MatplotlibWidget(Form)
        self.matplotlibwidget_static.setGeometry(QtCore.QRect(0, 0, 411, 261))
        self.matplotlibwidget_static.setObjectName("matplotlibwidget_static")
        self.showStaticButton = QtWidgets.QPushButton(Form)
        self.showStaticButton.setGeometry(QtCore.QRect(430, 120, 75, 23))
        self.showStaticButton.setObjectName("showStaticButton")
        self.showDynamicButton = QtWidgets.QPushButton(Form)
        self.showDynamicButton.setGeometry(QtCore.QRect(430, 340, 75, 23))
        self.showDynamicButton.setObjectName("showDynamicButton")
        self.matplotlibwidget_dynamic = MatplotlibWidget(Form)
        self.matplotlibwidget_dynamic.setGeometry(QtCore.QRect(40, 260, 371, 301))
        self.matplotlibwidget_dynamic.setObjectName("matplotlibwidget_dynamic")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.showStaticButton.setText(_translate("Form", "显示静态图"))
        self.showDynamicButton.setText(_translate("Form", "显示动态图"))

from MatplotlibWidget import MatplotlibWidget
