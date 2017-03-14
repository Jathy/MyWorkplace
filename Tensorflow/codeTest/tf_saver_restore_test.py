# utf-8
# python2.7

import tensorflow as tf
import numpy as np

# restore variable
# redefine the same dtype and shape for your variables
W = tf.Variable(np.arange(6).reshape((2,3)), dtype=tf.float32, name='Weights')
b = tf.Variable(np.arange(3).reshape((1,3)), dtype=tf.float32, name='biases')

# not need init step
saver = tf.train.Saver()

with tf.Session() as sess:
    saver.restore(sess, "MyNet/SaveNet.ckpt")
    print "Weights:",sess.run(W)
    print "biases:", sess.run(b)
