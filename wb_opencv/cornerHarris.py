
'''
角点检测
https://blog.csdn.net/HuangZhang_123/article/details/80660688
'''

import cv2
import numpy as np
import sys

img = cv2.imread('/home/deepl/Documents/wb/opencv-3.0.0/samples/data/pic1.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 3, 23, 0.04)
# cornerHarris参数： # src - 数据类型为 float32 的输入图像。
#  blockSize - 角点检测中要考虑的领域大小。
#  ksize - Sobel 求导中使用的窗口大小
#  k - Harris 角点检测方程中的自由参数,取值参数为 [0,04,0.06].

img[dst>0.01 * dst.max()] = [0, 0, 255]

# 变量a的阈值为0.01 * dst.max()，如果dst的图像值大于阈值，那么该图像的像素点设为True，否则为False
# 将图片每个像素点根据变量a的True和False进行赋值处理，赋值处理是将图像角点勾画出来

while (True):
    cv2.imshow('corners', img)
    if cv2.waitKey(1000 // 12) & 0xff == ord("q"):
        break
cv2.destroyAllWindows()