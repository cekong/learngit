''''''
'''
https://morvanzhou.github.io/tutorials/machine-learning/tensorflow/2-2-example2/#%E6%90%AD%E5%BB%BA%E6%A8%A1%E5%9E%8B
tensorflow 基本结构
1.创建数据
2.搭建模型
3.计算误差
4.传播误差
5.训练

'''

import tensorflow as tf
import numpy as np

# 1.创建数据
# create data
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data*0.1 + 0.3

# 2.搭建模型
Weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
biases = tf.Variable(tf.zeros([1]))

y = Weights*x_data + biases
# 3.计算误差
loss = tf.reduce_mean(tf.square(y-y_data))
# 4.传播误差
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

# 5.训练
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)          # Very important

for step in range(201):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(Weights), sess.run(biases))

sess.close()