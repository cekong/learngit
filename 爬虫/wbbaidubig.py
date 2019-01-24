


import re
import sys
import urllib
import os

import requests

if __name__ == '__main__':
    tem=urllib.parse.quote('泰勒斯威夫特1920*1080', safe='/')
    pages=3
    n = 0
    for i in range(60,60*pages+60,60):
        url='http://image.baidu.com/search/flip?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1497491098685_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&ctd=1497491098685%5E00_1519X735&word='+tem+'&pn='+str(i)
        html=requests.get(url).text
        pic_url=re.findall('"objURL":"(.*?)",',html,re.S)
        for each in pic_url:
            print(each)
            try:
                pic=requests.get(each,timeout=2)
            except requests.exceptions.ConnectionError:
                print('打不开！')
                continue
            string='/home/deepl/Documents/img/'+str(n)+'.jpg'
            fp=open(string,'wb')
            fp.write(pic.content)
            fp.close()
            n=n+1