# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWinMenuToolbar.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(542, 364)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(119, 29, 301, 231))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.MaingridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.MaingridLayout.setContentsMargins(0, 0, 0, 0)
        self.MaingridLayout.setObjectName("MaingridLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 542, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuedit = QtWidgets.QMenu(self.menubar)
        self.menuedit.setObjectName("menuedit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.fileNewAction = QtWidgets.QAction(MainWindow)
        self.fileNewAction.setObjectName("fileNewAction")
        self.fileOpenAction = QtWidgets.QAction(MainWindow)
        self.fileOpenAction.setObjectName("fileOpenAction")
        self.fileCloseAction = QtWidgets.QAction(MainWindow)
        self.fileCloseAction.setObjectName("fileCloseAction")
        self.addWinAction = QtWidgets.QAction(MainWindow)
        self.addWinAction.setObjectName("addWinAction")
        self.menuFile.addAction(self.fileNewAction)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.fileOpenAction)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.fileCloseAction)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuedit.menuAction())
        self.toolBar.addAction(self.addWinAction)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuedit.setTitle(_translate("MainWindow", "Edit"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.fileNewAction.setText(_translate("MainWindow", "New"))
        self.fileNewAction.setShortcut(_translate("MainWindow", "Alt+N"))
        self.fileOpenAction.setText(_translate("MainWindow", "Open"))
        self.fileOpenAction.setShortcut(_translate("MainWindow", "Alt+O"))
        self.fileCloseAction.setText(_translate("MainWindow", "Close"))
        self.fileCloseAction.setShortcut(_translate("MainWindow", "Alt+C"))
        self.addWinAction.setText(_translate("MainWindow", "添加窗体"))

