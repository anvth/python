import pandas as pd
import numpy as np
import tensorflow as tf

# step 1 load data
data_frame = pd.read_csv('tensorflow_classification.csv') #dataframe
# remove unwanted columns
data_frame = data_frame.drop(['index', 'price', 'sq_price'], axis=1)
# select first 10 rows as data set
data_frame = data_frame[0:10]

# step 2 - add labels
# 1 is good buy and 0 is bad buy
data_frame.loc[:, ('y1')] = [1, 1, 1, 0, 0, 1, 0, 1, 1, 1]
# y2 is a negation of y1
data_frame.loc[:, ('y2')] = data_frame['y1'] == 0
# turn TRUE/FALSE values to 1s and 0s
data_frame.loc[:, ('y2')] = data_frame['y2'].astype(int)

print(data_frame)

# step 3 - prepare data for tensorflow (tensors)
# tensors are generic version of vectors and matrices
# vector - is a list of numbers (1D Tensor)
# matrix - is a list of numbers (2D Tensor)
# list of list of list of numbers (3D Tensor)
# ...
# convertfeatures to input tensor
inputX = data_frame.loc[:, ['area', 'bathrooms']].as_matrix()
# convert labels to input tensors
inputY = data_frame.loc[:, ['y1', 'y2']].as_matrix()

# step 4 - write out hyperparameters
learning_rate = 0.000001
training_epochs = 2000
display_steps = 50
n_samples = inputY.size

# step 5 - Create our computational graph/ neural network
# 
x = tf.placeholder(tf.float32, [None, 2])

# create weights
# 2X2 float matrix, that'll keep updating through the 
# trainging process
# variables in tf hold and update parameters
# in memory buffers containing tensors
w = tf.Variable(tf.zeros([2, 2]))

# add biases
# example is b in y = mx + b
b = tf.Variable(tf.zeros([2]))

# multiply our weights by our inputs, first calculation
# weights are how we govern how data flow in our computation graph
# multiply input by weights and add biases
y_value = tf.add(tf.matmul(x, w), b)

# apply softmax to the value we just created
# softmax is the activation function
y = tf.nn.softmax(y_value)

# feed in matrix of labels
y_ = tf.placeholder(tf.float32, [None, 2])

# Step 6 - perform training
# create cost function, mean squared error
# reduce sum, computes the sum of elements across dimensions of a tensor
cost = tf.reduce_sum(tf.pow(y_ - y, 2))/(2*n_samples)
# Gradient descent
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

# Initialize variables and tensorflow session
init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)

# training loop
for i in range(training_epochs):
	sess.run(optimizer, feed_dict={x: inputX, y_: inputY})

	# write out logs of training
	if (i) % display_steps == 0:
		cc = sess.run(cost, feed_dict={x: inputX, y_: inputY})
		print("Training step:", "%04d" % (i), "cost=", "{:.9f}".format(cc))

print("Optimization Finished")
training_cost = sess.run(cost, feed_dict={x: inputX, y_: inputY})
print("Training cost=", training_cost, "w=", sess.run(w), "b=", sess.run(b), '\n')

sess.run(y, feed_dict={x: inputX})