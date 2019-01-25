import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

sess = tf.InteractiveSession()

"""
/home/deepl/Documents/wb/MNIST_DATA

"""

mnist = input_data.read_data_sets("/home/deepl/Documents/wb/MNIST_DATA/", False, one_hot=True)


x = tf.placeholder("float", [None, 784])

""" y_ 是实际的分布"""
y_ = tf.placeholder("float", [None,10])

""" 权重初始化 """
def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)

def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)

""" 
卷积和池化
卷积使用1步长（stride size），0边距（padding size）的模板，
保证输出和输入是同一个大小
池化用简单传统的2x2大小的模板做max pooling
"""
def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')

def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1],
                        strides=[1, 2, 2, 1], padding='SAME')

""" 第一层卷积 
把x_image和权值向量进行卷积，加上偏置项，
然后应用ReLU激活函数，最后进行max pooling。 
"""
W_conv1 = weight_variable([5, 5, 1, 32])
b_conv1 = bias_variable([32])

x_image = tf.reshape(x, [-1,28,28,1])

h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)
h_pool1 = max_pool_2x2(h_conv1)


""" 第二层卷积 
第二层中，每个5x5的patch会得到64个特征。
"""
W_conv2 = weight_variable([5, 5, 32, 64])
b_conv2 = bias_variable([64])

h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
h_pool2 = max_pool_2x2(h_conv2)


""" 全连接层 
现在，图片尺寸减小到7x7，我们加入一个有1024个神经元的全连接层，
用于处理整个图片。我们把池化层输出的张量reshape成一些向量，
乘上权重矩阵，加上偏置，然后对其使用ReLU。
"""

W_fc1 = weight_variable([7 * 7 * 64, 1024])
b_fc1 = bias_variable([1024])

h_pool2_flat = tf.reshape(h_pool2, [-1, 7*7*64])
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

"""dropout
为了减少过拟合
可以在训练过程中启用dropout，在测试过程中关闭dropout
"""
keep_prob = tf.placeholder("float")
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

"""输出层"""
W_fc2 = weight_variable([1024, 10])
b_fc2 = bias_variable([10])

y_conv=tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)


"""训练和评估模型"""
'''交叉熵'''
cross_entropy = -tf.reduce_sum(y_*tf.log(y_conv))
'''ADAM优化器来做梯度最速下降'''
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
'''检测我们的预测是否真实标签匹配'''
correct_prediction = tf.equal(tf.argmax(y_conv,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
sess.run(tf.initialize_all_variables())
for i in range(20000):
    batch = mnist.train.next_batch(50)
    if i%100 == 0:
        train_accuracy = accuracy.eval(feed_dict={
            x:batch[0], y_: batch[1], keep_prob: 1.0})
        print("step %d, training accuracy %g"%(i, train_accuracy))
    train_step.run(feed_dict={x: batch[0], y_: batch[1], keep_prob: 0.5})

print("test accuracy %g"%accuracy.eval(feed_dict={
    x: mnist.test.images, y_: mnist.test.labels, keep_prob: 1.0}))



