import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QTextEdit, QVBoxLayout
from PyQt5.QtGui import QIcon
# 引入自定义的控件类
from MatplotlibWidget import MatplotlibWidget

class TextEdit(QWidget):
    # 初始化
    def __init__(self):
        super(TextEdit, self).__init__()
        self.setWindowTitle('QTextEdit 例子')
        self.resize(500, 400)
        self.setWindowIcon(QIcon('./images/sandiantu.ico'))

        # 创建控件
        self.matplot = MatplotlibWidget() # 自定义的控件
        self.textEdit = QTextEdit()
        self.button1 = QPushButton('显示文本')
        self.button2 = QPushButton('显示HTML')

        # 布局
        layout = QVBoxLayout()
        layout.addWidget(self.matplot) # 自定义的控件
        layout.addWidget(self.textEdit)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        self.setLayout(layout)

        # 绑定信号与槽
        self.button1.clicked.connect(self.button1_Clicked)
        self.button2.clicked.connect(self.button2_Clicked)

    # 槽函数
    def button1_Clicked(self):
        self.textEdit.setPlainText('Hello PyQt5!\n你好')

    def button2_Clicked(self):
        self.textEdit.setHtml("<font color='red', size='6'><red>Hello PyQt5!\n 单击按钮。</font>")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = TextEdit()
    win.show()
    sys.exit(app.exec_())
