# -*- coding: utf-8 -*-
"""
Program - TensorFlow with constant

"""

import tensorflow as tf

# %% Create Node (constant)

node1 = tf.constant(3.0, tf.float32)
node2 = tf.constant(4.0, tf.float32)

print(node1,node2)

# %% Session execution (Launch and close the graph)

sess = tf.Session() # Launch the graph and create a session object
print(sess.run([node1, node2])) # Execution
sess.close() # Close the sesison and free-up the memory

# %% Another way to lauch and close the graph (Session)

with tf.Session() as sess:
    output = sess.run([node1, node2])
    print(output)
    
    
    
    
    