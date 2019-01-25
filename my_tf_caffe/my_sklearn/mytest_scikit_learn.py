''''''
'''
https://www.imooc.com/video/14997
https://blog.csdn.net/linxid/article/details/79104130
https://www.cnblogs.com/lianyingteng/p/7811126.html
Sklearn 包含了很多种机器学习的方式:

    Classification 分类
    Regression 回归
    Clustering 非监督分类
    Dimensionality reduction 数据降维
    Model Selection 模型选择
    Preprocessing 数据预处理

'''

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn import metrics



def main():
    iris=load_iris()
    # print(iris)
    '''预处理'''
    #导入数据和标签
    iris_x = iris.data
    iris_y = iris.target

    x_train, x_test, y_train, y_test = train_test_split(
        iris_x, iris_y, test_size=0.3,random_state=1)

    '''建模'''
    clf=tree.DecisionTreeClassifier(criterion="entropy")
    clf.fit(x_train,y_train)  #训练
    y_pred=clf.predict(x_test)   #预测

    '''验证'''
    print(metrics.accuracy_score(y_true=y_test, y_pred=y_pred))

    with open("tree.dot","w") as f:
        tree.export_graphviz(clf,out_file=f)


if __name__ == "__main__":
    main()