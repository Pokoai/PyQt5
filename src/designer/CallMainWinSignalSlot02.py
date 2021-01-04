import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from MainWinSignalSlot02 import Ui_Form
from PyQt5.QtCore import Qt, pyqtSignal

class MyMainWindow(QMainWindow, Ui_Form):
    # 定义信号
    helpSignal = pyqtSignal(str)
    printSignal = pyqtSignal(list)
    previewSignal = pyqtSignal([int, str], [str])

    # 初始化
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)

        # 绑定信号与槽
        self.helpSignal.connect(self.showHelpMessage)
        self.printSignal.connect(self.printPaper)
        self.previewSignal[str].connect(self.previewPaper)
        self.previewSignal[int, str].connect(self.previewPaperWithArgs)

        self.printButton.clicked.connect(self.emitPrintSignal)
        self.previewButton.clicked.connect(self.emitPreviewSignal)

    # 发射预览信号
    def emitPreviewSignal(self):
        if self.previewStatus.isChecked() == True:
            self.previewSignal[int, str].emit(1080, " Full Screen")
        else:
            self.previewSignal[str].emit("Preview")

    # 发射打印信号
    def emitPrintSignal(self):
        pList = []
        pList.append(self.numberSpinBox.value())
        pList.append(self.styleCombo.currentText())
        self.printSignal.emit(pList)

    # 定义打印槽函数
    def printPaper(self, list):
        self.resultLabel.setText("打印：份数：%d 纸张：%s" % (list[0], list[1]))

    # 定义预览槽函数
    def previewPaper(self, text):
        self.resultLabel.setText(text)

    def previewPaperWithArgs(self, style, text):
        self.resultLabel.setText(str(style) + text)

    # 重载按键事件
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F1:
            self.helpSignal.emit("help message")

    # 定义帮助槽函数
    def showHelpMessage(self, message):
        self.resultLabel.setText(message)
        #print('按下F1')
        self.statusBar().showMessage(message)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    Win = MyMainWindow()
    Win.show()
    sys.exit(app.exec_())