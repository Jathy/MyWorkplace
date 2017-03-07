#utf-8
#python 2.7

import tensoflow as tf

def add_layer(inputs, in_size, out_size, activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size,out_size]))
    biases = tf.Variable(tf.zeros([1,out_size]) + 0.1)
    Wx_pluse_b = tf.matmul(inputs, Weights) + biases
    if activation_function is None:
        outputs = Wx_pluse_b
    else:
        outputs = activation_function(Wx_pluse_b)
    return outputs

    

