'''
自定义 Widget 的2种使用方式：
二、在 designer 中提升 -> ui设计 -> 主程序引用

'''

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from matplotlib_pyqt import Ui_Form

class MyMainWindow(QMainWindow, Ui_Form):
    # 初始化
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)

        # 绑定信号与槽
        self.showStaticButton.clicked.connect(self.buttonStatic_Clicked)
        self.showDynamicButton.clicked.connect(self.buttonDynamic_Clicked)

    # 槽函数
    def buttonStatic_Clicked(self):
        self.matplotlibwidget_static.mpl.start_static_plot()

    def buttonDynamic_Clicked(self):
        self.matplotlibwidget_dynamic.mpl.start_dynamic_plot()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Win = MyMainWindow()
    Win.show()
    sys.exit(app.exec_())