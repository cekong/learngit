''''''
'''
如何在Keras中保存已经训练好的模型
https://blog.csdn.net/baimafujinji/article/details/42110831
Keras实例--实现手写数字识别 
https://blog.csdn.net/baimafujinji/article/details/78385745
'''

import numpy as np
import random
import keras
import matplotlib.pyplot as plt
from skimage import io,transform

from keras.datasets import mnist
from keras.models import Sequential, Model,load_model
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import RMSprop
from keras.utils import np_utils
from keras.preprocessing.image import load_img,img_to_array

(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train = X_train.reshape(X_train.shape[0], -1)  # 等价于X_train = X_train.reshape(60000,784)
X_test = X_test.reshape(X_test.shape[0], -1)  # 等价于X_test = X_test.reshape(10000,784)
X_train = X_train.astype("float32")
X_test = X_test.astype("float32")
X_train /= 255
X_test /= 255

# 把原来0~9这样的标签，变成长度为10的one-hot向量表示。
y_train = np_utils.to_categorical(y_train, num_classes=10)
y_test = np_utils.to_categorical(y_test, num_classes=10)

def train():
    model = Sequential()
    model.add(Dense(512, input_shape=(784,)))
    model.add(Activation('relu'))
    model.add(Dropout(0.2))
    model.add(Dense(512))
    model.add(Activation('relu'))
    model.add(Dropout(0.2))
    model.add(Dense(10))
    model.add(Activation('softmax'))

    model.summary()

    rmsprop = RMSprop(lr=0.001, rho=0.9, epsilon=1e-08, decay=0.0)

    # metrics means you want to get more results during the training process
    model.compile(optimizer=rmsprop,
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

    history = model.fit(X_train, y_train, epochs=10, batch_size=128,
                       verbose = 1, validation_data=[X_test, y_test])

    score = model.evaluate(X_test, y_test, verbose = 0)
    print('Test score:', score[0])
    print('Test accuracy:', score[1])
    model.save('fei_model.h5')
    return model

def predict(model): #
    X_test_0 = X_test[0,:].reshape(1,784)
    y_test_0 = y_test[0,:]
    plt.imshow(X_test_0.reshape([28,28]))
    plt.show()

    pred = model.predict(X_test_0[:])
    print('Label of testing sample:\n', np.argmax(y_test_0))
    print('Output of the softmax layer:\n', pred[0])
    print('Network prediction:\n', np.argmax([pred[0]]))


if __name__ == '__main__':
    # my_model=train()
    my_model = load_model('/home/deepl/Documents/wb/my_tf_caffe/my_keras/fei_model.h5')
    predict(my_model)

    # test_image = io.imread('/home/deepl/Documents/wb/my_tf_caffe/my_keras/9.jpg', as_grey=True)
    # test_x = transform.resize(test_image, (28, 28), mode='constant')
    # plt.imshow(test_x)
    # plt.show()
    # test_x = test_x.reshape(1,784)
    #
    # pred = my_model.predict(test_x[:])
    # print('Output of the softmax layer:\n', pred[0])
    # print('Network prediction:\n', np.argmax([pred[0]]))
