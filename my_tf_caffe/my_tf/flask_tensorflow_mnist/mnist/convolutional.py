import tensorflow as tf
import os
from flask_tensorflow_mnist.mnist import module
from tensorflow.examples.tutorials.mnist import input_data

data=input_data.read_data_sets("/home/deepl/Documents/wb/MNIST_DATA/", False, one_hot=True)

# 定义模型
with tf.variable_scope("convolutional"):
    x = tf.placeholder(tf.float32, [None, 784], name="x")
    keep_prob = tf.placeholder(tf.float32)
    y, variables = module.convolutional(x, keep_prob)




# 训练
y2 = tf.placeholder(dtype=tf.float32, shape=[None, 10], name='y2')
#交叉熵
cross_entropy = -tf.reduce_sum(y2 * tf.log(y))
#Adam算法的优化器
learning_rate = 1e-4
train_step = tf.train.AdamOptimizer(learning_rate).minimize(cross_entropy)
# 预测
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y2, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))



saver = tf.train.Saver(variables)

with tf.Session() as sess:
    #可视化
    merged_summary_op = tf.summary.merge_all()
    summary_writer = tf.summary.FileWriter('mnist_log/1', sess.graph)
    summary_writer.add_graph(sess.graph)

    sess.run(tf.initialize_all_variables())

    # 断点续训
    ckpt = tf.train.get_checkpoint_state(
        os.path.join(os.path.dirname(__file__), 'data', 'convalution.ckpt'))
    if ckpt and ckpt.model_checkpoint_path:
        saver.restore(sess, ckpt.model_checkpoint_path)

    for i in range(2000):
        batch = data.train.next_batch(50)
        if i % 100 == 0:
            train_accuracy = accuracy.eval(feed_dict={
                x: batch[0],
                y2: batch[1],
                keep_prob: 1.0
            })
            print("setp %d, train accuracy=%g" % (i, train_accuracy))
        sess.run(
            train_step, feed_dict={
                x: batch[0],
                y2: batch[1],
                keep_prob: 0.5
            })
    print(
        sess.run(
            accuracy,
            feed_dict={
                x: data.test.images,
                y2: data.test.labels,
                keep_prob: 1.0
            }))
    path = saver.save(
        sess,
        os.path.join(
            os.path.dirname(__file__), 'data', 'convalution.ckpt'),
        write_meta_graph=False,
        write_state=False)

print("Saved:", path)