import time
import os

if __name__ == '__main__':
    for i in range(20):
        os.system("python openweb.py")
        print("正在刷新页面. 次数 =>", i + 1)
        time.sleep(10)