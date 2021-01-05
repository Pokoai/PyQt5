import sys
import time

from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class WebView(QWebEngineView):
    def __init__(self):
        super(WebView, self).__init__()
        url = 'https://arctee.cn/639.html'
        self.load(QUrl(url))
        self.show()
        # 使用定时器5秒后关闭窗口
        QTimer.singleShot(1000*5, self.close)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    web = WebView()
    print('### exec succeed !')
    sys.exit(app.exec_())