'''
自定义 Widget 的2种使用方式：
二、在 designer 中提升 -> ui设计 -> 主程序引用
并且使用 @pyqtSlot()
'''

import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow
from matplotlib_pyqt import Ui_Form

class MyMainWindow(QMainWindow, Ui_Form):
    # 初始化
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)
        self.matplotlibwidget_dynamic.setVisible(False)
        self.matplotlibwidget_static.setVisible(False)

    @pyqtSlot()
    def on_showStaticButton_clicked(self):
        self.matplotlibwidget_static.setVisible(True)
        self.matplotlibwidget_static.mpl.start_static_plot()

    @pyqtSlot()
    def on_showDynamicButton_clicked(self):
        self.matplotlibwidget_dynamic.setVisible(True)
        self.matplotlibwidget_dynamic.mpl.start_dynamic_plot()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Win = MyMainWindow()
    Win.show()
    sys.exit(app.exec_())