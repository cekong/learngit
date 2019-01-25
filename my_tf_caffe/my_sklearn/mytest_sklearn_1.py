import numpy as npy
from sklearn import linear_model, datasets
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score, classification_report

iris = datasets.load_iris()
X = iris.data[:, :2]  # we only take the first two features.
Y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
logreg = linear_model.LogisticRegression(C=1e5,solver='lbfgs', multi_class='multinomial')
logreg.fit(X_train, y_train)

prediction = logreg.predict(X_test)
print("accuracy score: ")
print(accuracy_score(y_test, prediction))
print(classification_report(y_test, prediction))

logreg_proba = logreg.predict_proba(X_test)
logreg_pred = logreg.predict(X_test)
for index in range (5):
    print(logreg_proba[index])
    print("Predict label:", logreg_pred[index])
    print("Correct label:", y_test[index])
'''
predict_proba返回的是一个 n 行 k 列的数组，
 第 i 行 第 j 列上的数值是模型预测 第 i 个预测样本为某个标签的概率，
 并且每一行的概率和为1。
'''