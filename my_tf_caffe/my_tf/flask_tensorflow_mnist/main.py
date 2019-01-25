import numpy as np
import tensorflow as tf
from flask import Flask, jsonify, render_template, request
from my_tf.flask_tensorflow_mnist.mnist import module as model


x = tf.placeholder("float", [None, 784])
sess = tf.Session()


#传入线性回归模型
with tf.variable_scope("regression"):
    print(model.regression(x))
    y1, variables = model.regression(x)
saver = tf.train.Saver(variables)
regression_file = tf.train.latest_checkpoint("mnist/data/regreesion.ckpt")
if regression_file is not None:
    saver.restore(sess, regression_file)

def regression(input):
    return sess.run(y1, feed_dict={x: input}).flatten().tolist()


#传入卷积模型
with tf.variable_scope("convolutional"):
    keep_prob = tf.placeholder("float")
    y2, variables = model.convolutional(x, keep_prob)
sess.run(tf.global_variables_initializer())
saver = tf.train.Saver(variables)
convolutional_file = tf.train.latest_checkpoint(
    "mnist/data/convolutional.ckpt")
if convolutional_file is not None:
    saver.restore(sess, convolutional_file)

def convolutional(input):
    return sess.run(
        y2, feed_dict={
            x: input,
            keep_prob: 1.0
        }).flatten().tolist()



app = Flask(__name__)
# 路由
@app.route("/api/mnist", methods=['post'])
def mnist():
    input = ((255 - np.array(request.json, dtype=np.uint8)) / 255.0).reshape(1, 784)
    output1 = regression(input)
    output2 = convolutional(input)
    return jsonify(results=[output1, output2])


@app.route("/")
def main():
    return render_template("index.html")

if __name__ == "__main__":
    app.debug = True
    app.run()