import sys
from PyQt5.QtWidgets import QApplication, QWidget
from WeatherWin import Ui_Form
import requests


class MyMainWindow(QWidget, Ui_Form):
    cityCode = {'杭州':'101210101', '沈阳':'101070101', '安庆':'101010800', '乐安县':'101240403'}

    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)

    def queryWeather(self):
        print('* queryWeather ')
        self.resultText.clear()
        cityName = self.cityComboBox.currentText()
        cityCode = self.cityCode[cityName]

        rep = requests.get('http://www.weather.com.cn/data/sk/' + cityCode + '.html', timeout=30)
        rep.raise_for_status()
        rep.encoding = 'utf-8'
        print(rep.json())

        msg1 = '城市: %s' % rep.json()['weatherinfo']['city'] + '\n'
        msg2 = '温度: %s' % rep.json()['weatherinfo']['temp'] + '度\n'
        msg3 = '湿度: %s' % rep.json()['weatherinfo']['SD'] + '\n'
        msg4 = '风向: %s' % rep.json()['weatherinfo']['WD'] + '\n'
        msg5 = '风力: %s' % rep.json()['weatherinfo']['WS'] + '\n'
        result = msg1 + msg2 + msg3 + msg4 + msg5

        self.resultText.setText(result)

    def clearResult(self):
        print('* clearResult ')
        self.resultText.clear()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    Win = MyMainWindow()
    Win.show()
    sys.exit(app.exec_())