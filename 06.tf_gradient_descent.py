# -*- coding: utf-8 -*-
"""
Program: Gradient Descent
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

# %% Gradient Descent 

optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)

# %% Variable Initializer

init = tf.global_variables_initializer()

# %% Session execution (Launch and close the graph)

sess = tf.Session()

sess.run(init)

for i in range (1000):
    sess.run(train,{x: [1,2,3,4], y:[0, -1, -2, -3]})

print(sess.run([w,b]))