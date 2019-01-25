import tensorflow as tf
import numpy as np
"""
https://www.cnblogs.com/minsons/p/7866618.html
"""



def one_hot_matrix(labels, C):
    depth = tf.constant(value=C, name='C')
    one_hot_matrix = tf.one_hot(labels, depth, axis=0)
    sess = tf.Session()

    one_hot = sess.run(one_hot_matrix)
    sess.close()
    return one_hot

labels = np.array([1,2,3,0,2,1])
one_hot = one_hot_matrix(labels, C = 4)
print ("one_hot = \n" + str(one_hot))