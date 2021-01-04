import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QHBoxLayout, QPushButton
from PyQt5.QtGui import QIcon

class QuitApplication(QMainWindow):
    # 结构函数-初始化
    def __init__(self):
        super(QuitApplication, self).__init__()

        # 设置窗口标题
        self.setWindowTitle('关闭窗口程序')
        # 设置窗口尺寸
        self.resize(400, 300)
        # 设置窗口位置
        self.move(300, 300)

        # 创建一个按键
        self.button1 = QPushButton('关闭主窗口')
        # 创建水平布局
        layout = QHBoxLayout()
        # 将按键添加到水平布局里
        layout.addWidget(self.button1)
        # 创建一个框架
        main_frame = QWidget()
        # 将布局放到框架里
        main_frame.setLayout(layout)
        # 将框架放到窗口中心的位置
        self.setCentralWidget(main_frame)

        # 绑定信号与槽
        self.button1.clicked.connect(self.onButtonClick)

    # 定义 onButtonClick 方法
    def onButtonClick(self):
        # 创建发送对象
        sender = self.sender()
        # 被按下就显示信息
        print(sender.text() + '被按下')
        # 创建应用实例
        app = QApplication.instance()
        # 结束应用
        app.quit()


if __name__ == '__main__':
    # 创建一个应用程序
    app = QApplication(sys.argv)
    # 设置程序图标
    app.setWindowIcon(QIcon('./images/sandiantu.ico'))
    # 窗口实例化
    win = QuitApplication()
    # 显示窗口
    win.show()
    # 程序循环运行
    sys.exit(app.exec_())