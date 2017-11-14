#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :11/2/17 11:20 AM
# @Author:rsong


import os

import tensorflow as tf
from tensorflow.python import debug as tf_debug

W = tf.Variable(tf.zeros([4, 3]), name="weights")
b = tf.Variable(tf.zeros([3], name="bias"))


# print(os.path.dirname(__file__) + os.sep )

def combine_inputs(X):
    return tf.matmul(X, W) + b


def inference(X):
    return tf.nn.softmax(combine_inputs(X))


def loss(X, Y):
    return tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(logits=combine_inputs(X), labels=Y))


def read_csv(batch_size, file_name, record_defaults):
    filename_queue = tf.train.string_input_producer([os.path.dirname(__file__) + os.sep + file_name])
    reader = tf.TextLineReader()
    key, value = reader.read(filename_queue)
    decoded = tf.decode_csv(value, record_defaults=record_defaults)  # 将一行转成张量列表
    return tf.train.shuffle_batch(decoded, batch_size=batch_size, capacity=batch_size * 50,
                                  min_after_dequeue=batch_size)


def inputs():
    sepal_length, sepal_width, petal_length, petal_width, label = read_csv(100, "bezdekIris.data",
                                                                           [[0.0], [0.0], [0.0], [0.0], [""]])
    label_number = tf.to_int32(tf.argmax(tf.to_int32(tf.stack(
        [tf.equal(label, ["Iris-setosa"]), tf.equal(label, ["Iris-versicolor"]), tf.equal(label, ["Iris-virginica"])])),
        0))
    features = tf.transpose(tf.stack([sepal_length, sepal_width, petal_length, petal_width]))
    return features, label_number


def train(total_loss):
    learning_rate = 0.01
    return tf.train.GradientDescentOptimizer(learning_rate).minimize(total_loss)


def evaluate(sess, X, Y):
    predicted = tf.cast(tf.argmax(inference(X), 1), tf.int32)
    print(sess.run(tf.reduce_mean(tf.cast(tf.equal(predicted, Y), tf.float32))))


sess = tf.InteractiveSession()
init_op = tf.group(tf.global_variables_initializer(), tf.local_variables_initializer())
sess.run(init_op)
X, Y = inputs()
# sess=tf_debug.LocalCLIDebugWrapperSession()
total_loss = loss(X, Y)
train_op = train(total_loss)
coord = tf.train.Coordinator()
threads = tf.train.start_queue_runners(sess=sess, coord=coord)
trainning_steps = 1000
try:
    for step in range(trainning_steps):
        if coord.should_stop():
            break
        sess.run(train_op)
        if step % 10 == 0:
            print("loss: ", sess.run([total_loss]))
except Exception as e:
   # Report exceptions to the coordinator.
   coord.request_stop(e)

evaluate(sess, X, Y)
coord.request_stop()
coord.join(threads)
sess.close()
