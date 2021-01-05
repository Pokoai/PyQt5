'''
自定义 Widget 的2种使用方式：
一、在主程序中导入模块

'''

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QTextEdit, QVBoxLayout
from PyQt5.QtGui import QIcon
# 导入自定义的控件类
from MatplotlibWidget import MatplotlibWidget

class Matplotlib(QWidget):
    # 初始化
    def __init__(self):
        super(Matplotlib, self).__init__()
        self.setWindowTitle('Matplotlib 例子1')
        self.resize(500, 650)
        self.setWindowIcon(QIcon('./images/sandiantu.ico'))

        # 创建控件
        self.matplotwidget1 = MatplotlibWidget()  # 自定义的控件
        self.matplotwidget2 = MatplotlibWidget()  # 自定义的控件
        self.button1 = QPushButton('显示静态图')
        self.button2 = QPushButton('显示动态图')

        # 布局
        layout = QVBoxLayout()
        layout.addWidget(self.matplotwidget1)  # 自定义的控件
        layout.addWidget(self.matplotwidget2)  # 自定义的控件
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        self.setLayout(layout)

        # 绑定信号与槽
        self.button1.clicked.connect(self.button1_Clicked)
        self.button2.clicked.connect(self.button2_Clicked)

    # 槽函数
    def button1_Clicked(self):
        self.matplotwidget1.mpl.start_static_plot()

    def button2_Clicked(self):
        self.matplotwidget2.mpl.start_dynamic_plot()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Matplotlib()
    win.show()
    sys.exit(app.exec_())
