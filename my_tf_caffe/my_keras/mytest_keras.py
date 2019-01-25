''''''
'''
 https://www.imooc.com/learn/843 
https://blog.csdn.net/baimafujinji/article/details/78385745
https://blog.csdn.net/baimafujinji/article/details/80705578
'''
import numpy as np
from keras.models import Sequential
from keras.layers import Dense,Activation
from keras.optimizers import SGD
from sklearn.datasets import load_iris
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
def main():
    iris=load_iris()
    print(iris["target"])
    print(LabelBinarizer().fit_transform(iris["target"]))
    x_train, x_test, y_train, y_test = train_test_split(
            iris.data, iris.target, test_size=0.3,random_state=1)
    labels_train=LabelBinarizer().fit_transform(y_train)
    labels_test=LabelBinarizer().fit_transform(y_test)

    model=Sequential(
        [
            Dense(5,input_dim=4),
            Activation("relu"),
            Dense(3),
            Activation("sigmoid")
        ]
    )
    sgd=SGD(lr=0.01,decay=1e-6,momentum=0.9,nesterov=True)
    model.compile(optimizer=sgd,loss="categorical_crossentropy")
    history=model.fit(x_train,labels_train,epochs=200,batch_size=40)
    print(model.predict_classes(x_test))
    print(y_test)
    # score=model.evaluate(x_test,labels_test,verbose = 0)
    # print(score)
    model.save_weights("./data/w")
    model.load_weights("./data/w")
    print(history.params)  #模型中设定的参数
if __name__ == '__main__':
    main()
