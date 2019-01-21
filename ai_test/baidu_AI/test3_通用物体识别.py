from aip import AipImageClassify
import os

""" 填入参数"""
APP_ID = '**'
API_KEY = '**'
SECRET_KEY = '**'

client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

dish_path = os.getcwd()
dish_path = dish_path + '/object'
folderlist = os.listdir(dish_path)
for folder in folderlist:
    filePath=dish_path + '/'+folder
    image = get_file_content(filePath)

    """ 调用通用物体识别 """
    results = client.advancedGeneral(image)
    result = results['result'][0]
    print(result['keyword'], '\t置信度：', result['score'])