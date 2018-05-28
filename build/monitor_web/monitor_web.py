# coding:utf-8
import time
import requests
import os
url = "http://www.cninfo.com.cn/server-status"
f = open('D:\\' + 'result' + '.txt','w')
#file_name = 'result.tex'

def get_website_status (url):
    res = requests.head(url)
    time.sleep(5)
    return res.status_code

if __name__ == '__main__':
    while 1:
        if get_website_status(url) == 200 :
            print(time.asctime(),"检测访问",url,"正常")
            print(( time.asctime(),'%s status is ok' %url),file=f)
        else:
            print("检测异常，异常时间：",time.asctime(),"请查看D盘目录下resul.txt文件")
            print (('%s status is error' %url),file=f)
            print(get_website_status(url))




