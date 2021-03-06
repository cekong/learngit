#!coding=utf-8
import requests,re
import random
import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning

import xlwt
from lxml import etree
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)  ###禁止提醒SSL警告



workbook = xlwt.Workbook()
worksheet = workbook.add_sheet("Sheet Name")
exceltitle=['商品名称','商品价格','商品链接','商品图片','类型','口味','产地','保质期','是否含糖','脂肪含量','适用人群',
                    '储存方式','包装','单件净含量','包装件数']
for m in range(len(exceltitle)):
    worksheet.write(0, m, exceltitle[m])
class suning(object):

    def __init__(self):
        self.s = requests.session()
        headers = {'Accept': '*/*',
                   'Accept-Language': 'zh-CN',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.15 Safari/537.36'
                   }
        self.s.headers.update(headers)
        self.row=1




    def closes(self):
        self.s.close()

    def gooddetail(self,good_detail):
        detailurl=good_detail['商品链接']
        detail = self.s.get(url=detailurl, verify=False).text
        time.sleep(random.random())
        detail = etree.HTML(detail)
        key = detail.xpath(u'//table[@id="itemParameter"]/tbody/tr/td[@class="name"]/div/span/text()')
        value=detail.xpath(u'//table[@id="itemParameter"]/tbody/tr/td[@class="val"]/text()')

        if len(key) >2:
            worksheet.write(self.row, 0, good_detail['商品名称'])
            worksheet.write(self.row, 1, good_detail['商品价格'])
            worksheet.write(self.row, 2, good_detail['商品链接'])
            worksheet.write(self.row, 3, good_detail['商品图片'])
            for keyi in range(len(key)):
                for m in range(len(exceltitle)):
                    if key[keyi] == exceltitle[m]:
                        if '品牌' in key:
                            worksheet.write(self.row, m, value[keyi-1])
                        else:
                            worksheet.write(self.row, m, value[keyi])
            print(self.row)
            self.row += 1

        workbook.save('data.xlsx')


    def getgoodprice(self,url):
        pattern1 = re.compile(r"com/(.*?)/(.*?).html")
        key = pattern1.findall(url)

        priceurl = "http://pas.suning.com/nspcsale_0_000000000" + key[0][1] + "_000000000" + key[0][1] + "_" + key[0][
            0] + "_20_021_0210101_500353_1000267_9264_12113_Z001___R9006849_3.3_1___000278188__.html?callback=pcData&_=1558663936729"
        if len(key[0][1]) == 11:
            priceurl = "http://pas.suning.com/nspcsale_0_0000000" + key[0][1] + "_0000000" + key[0][1] + "_" + key[0][
                0] + "_20_021_0210101_500353_1000267_9264_12113_Z001___R9006849_3.3_1___000278188__.html?callback=pcData&_=1558663936729"

        html = self.s.get(url=priceurl, verify=False).text
        time.sleep(random.random())
        pattern1 = re.compile(r'"netPrice":"(.*?)","warrantyList')
        key = pattern1.findall(html)
        price=key[0]
        return price

    def good(self,url):
        html = self.s.get(url=url, verify=False).text
        time.sleep(random.random())
        html = etree.HTML(html)

        href=html.xpath(u'//div[@class="title-selling-point"]/a/@href')
        name = html.xpath(u'//div[@class="res-img"]/div/a/img/@alt')
        imageurl=html.xpath('//div[@class="res-img"]/div/a/img/@src')

        for namei in range(len(name)):
            if name[namei] !='\n':
                detailurl='http:'+href[namei]
                good_detail={}
                good_detail['商品链接']=detailurl
                image_url='http:'+imageurl[namei]
                good_detail['商品图片'] = image_url
                item = name[namei].strip()
                good_detail['商品名称'] = item
                good_detail['商品价格']=self.getgoodprice(detailurl)
                self.gooddetail(good_detail)
    def getpagelist(self,url,v):
        urls=[]
        html = self.s.get(url=url.format("0",v), verify=False).text
        time.sleep(random.random())
        html = etree.HTML(html)
        pagenum = html.xpath(u'/html/body/div[9]/div/div/div/a[last()-1]/@pagenum')
        urls.append(url.format("0",v))
        if len(pagenum)>0:
            pagenum = int(pagenum[0])
            for i in range(1,pagenum):
                urls.append(url.format(str(i),v))
        return urls


if __name__ == '__main__':

    sn = suning()

    brand_categories = {'伊利': '6063197', '蒙牛': '41573', '君乐宝': '21530', '光明': '4340904'}

    for k, v in brand_categories.items():
        url = 'https://list.suning.com/0-500479-{}-0-0-0-0-0-0-0-{}.html'
        pageurls=sn.getpagelist(url,v)
        for i in range(len(pageurls)):
            sn.good(pageurls[i])
    sn.closes()
