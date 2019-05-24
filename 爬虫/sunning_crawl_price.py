# -*- coding: UTF-8 -*-

import re,requests
import random
import time

url = "http://product.suning.com/0000000000/144016246.html"

pattern1 = re.compile(r"com/(.*?)/(.*?).html")
key=pattern1.findall(url)

priceurl = "http://pas.suning.com/nspcsale_0_000000000" + key[0][1] + "_000000000" + key[0][1] + "_" + key[0][0] + "_20_021_0210101_500353_1000267_9264_12113_Z001___R9006849_3.3_1___000278188__.html?callback=pcData&_=1558663936729"
if len(key[0][1]) == 11 :
    priceurl = "http://pas.suning.com/nspcsale_0_0000000" + key[0][1] + "_0000000" + key[0][1] + "_" + key[0][0] + "_20_021_0210101_500353_1000267_9264_12113_Z001___R9006849_3.3_1___000278188__.html?callback=pcData&_=1558663936729"


s = requests.session()
headers = {'Accept': '*/*',
           'Accept-Language': 'zh-CN',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.15 Safari/537.36'
           }
s.headers.update(headers)
html = s.get(url=priceurl, verify=False).text
time.sleep(random.random())

print(html)

pattern1 = re.compile(r'"netPrice":"(.*?)","warrantyList')
key=pattern1.findall(html)

print(key[0])


s.close()