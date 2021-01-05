'''
	查询城市天气数据
'''

import requests

url = 'http://www.weather.com.cn/data/sk/101210101.html'

try:
    rep = requests.get(url, timeout=30)
    rep.raise_for_status()
    rep.encoding = 'utf-8'

    print('返回结果: %s' % rep.json())
    print('城市: %s' % rep.json()['weatherinfo']['city'])
    print('温度: %s' % rep.json()['weatherinfo']['temp'] + " 度")
    print('湿度: %s' % rep.json()['weatherinfo']['SD'])
    print('风向: %s' % rep.json()['weatherinfo']['WD'])
    print('风力: %s' % rep.json()['weatherinfo']['WS'])

except:
    print('爬取失败')