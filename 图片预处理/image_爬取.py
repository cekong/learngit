import requests
import re
import os
import urllib.parse
from lxml import etree
import json


page_num = 30
photo_dir = "/media/deepl/文档/platedata"


def getDetailImage(word):
    num = 0
    count=0
    url = "https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord={0}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&hd=&latest=&copyright=&word={0}&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn={1}&rn=" + str(
        page_num) + "&gsm=1e&1552975216767="
    while num < 50:

        page_url = url.format(urllib.parse.quote(word), num * page_num)
        print(page_url)
        response = requests.get(page_url)

        regex = re.compile(r'\\(?![/u"])')
        json_data = json.loads(regex.sub(r"\\\\", response.text))  # 问题在于编码中是\xa0之类的，当遇到有些 不用转义的\http之类的，则会出现以上错误
        for item in json_data['data']:
            try:
                params = {
                    "word": word,
                    "di": item['di'],
                    "tn": "baiduimagedetail",
                    "cs": item['cs'],
                    "os": item['os'],
                }
                detail_url = "http://image.baidu.com/search/detail"
                response = requests.get(detail_url, params=params,timeout=5)
                selector = etree.HTML(response.text)
                pic_url = selector.xpath("//img[@id='hdFirstImgObj']/@src")[0]
                print(count,'****',pic_url)
                count=count+1
                name = 'hhyzms' + '%d.jpg' % count
                headers = {
                    "Referer": page_url,
                }

                html = requests.get(pic_url, headers=headers,timeout=5)
                with open(os.path.join(word_dir, name), 'wb')as f:
                    f.write(html.content)
            except:
                pass

        num = num + 1


if __name__ == "__main__":
    word = '豪华一桌大餐美食图片'
    word_dir = os.path.join(photo_dir, word)
    if not os.path.exists(word_dir):
        os.mkdir(word_dir)
    # qword= '一桌点心'
    getDetailImage(word)