''''''
'''
python 将数据写入excel
https://www.cnblogs.com/liuyang92/p/7492336.html
Python爬虫基础之Requests和XPath实例（二）
https://blog.csdn.net/weixin_42555080/article/details/85171506
'''

import requests
from lxml import etree
from xlrd import open_workbook
from xlutils.copy import copy
#得到页面全部内容
def askURL(url):
    #request = urllib.Request(url)#发送请求
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'}
    response = requests.get(url,headers=headers)#取得响应
    response.encoding='GBK' #防止中文乱码
    # print(response)
    return response.text

#获取相关内容
def getData(baseurl):
    for i in range(1,65):
        url=baseurl+str(i)
        html=askURL(url)
        selector = etree.HTML(html)
        hrefs=selector.xpath('/html/body/table[5]/tr/td[2]/table/tr[2]/td/table/tr[2]/td/table/tr/td/table[2]/tr/td/a/@href')
        names=selector.xpath('/html/body/table[5]/tr/td[2]/table/tr[2]/td/table/tr[2]/td/table/tr/td/table[2]/tr/td/a/text()')
        diqus=selector.xpath('/html/body/table[5]/tr/td[2]/table/tr[2]/td/table/tr[2]/td/table/tr/td/table[2]/tr/td[2]/text()')
        j=0
        for diqu in diqus:
            ws.write((i-1)*12+j, 0, diqu)
            ws.write((i - 1) * 12 + j, 1, names[j*2])
            ws.write((i - 1) * 12 + j, 2, hrefs[j*2])
            j+=1


baseurl='http://www.12333sh.gov.cn/wsbs/zypxjd/2007zpsy/2007pxjg/px.shtml?pageno='
# response=askURL(baseurl)
rb = open_workbook('1.xlsx')
rs = rb.sheet_by_index(0)
wb = copy(rb)
ws = wb.get_sheet(0)
getData(baseurl)
wb.save('1.xlsx')




