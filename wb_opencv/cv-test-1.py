'''
OpenCV获取摄像头数据并显示在窗口里 Python实现,左键单击停止
'''
import cv2

clicked = False
def onMouse(event, x, y, flags, param):
    global clicked
    if event == cv2.EVENT_LBUTTONUP:
        clicked = True
# cameraCapture = cv2.VideoCapture(0)#获取摄像头数据
cameraCapture=cv2.VideoCapture('/home/deepl/Documents/wb/opencv-3.0.0/samples/data/768x576.avi')
cv2.namedWindow('MyWindow')
cv2.setMouseCallback('MyWindow', onMouse)
success, frame = cameraCapture.read()
while success and cv2.waitKey(1) == -1 and not clicked:
    keycode = cv2.waitKey(1)
    cv2.imshow('MyWindow', frame)
    success, frame = cameraCapture.read()
cv2.destroyWindow('MyWindow')
cameraCapture.release()