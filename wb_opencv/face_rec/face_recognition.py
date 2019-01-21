#!/usr/bin/env python

import os
import sys
import cv2
import numpy as np

def normalize(X, low, high, dtype=None):
    """Normalizes a given array in X to a value between low and high."""
    X = np.asarray(X)
    minX, maxX = np.min(X), np.max(X)
    # normalize to [0...1].
    X = X - float(minX)
    X = X / float((maxX - minX))
    # scale to [low...high].
    X = X * (high-low)
    X = X + low
    if dtype is None:
        return np.asarray(X)
    return np.asarray(X, dtype=dtype)


def read_images(path, sz=None):
    """Reads the images in a given folder, resizes images on the fly if size is given.
    Args:
        path: Path to a folder with subfolders representing the subjects (persons).
        sz: A tuple with the size Resizes
    Returns:
        A list [X,y]
            X: The images, which is a Python list of numpy arrays.
            y: The corresponding labels (the unique number of the subject, person) in a Python list.
    """
    c = 0
    X,y = [], []
    for dirname, dirnames, filenames in os.walk(path):
        for subdirname in dirnames:
            subject_path = os.path.join(dirname, subdirname)
            for filename in os.listdir(subject_path):
                try:
                    if (filename == ".directory"):
                        continue
                    filepath = os.path.join(subject_path, filename)
                    im = cv2.imread(os.path.join(subject_path, filename), cv2.IMREAD_GRAYSCALE)
                    if (im is None):
                        print("image " + filepath + " is none")
                    # resize to given size (if given)
                    if (sz is not None):
                        im = cv2.resize(im, sz)
                    X.append(np.asarray(im, dtype=np.uint8))
                    y.append(c)
                except IOError as e:
                    print("I/O error({0}): {1}".format(e))
                except:
                    print("Unexpected error:", sys.exc_info()[0])
                    raise
            c = c+1
    return [X, y]
if __name__ == "__main__":
    names=['joe','jim','tom']
    filepath='./data/at/jm/'
    # Now read in the image data. This must be a valid path!
    [X,y] = read_images(filepath)
    # Convert labels to 32bit integers. This is a workaround for 64bit machines,
    # because the labels will truncated else. This will be fixed in code as
    # soon as possible, so Python users don't need to know about this.
    # Thanks to Leo Dirac for reporting:
    y = np.asarray(y, dtype=np.int32)
    # If a out_dir is given, set it:
    if len(sys.argv) == 3:
        out_dir = sys.argv[2]
    # Create the Eigenfaces model. We are going to use the default
    # parameters for this simple example, please read the documentation
    # for thresholding:
    model = cv2.face.createEigenFaceRecognizer()
    # Read
    # Learn the model. Remember our function returns Python lists,
    # so we use np.asarray to turn them into NumPy lists to make
    # the OpenCV wrapper happy:
    model.train(np.asarray(X), np.asarray(y))

    face_cascade = cv2.CascadeClassifier('../cascades/haarcascade_frontalface_default.xml')
    camera = cv2.VideoCapture(0)
    while (True):
        read, img = camera.read()
        faces = face_cascade.detectMultiScale(img, 1.3, 5)
        for (x, y, w, h) in faces:
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            roi = gray[x: x + w, y: y + h]
            try:
                # 选出感兴趣的区域，使用内插法，还是老规矩自行百度
                roi = cv2.resize(roi, (200, 200), interpolation=cv2.INTER_LINEAR)
                # 预测实时图片
                params = model.predict(roi)
                # 把匹配的特征和置信度打印在IDLE内
                print("Label: %s, Confidence: %.2f" % (params[0], params[1]))
                # 把匹配的名字显示在方框左上角，有时候会瞎显示，以后研究，还有就是现在无法显示中文字符，也以后吧 :P
                cv2.putText(img, names[params[0]], (x, y - 20),cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 2)
            except:
                continue
            cv2.imshow("camera", img)
            if cv2.waitKey(1000 / 12) & 0xff == ord("q"):
                break
            cv2.destroyAllWindows()
