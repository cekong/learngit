
'''
使用普通摄像头进行深度估计
'''
'''
使用普通摄像头进行深度估计
'''


import numpy as np
import cv2

# create windows
cv2.namedWindow('left_Webcam', cv2.WINDOW_NORMAL)
cv2.namedWindow('right_Webcam', cv2.WINDOW_NORMAL)
cv2.namedWindow('disparity', cv2.WINDOW_NORMAL)
blockSize = 40

while(cv2.waitKey(1) & 0xFF != ord('q')):
    left_frame = cv2.imread('/home/deepl/Documents/wb/opencv-3.0.0/samples/data/aloeL.jpg')
    right_frame = cv2.imread('/home/deepl/Documents/wb/opencv-3.0.0/samples/data/aloeR.jpg')
    # our operations on the frame come here
    gray_left = cv2.cvtColor(left_frame, cv2.COLOR_BGR2GRAY)
    gray_right = cv2.cvtColor(right_frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('left_Webcam', gray_left)
    cv2.imshow('right_Webcam', gray_right)
    stereo = cv2.StereoSGBM_create(minDisparity=1,
                                   numDisparities=16,
                                   blockSize=15,
                                  # uniquenessRatio = 10,
                                   speckleWindowSize=55,
                                   speckleRange=32,
                                   disp12MaxDiff=1,
                                   P1=8 * 3 * blockSize ** 2,
                                   P2=32 * 3 * blockSize ** 2)

    disparity = stereo.compute(gray_left, gray_right)
    disparity = cv2.normalize(disparity, disparity, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    cv2.imshow('disparity', disparity)

cv2.destroyAllWindows()