import tensorflow as tf
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '0'  # You need to tell CUDA
# which GPU you'd like to use. if you have one GPU probably your GPU is '0'
with tf.device('/gpu:0'):
    a = tf.constant([1.0, 2.0, 3.0, 4.0], shape=[2, 2], name='a')
    b = tf.constant([4.0, 3.0, 2.0, 1.0], shape=[2, 2], name='b')
    c = tf.matmul(a, b)
with tf.compat.v1.Session() as sess:
    print(sess.run(c))
