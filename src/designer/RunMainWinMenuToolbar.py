import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from MainWinMenuToolbar import Ui_MainWindow
from ChildrenForm import Ui_ChildrenForm

class MainForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)

        # 创建子窗口实例
        self.child = ChildrenForm()

        # 添加信号与槽函数
        self.fileCloseAction.triggered.connect(self.close)
        self.fileOpenAction.triggered.connect(self.openMsg)
        self.addWinAction.triggered.connect(self.childShow)

    def childShow(self):
        # 添加子窗口
        self.MaingridLayout.addWidget(self.child)
        self.child.show()

    def openMsg(self):
        file, ok = QFileDialog.getOpenFileName(self, "打开", "c:/", "All Files (*);;Text Files (*.txt)")
        self.statusBar.showMessage(file, timeout=0)

class ChildrenForm(QWidget, Ui_ChildrenForm):
    def __init__(self):
        super(ChildrenForm, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())
