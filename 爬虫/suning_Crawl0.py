#!coding=utf-8
import requests
import re
import math
import random
import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import pandas as pd
import xlrd
import xlwt
from lxml import etree
import MySQLdb

# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)  ###禁止提醒SSL警告


class suning(object):

    def __init__(self):
        self.s = requests.session()
        headers = {'Accept': '*/*',
                   'Accept-Language': 'zh-CN',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.15 Safari/537.36'
                   }
        self.s.headers.update(headers)



    def closes(self):
        self.s.close()

    def gooddetail(self,item,detailurl,image_url):
        detail = self.s.get(url=detailurl, verify=False).text
        time.sleep(random.random())
        # print(html)
        detail = etree.HTML(detail)
        key = detail.xpath(u'//table[@id="itemParameter"]/tbody/tr/td[@class="name"]/div/span/text()')
        value=detail.xpath(u'//table[@id="itemParameter"]/tbody/tr/td[@class="val"]/text()')
        print(len(key))
        print(len(value))
        if len(value) >2:
            sql = "INSERT INTO sunning(name, url,imageurl,detail_madein, detail_class,detail_place,detail_period,detail_suger,detail_fat,detail_people,detail_store,detail_packaging,detail_weight,detail_count) VALUES ('%s', '%s', '%s','%s', '%s', '%s', '%s', '%s','%s', '%s', '%s', '%s','%s', '%s')" % (item,detailurl,image_url,value[0], value[1],value[2],value[3], value[4],value[5],value[6], value[7],value[8], value[9],value[10])
            cursor.execute(sql)
            db.commit()
        print(key,value)
        print('////////////////////////////////////')
    def good(self,url):
        html = self.s.get(url=url, verify=False).text
        time.sleep(random.random())
        html = etree.HTML(html)

        href=html.xpath(u'//div[@class="title-selling-point"]/a/@href')
        name = html.xpath(u'//div[@class="title-selling-point"]/a/text()')
        imageurl=html.xpath('//div[@class="res-img"]/div/a/img/@src')

        i=0
        for item in name:
            if item !='\n':
                detailurl='http:'+href[i]
                print(detailurl)
                image_url='http:'+imageurl[i]
                print(image_url)
                item=item.strip()
                self.gooddetail(item,detailurl,image_url)
                i += 1

        db.close()
        print('-----------------------------------------------------------------')
        return name



if __name__ == '__main__':
    db = MySQLdb.connect("127.0.0.1", "root", "password", "my_test", charset='utf8')
    cursor = db.cursor()
    sn = suning()

    brand_categories = {'伊利': '6063197', '蒙牛': '41573', '君乐宝': '21530', '光明': '4340904'}
    writer = pd.ExcelWriter(r'/home/deepl/data.xlsx', engine='openpyxl')
    exlheaders=['商品名称','商品价格','商品图片','详情url']
    for k, v in brand_categories.items():
        url = 'https://list.suning.com/0-500479-0-0-0-0-0-0-0-0-{}.html'.format(v)
        df=sn.good(url)
    sn.closes()