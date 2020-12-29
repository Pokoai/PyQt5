import sys
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QApplication, QPushButton, QWidget

class QuitApplication(QMainWindow):
    def __init__(self):
        super(QuitApplication,self).__init__()

        self.setWindowTitle('退出应用程序')
        self.resize(300, 200)

        # 添加Button
        self.button1 = QPushButton('退出应用程序')
        # 绑定信号与槽
        self.button1.clicked.connect(self.onClick_Button)

        # 创建水平布局
        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        # 框架
        mainFrame = QWidget()
        mainFrame.setLayout(layout)

        self.setCentralWidget(mainFrame)

    # 按钮单击事件的方法（自定义的槽）
    def onClick_Button(self):
        sender = self.sender()
        print(sender.text() + ' 按钮被按下')
        app = QApplication.instance()
        # 退出应用程序
        app.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 创建实例
    main = QuitApplication()

    main.show()
    sys.exit(app.exec_())