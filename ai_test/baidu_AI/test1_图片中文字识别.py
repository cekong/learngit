import cv2
from aip import AipOcr

""" 填入参数 """
APP_ID = '**'
API_KEY = '**'
SECRET_KEY = '**'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)



""" 读取图片 """
fname = 'j_test_ocr.jpg'
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
image = get_file_content(fname)



""" 调用通用文字识别, 图片参数为本地图片 """
'''
调用通用文字识别basicGeneral
高精度版就是basicAccurate
具体参数见：http://ai.baidu.com/docs#/OCR-Python-SDK/top
'''
text = client.basicGeneral(image)

for each in text.get('words_result'):
    print(each.get('words'))        #返回的是个json，内容在这里面
print('--------------------------------------------')



""" 调用通用文字识别, 含位置信息 """
'''
accurate 含位置高精度
'''
results = client.general(image)["words_result"]  # 还可以使用身份证驾驶证模板，直接得到字典对应所需字段

img = cv2.imread(fname)
for result in results:
    text = result["words"]
    location = result["location"]

    print(text)
    # 画矩形框
    cv2.rectangle(img, (location["left"],location["top"]),
                  (location["left"]+location["width"],
                   location["top"]+location["height"]), (0,255,0), 2)

cv2.imwrite(fname[:-4]+"_result.jpg", img)



