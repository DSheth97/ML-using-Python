# -*- coding: utf-8 -*-
"""
Program: TensorFlow placeholder.
"""

import tensorflow as tf

# %% Create Tensor - Placeholder

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)

add = a + b

# %% Session execution (Launch and close the graph)

sess = tf.Session()

print(sess.run(add, {a: [10,3], b: [20,40]}))