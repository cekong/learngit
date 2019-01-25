
''''''
"""
https://blog.csdn.net/qiqiaiairen/article/details/53184216
http://www.tensorfly.cn/tfdoc/how_tos/variables.html
https://morvanzhou.github.io/tutorials/machine-learning/tensorflow/5-06-save/
"""

import tensorflow as tf
import numpy as np

# Save to file
# remember to define the same dtype and shape when restore
# W = tf.Variable([[1,2,3],[3,4,5]], dtype=tf.float32, name='weights')
# b = tf.Variable([[1,2,3]], dtype=tf.float32, name='biases')
#
# # tf.initialize_all_variables() no long valid from
# # 2017-03-02 if using tensorflow >= 0.12
# if int((tf.__version__).split('.')[1]) < 12 and int((tf.__version__).split('.')[0]) < 1:
#     init = tf.initialize_all_variables()
# else:
#     init = tf.global_variables_initializer()
#
# saver = tf.train.Saver()
#
# with tf.Session() as sess:
#    sess.run(init)
#    save_path = saver.save(sess, "/tmp/save_net.ckpt")
#    print("Save to path: ", save_path)


################################################
# restore variables
# redefine the same shape and same type for your variables
W = tf.Variable(np.arange(6).reshape((2, 3)), dtype=tf.float32, name="weights")
b = tf.Variable(np.arange(3).reshape((1, 3)), dtype=tf.float32, name="biases")

# not need init step

saver = tf.train.Saver()
with tf.Session() as sess:
    saver.restore(sess, "/tmp/save_net.ckpt")
    print("weights:", sess.run(W))
    print("biases:", sess.run(b))


"""恢复变量
当从文件中恢复变量时，不需要事先对它们做初始化。init
"""