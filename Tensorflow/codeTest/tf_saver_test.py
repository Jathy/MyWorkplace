# utf-8
# python 2.7

import tensorflow as tf

# Save to file
# Remember to define the same dtype and shape when restore
W = tf.Variable([[1,2,3],[4,5,6]], dtype=tf.float32, name='Weights')
b = tf.Variable([[1,2,3]], dtype=tf.float32, name='biases')

init = tf.global_variables_initializer()

saver = tf.train.Saver()

with tf.Session() as sess:
    sess.run(init)
    save_path = saver.save(sess, "MyNet/SaveNet.ckpt")
    print "Save to path: ", save_path
