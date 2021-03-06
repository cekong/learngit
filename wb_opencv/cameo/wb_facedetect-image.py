import cv2

filename = '/home/deepl/Pictures/wb.jpg'


def detect(filename):
    face_cascade = cv2.CascadeClassifier('../cascades/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('../cascades/haarcascade_eye.xml')
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        roi = gray[ y:y + h,x:x + w]
        eyes=eye_cascade.detectMultiScale(roi,1.3,5,0,(40,40))
        for (ex, ey, ew, eh) in eyes:
            img = cv2.rectangle(img, (x+ex, y+ey), (x+ex + ew, y+ey + eh), (0, 0, 255), 2)
    cv2.namedWindow('Vikings Detected!!')
    cv2.imshow('Vikings Detected!!', img)
    cv2.waitKey(0)
detect(filename)