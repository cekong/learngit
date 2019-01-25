import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data


"""
/home/deepl/Documents/wb/MNIST_DATA

softmax回归


"""

mnist = input_data.read_data_sets("/home/deepl/Documents/wb/MNIST_DATA/", False, one_hot=True)


x = tf.placeholder("float", [None, 784])
W = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))

"""y 是我们预测的概率分布"""
y = tf.nn.softmax(tf.matmul(x,W) + b)

""" y_ 是实际的分布"""
y_ = tf.placeholder("float", [None,10])

"""计算交叉熵"""
cross_entropy = -tf.reduce_sum(y_*tf.log(y))
"""用梯度下降算法（gradient descent algorithm）以0.01的学习速率最小化交叉熵"""
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)
"""在一个Session里面启动我们的模型，并且初始化变量"""
init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)
"""
开始训练模型，模型循环训练1000次！
随机梯度下降训练
随机抓取训练数据中的100个批处理数据点
"""
for i in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
"""检测我们的预测是否真实标签匹配"""
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
"""
计算所学习到的模型在测试数据集上面的正确率
为了确定正确预测项的比例，我们可以把布尔值转换成浮点数，然后取平均值。
例如，[True, False, True, True] 会变成 [1,0,1,1] ，取平均值后得到 0.75.
"""
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))