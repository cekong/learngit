'''
ORB基于FAST关键点检测和BRIEF的描述符技术相结合
FAST：特征检测算法。
BRIEF：只是一个描述符，这是图像一种表示方式，
可以比较两个图像的关键点描述符，可作为特征匹配的一种方法。
暴力匹配：比较两个描述符并产生匹配结果。
'''


import numpy as np
import cv2
from matplotlib import pyplot as plt

# query and test images
img1 = cv2.imread('/home/deepl/Documents/wb/opencv-3.0.0/samples/data/graf1.png',0)
img2 = cv2.imread('/home/deepl/Documents/wb/opencv-3.0.0/samples/data/graf3.png',0)

# create the ORB detector
orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

# brute force matching
# 暴力匹配BFMatcher，遍历描述符，确定描述符是否匹配，然后计算匹配距离并排序
# BFMatcher函数参数：
# normType：NORM_L1, NORM_L2, NORM_HAMMING, NORM_HAMMING2。
# NORM_L1和NORM_L2是SIFT和SURF描述符的优先选择，NORM_HAMMING和NORM_HAMMING2是用于ORB算法
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1,des2)

# Sort by distance.
matches = sorted(matches, key = lambda x:x.distance)
# matches是DMatch对象，具有以下属性：
# DMatch.distance - 描述符之间的距离。 越低越好。
# DMatch.trainIdx - 训练描述符中描述符的索引
# DMatch.queryIdx - 查询描述符中描述符的索引
# DMatch.imgIdx - 训练图像的索引。

# 获取img1的关键点位置
x,y = kp1[matches[0].queryIdx].pt
cv2.rectangle(img1, (int(x),int(y)), (int(x) + 5, int(y) + 5), (0, 255, 0), 2)
cv2.imshow('a', img1)

# 获取img2的关键点位置
x1,y1 = kp2[matches[0].trainIdx].pt
cv2.rectangle(img2, (int(x1),int(y1)), (int(x1) + 5, int(y1) + 5), (0, 255, 0), 2)
cv2.imshow('b', img2)


# 使用plt将两个图像的匹配结果显示出来
img3 = cv2.drawMatches(img1,kp1,img2,kp2, matches[:25], img2,flags=2)

plt.imshow(img3),plt.show()