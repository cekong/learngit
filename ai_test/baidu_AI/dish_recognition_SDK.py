''''''
'''
           百度人工智能api
AipImageClassify是图像识别的Python SDK客户端
'''
from aip import AipImageClassify
import os


""" 填入参数 """
APP_ID = 'your APP_ID'
API_KEY = 'your API_KEY'
SECRET_KEY = 'your SECRET_KEY'
client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)


""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


def dish_Detect():
    dish_path = os.getcwd()
    dish_path = dish_path + '/dish'
    folderlist = os.listdir(dish_path)
    for folder in folderlist:
        filePath=dish_path + '/'+folder
        image = get_file_content(filePath)
        """ 调用菜品识别 """
        results=client.dishDetect(image)
        result = results['result'][0]
        print(folder,
              '\t菜品为：',result['name'],
              '\t置信度：', result['probability'],
              '\t卡路里：', result['calorie'])

if __name__ == '__main__':
    dish_Detect()