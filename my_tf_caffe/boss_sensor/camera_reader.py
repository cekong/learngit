''''''
"""
人脸识别老板探测器
https://blog.csdn.net/u011001084/article/details/54340392
https://github.com/Hironsan/BossSensor
"""
import cv2

from boss_sensor.boss_train import Model
from boss_sensor.image_show import show_image


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    cascade_path = "/usr/local/opt/opencv/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml"
    model = Model()
    model.load()
    while True:
        _, frame = cap.read()

        # 灰度级变换
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 获得级联分器的特征量
        cascade = cv2.CascadeClassifier(cascade_path)

        # 物体识别(脸部识别)的执行
        facerect = cascade.detectMultiScale(frame_gray, scaleFactor=1.2, minNeighbors=3, minSize=(10, 10))
        #facerect = cascade.detectMultiScale(frame_gray, scaleFactor=1.01, minNeighbors=3, minSize=(3, 3))
        if len(facerect) > 0:
            print('face detected')
            color = (255, 255, 255)  # 白
            for rect in facerect:
                # 生成检测到的面部周围的矩形
                #cv2.rectangle(frame, tuple(rect[0:2]), tuple(rect[0:2] + rect[2:4]), color, thickness=2)

                x, y = rect[0:2]
                width, height = rect[2:4]
                image = frame[y - 10: y + height, x: x + width]

                result = model.predict(image)
                if result == 0:  # boss
                    print('Boss is approaching')
                    show_image()
                else:
                    print('Not boss')

        #10msec等待输入键
        k = cv2.waitKey(100)
        #Esc按下按键后结束
        if k == 27:
            break

    #结束捕获
    cap.release()
    cv2.destroyAllWindows()