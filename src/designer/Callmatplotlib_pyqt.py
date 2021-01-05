import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from matplotlib_pyqt import Ui_Form
from PyQt5.QtCore import Qt, pyqtSignal

class MyMainWindow(QMainWindow, Ui_Form):
    # 初始化
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Win = MyMainWindow()
    Win.show()
    sys.exit(app.exec_())