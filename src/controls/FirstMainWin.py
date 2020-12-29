import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon

class FirstMainWin(QMainWindow):
    def __init__(self, parent=None):
        super(FirstMainWin, self).__init__(parent)

        # 设置窗口的标题
        self.setWindowTitle('第一个主窗口应用')

        # 设置窗口尺寸
        self.resize(400, 300)

        # 设置状态栏
        self.status = self.statusBar()

        self.status.showMessage('只存在5秒的消息', 5000)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 设置应用图标
    app.setWindowIcon(QIcon('./icons/sandiantu.ico'))

    # 创建实例
    main = FirstMainWin()

    main.show()
    sys.exit(app.exec_())


