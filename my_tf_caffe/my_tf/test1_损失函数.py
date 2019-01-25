import tensorflow as tf
import numpy as np
"""
https://www.cnblogs.com/minsons/p/7866618.html
"""


def sigmoid(z):
    x = tf.placeholder(tf.float32,name = 'x')
    sigmoid = tf.sigmoid(x)

    with tf.Session() as sess:
        result = sess.run(sigmoid,feed_dict = {x:z})

    return result



def cost(logits,labels):
    z = tf.placeholder(tf.float32,name='z')
    y= tf.placeholder(tf.float32,name='y')
    costvalue = tf.nn.sigmoid_cross_entropy_with_logits(logits=z, labels=y)
    with tf.Session() as sess:
        costvalue = sess.run(costvalue,feed_dict = {z:logits,y:labels})
    return costvalue

#测试
logits = sigmoid(np.array([0.2,0.4,0.7,0.9]))
costvalue = cost(logits, np.array([0,0,1,1]))
print ("cost = " + str(costvalue))