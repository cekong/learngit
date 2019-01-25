''''''
'''
全屏显示图片
https://github.com/Hironsan/BossSensor/blob/master/image_show.py
人脸识别老板探测器
https://blog.csdn.net/u011001084/article/details/54340392
'''
import sys
import cv2
from PyQt5 import QtGui,QtWidgets


def show_image(image_path='2019-01-17 09-50-58屏幕截图.png'):
    app = QtWidgets.QApplication(sys.argv)
    pixmap = QtGui.QPixmap(image_path)
    screen = QtWidgets.QLabel()
    screen.setPixmap(pixmap)
    screen.showFullScreen()
    sys.exit(app.exec_())


if __name__ == '__main__':
    # show_image()
    while True:
        show_image()
        print("1")
        # 10msec等待输入键
        k = cv2.waitKey(100)
        # Esc按下按键后结束
        if k == 27:
            break
