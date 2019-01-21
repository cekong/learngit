''''''
'''
    百度人工智能api
用于菜品识别。即对于输入的一张图片（可正常解码，且长宽比适宜），
输出图片的菜品名称、卡路里信息、置信度。
步骤：
1.获取access_token
2.图片设置base64
'''
import requests
import base64
from baidu_AI.get_access_token import GetToken
import os

""" 填入参数 """
API_KEY = 'your API_KEY'
SECRET_KEY = 'your SECRET_KEY'
url = "https://aip.baidubce.com/rest/2.0/image-classify/v2/dish"

def DishRecg(url,data,access_token,folder):
    header = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    request_url = url + "?access_token=" + access_token
    response=requests.post(url=request_url,data=data,headers=header).json()
    result=response['result'][0]
    print(folder,
          '\t菜品为：',result['name'],
          '\t置信度：', result['probability'],
          '\t卡路里：', result['calorie'])


def image_base64(imagepath):
    # 二进制方式打开图片文件
    f = open(imagepath, 'rb')
    img = base64.b64encode(f.read())
    return img


if __name__ == "__main__":
    data={}
    access_token = GetToken(API_KEY, SECRET_KEY)
    dish_path = os.getcwd()
    dish_path = dish_path + '/dish'
    folderlist = os.listdir(dish_path)
    for folder in folderlist:
        imagepath=dish_path + '/' + folder
        image=image_base64(imagepath)
        data['image']=str(image,'utf-8')
        DishRecg(url,data,access_token,folder)
