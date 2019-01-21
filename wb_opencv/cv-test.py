import cv2
import numpy as np

# 读图
img = cv2.imread('imageTest.jpg',1)
# 展示图
cv2.imshow('src',img)

# 获取图片信息
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
# 设置一个偏移矩阵 两行三列数据
matShift = np.float32([[1,0,100],[0,1,200]])# 2*3
# 目标图片warpAffine，完成矩阵的映射。
# 参数1: 原图片 参数2: 移位矩阵 参数3: 当前图片的高宽
dst = cv2.warpAffine(img,matShift,(height,width)) # 1 data 2 matshift 3 info
# 移位 矩阵运算

cv2.imshow('dst',dst)
cv2.waitKey(0)