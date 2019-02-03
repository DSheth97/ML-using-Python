# -*- coding: utf-8 -*-
"""
Program: Linear model using TensorFlow Variable
"""

import tensorflow as tf

# %% Create Tensor - Variable

w = tf.Variable([0.3],tf.float32)    # W = -1
b = tf.Variable([-0.3],tf.float32)   # b = 1

x = tf.placeholder(tf.float32) # Input

linear_model = w * x + b # Model output

y = tf.placeholder(tf.float32) # Actual output

# %% Loss Function

squared_Error = tf.square(linear_model - y)
loss = tf.reduce_sum(squared_Error)

# %% Variable Initializer

init = tf.global_variables_initializer()

# %% Session execution (Launch and close the graph)

sess = tf.Session()

sess.run(init)
print(sess.run(loss,{x: [1,2,3,4], y:[0, -1, -2, -3]}))