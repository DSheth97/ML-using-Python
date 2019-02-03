# -*- coding: utf-8 -*-
"""
Program: Visulization of TensorFlow graph
"""

import tensorflow as tf

# %% Tensor creation - Create Node (constant)

a = tf.constant(3.0, tf.float32)
b = tf.constant(4.0, tf.float32)

c = a * b
# %% Session execution (Launch and close the graph)

sess = tf.Session() # Launch the graph and create a session object

fileWriter = tf.summary.FileWriter('graph', sess.graph)

print(sess.run(c)) # Execution
sess.close() # Close the sesison and free-up the memory