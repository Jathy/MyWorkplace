# utf-8
# python2.7
# tensorflow 1.01

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# data
mnist = input_data.read_data_sets('MNIST_data', one_hot = True)

# hyperparameters
learningRate = 0.001
trainingIters = 100000
batchSize = 128
displayStep = 10

nInputs = 28 # MNIST data input(img shape: 28x28)
nSteps = 28 # time steps
nHiddenUnis = 128 #neurons in hidden layer
nClasses = 10 # MNIST classes(0-9 digits)

# tf Graph input
x = tf.placeholder(tf.float32, [None, nSteps, nInputs])
y = tf.placeholder(tf.float32, [None, nClasses])

# Define weights
Weights = {
        #(28, 128)
        'in':tf.Variable(tf.random_normal([nInputs, nHiddenUnis])),
        #(128, 10)
        'out':tf.Variable(tf.random_normal([nHiddenUnis, nClasses]))
        }
# Define biases
biases = {
        #(128, )
        'in':tf.Variable(tf.constant(0.1, shape=[nHiddenUnis, ])),
        #(10, )
        'out':tf.Variable(tf.constant(0.1, shape=[nClasses, ]))
        }

def RNN(X, Weights, biases):
    #----------hidden layer for input to cell -----------#
    # X(128 batch, 28 steps, 28 inputs) 
    # ==>(128*28, 28 inputs)
    X = tf.reshape(X, [-1, nInputs])
    # X_in ==> (128batch*28steps, 128hidden)
    X_in = tf.matmul(X, Weights['in']) + biases['in']
    # X_in ==> (128, 28steps, 128hidden)
    X_in = tf.reshape(X_in, [-1, nSteps, nHiddenUnis])

    #--------------------- cell -------------------------#
    # basic LSTM Cell:
    if int((tf.__version__).split('.')[1]<12 and int((tf.__version__).split('.')[0])<1):     
        lstmCell = tf.nn.rnn.cell.BasicLSTMCell(nHiddenUnis, forget_bias=1.0, state_is_tuple=True)   
    else:
        lstmCell = tf.contrib.rnn.BasicLSTMCell(nHiddenUnis)
    
    # lstm cell is divided into two parts(c_state, m_state)
    initState = lstmCell.zero_state(batchSize, dtype=tf.float32)
    
    # You have 2 options for following step:
    # 1.tf.nn.rnn(cell, inputs)
    # 2.tf.nn.dynamic_rnn(cell, inputs)
    # if use option 1, you have to modified the shape of X_in
    # In here, we go for option 2 
    # dynamic_rcc receiver Tensor( batch, stpes, inputs ) or ( steps, batch, inputs ) as X_in
    # make sure the time_major is changed accordingly
    outputs, final_states = tf.nn.dynamic_rnn(lstmCell, X_in, initial_state=initState, time_major=False)

    #----hidden layer for output as the final result-----#
#    results = tf.matmul(final_states[1], Weights['out']) + biases['out']
    
    # or
    # unpakc to list[(batch, outputs)..]*steps     
    if int((tf.__version__).split('.')[1]<12 and int((tf.__version__).split('.')[0])<1):     
        outputs = tf.unpack(tf.transpose(outputs, [1,0,2]))
    else:
        outputs = tf.unstack(tf.transpose(outputs, [1,0,2])) # state is the last outputs
    results = tf.matmul(outputs[-1], Weights['out']) + biases['out']
    
    return results

prediction = RNN(x, Weights, biases)
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=prediction, labels=y))
train_op = tf.train.AdamOptimizer(learningRate).minimize(cost)

correct_prediction = tf.equal(tf.argmax(prediction, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    step = 0
    while step * batchSize < trainingIters:
        batch_xs, batch_ys = mnist.train.next_batch(batchSize)
        batch_xs = batch_xs.reshape(batchSize, nSteps, nInputs)
        sess.run([train_op], feed_dict={x:batch_xs, y:batch_ys})
        if step % 20 == 0:
            print sess.run(accuracy, feed_dict={x:batch_xs, y:batch_ys})
        step += 1


