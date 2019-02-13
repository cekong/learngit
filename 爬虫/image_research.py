'''以图搜图'''
# -*-coding:utf-8-*-
import requests
import json
import re,os
import itertools
from hashlib import md5
count=0


def down_pic(pic_urls, localPath):
    global count
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36"
    headers ={'User-Agent': user_agent, "Upgrade-Insecure-Requests": 1,
     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
     "Accept-Encoding": "gzip, deflate, sdch",
     "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
     "Cache-Control": "no-cache"}
    if not os.path.exists(localPath):  # 新建文件夹
        os.mkdir(localPath)
    """给出图片链接列表, 下载图片"""
    # print(pic_urls)
    for pic_url in pic_urls:
        count = count + 1
        try:
            pic = requests.get(pic_url, timeout=15)
            picname=md5(pic.content).hexdigest()+'.jpg'
            picPath=localPath+picname
            if not os.path.exists(picPath):
                with open(picPath, 'wb') as f:
                    f.write(pic.content)
                    f.close()
            print('成功下载第%s张图片: %s' % (str(count), str(pic_url)))
        except Exception as e:
            print('下载第%s张图片时失败: %s' % (str(count), str(pic_url)))
            print(e)
            continue



def get_response(files,imgpath):
    url = '/pcdutu/a_upload?fr=html5&target=pcSearchImage&needJson=true'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    }
    source = 'http://image.baidu.com'
    vs_url = source + '/?fr=shitu'
    vs_page = requests.get(vs_url, headers=headers).text
    vs_id = re.findall('window.vsid = "(.*?)"', vs_page)[0]
    r = requests.post(source + url, headers=headers, files=files)
    tmp = r.text
    tmp_json = json.loads(tmp)
    queryImageUrl = tmp_json['url']
    querySign = tmp_json['querySign']
    url2 = source + '/pcdutu/a_similar?queryImageUrl=' + queryImageUrl + '&querySign=' + querySign + '&simid=undefined&word=&querytype=0&t=1534831269418&rn=60&sort=&fr=pc&pn={pn}'
    url3 = (url2.format(pn=x) for x in itertools.count(start=0, step=60))
    for url in url3:
        html = requests.get(url, timeout=10).text
        a = re.compile(r'"ObjURL":"(.*?)"')
        downURL = re.findall(a, html)
        down_pic(list(set(downURL)), imgpath)
        if len(downURL)==0:
             print('已下载全部搜索到的图片')
             break


if __name__ == '__main__':
    #############需要输入的图片
    path0 = os.getcwd()
    dish_path=path0+'/dish'
    folderlist=os.listdir(dish_path)
    for folder in folderlist:
        count = 0
        folderpath=dish_path+'/'+folder
        filelist = os.listdir(folderpath)
        for file in filelist:
            ext=os.path.splitext(file)[1]
            if ext == '.jpg':
                files = {'file': (file, open(folderpath + '/' + file, 'rb'), 'image/jpg'), 'pos': (None, 'upload'),
                         'uptype': (None, 'upload_pc'), 'fm': (None, 'home')}
                filename=file.split(".")[0]
                imgpath=folderpath+'/結果/'
                get_response(files,imgpath)

