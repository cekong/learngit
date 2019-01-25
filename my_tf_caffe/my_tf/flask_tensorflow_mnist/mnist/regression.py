import tensorflow as tf
import os
from flask_tensorflow_mnist.mnist import module
from tensorflow.examples.tutorials.mnist import input_data

data=input_data.read_data_sets("/home/deepl/Documents/wb/MNIST_DATA/", False, one_hot=True)

# create model
with tf.variable_scope("regression"):
    x = tf.placeholder(tf.float32, [None, 784])
    y, variables = module.regression(x)

#train
y1=tf.placeholder('float',[None,10])
#交叉熵
cross_entropy = -tf.reduce_sum(y1 * tf.log(y))
#梯度下降
learning_rate = 0.001
train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(cross_entropy)
# 预测
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y1, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))



saver = tf.train.Saver()
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    # 断点续训
    ckpt = tf.train.get_checkpoint_state(
        os.path.join(os.path.dirname(__file__), 'data', 'regression.ckpt'))
    if ckpt and ckpt.model_checkpoint_path:
        saver.restore(sess, ckpt.model_checkpoint_path)

    for item in range(1000):
        batch_xs, batch_ys = data.train.next_batch(100)
        sess.run(train_step, feed_dict={x: batch_xs, y1: batch_ys})
    print((sess.run(
        accuracy, feed_dict={
            x: data.test.images,
            y1: data.test.labels
        })))
    path = saver.save(
        sess,
        os.path.join(os.path.dirname(__file__), 'data', 'regression.ckpt'),
        write_meta_graph=False,
        write_state=False)
print("Saved:", path)