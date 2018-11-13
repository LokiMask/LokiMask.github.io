#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :11/2/17 6:39 PM
# @Author:rsong
import tensorflow as tf
import os

# def read_csv(batch_size, file_name, record_defaults):
#     filename_queue = tf.train.string_input_producer([os.path.dirname(__file__) + os.sep + file_name])
#     reader = tf.TextLineReader()
#     key, value = reader.read(filename_queue)
#     decoded = tf.decode_csv(value, record_defaults=record_defaults)#将一行转成张量列表
#     return tf.train.shuffle_batch(decoded, batch_size=batch_size, capacity=batch_size * 50,
#                                   min_after_dequeue=batch_size,allow_smaller_final_batch=True)


# sepal_length, sepal_width, petal_length, petal_width, label =read_csv(100,"iris.data",[[0.0], [0.0], [0.0], [0.0], [""]])
# value=read_csv(100,"iris.data",[[0.0], [0.0], [0.0], [0.0], [""]])
# with tf.Session() as sess:
#     sess.run(value)
filename_queue = tf.train.string_input_producer([os.path.dirname(__file__) + os.sep + "titanic.csv"],shuffle=True)
reader = tf.TextLineReader()
key, value = reader.read(filename_queue)
# decoded = tf.decode_csv(value, record_defaults=[[0.0], [0.0], [0.0], [0.0], [""]])
decoded=tf.decode_csv(value,record_defaults=[[0.0], [0.0], [0], [""], [""], [0.0], [0.0], [0.0], [""], [0.0], [""], [""]])
passenger_id, survived, pclass, name, sex, age, sibsp, parch, ticket, fare, cabin, embarked =tf.train.shuffle_batch(decoded, batch_size=10, capacity=10* 5,min_after_dequeue=10)
# sepal_length, sepal_width, petal_length, petal_width, label=tf.train.shuffle_batch(decoded, batch_size=10, capacity=10* 5,min_after_dequeue=10)
# Create the graph, etc.
init_op = tf.global_variables_initializer()

# Create a session for running operations in the Graph.
sess = tf.Session()

# Initialize the variables (like the epoch counter).
sess.run(init_op)

# Start input enqueue threads.
coord = tf.train.Coordinator()
threads = tf.train.start_queue_runners(sess=sess, coord=coord)
print(passenger_id)
print(passenger_id)
