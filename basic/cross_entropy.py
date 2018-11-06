import tensorflow as tf
import numpy as np

a1 = [0.5,0.25,0.125,0.125]
#print(a1)
#a1.flat[1] = 1
print(a1)

#a2 = np.zeros(10,np.float32)
a2 = [0.25,0.25,0.25,0.25]
#a2.flat[2] = 1

#计算信息熵
y1 = -tf.reduce_sum(a1*tf.log(a1))
y2 = -tf.reduce_sum(a2*tf.log(a2))

#计算交叉熵
y3 = -tf.reduce_sum(a1*tf.log(a2))
y4 = -tf.reduce_sum(a2*tf.log(a1))

sess = tf.Session()
print(sess.run(y1))
print(sess.run(y2))
print(sess.run(y3))
print(sess.run(y4))
print(sess.run(tf.log(1.,'2')))

sess.close()
