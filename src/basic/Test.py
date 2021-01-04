import sys
from PyQt5.QtWidgets import QMainWindow, QApplication

class MyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)

        self.resize(400, 300)

        self.setWindowTitle('First')

        self.move(300, 300)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = MyMainWindow()

    win.show()

    sys.exit(app.exec_())



