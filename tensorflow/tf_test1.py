import tensorflow as tf
import numpy as np
import tensorflow_study.input_data as id

sess = tf.Session()
sum = tf.reduce_sum([1, 2, 3, 4, 5])
mean = tf.reduce_mean([1, 2, 3, 4, 5])
mean = tf.reduce_mean([[[1, 1], [2, 2]], [[3, 3], [4, 4]]], [1, 2])

print(sess.run(sum))
print(sess.run(mean))
arr0 = [[1, 2, 3, 4, 5], [9, 8, 7, 6, 5], [555, 444, 333, 222, 111]]
print(sess.run(tf.shape(arr0)))
print(sess.run(tf.argmax(arr0, 1)))
print(sess.run(tf.argmax([1, 2, 3, 4, 5])))
print(sess.run(tf.one_hot(1, 10)))

sess.close()

a1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
labels = id.dense_to_one_hot(a1)
print(labels)


def dense_to_one_hot(labels_dense, num_classes=10):
    num_labels = labels_dense.shape[0]
    print(num_labels)
    index_offset = np.arange(num_labels) * num_classes
    print(index_offset)
    labels_one_hot = np.zeros((num_labels, num_classes))
    labels_one_hot.flat[index_offset + labels_dense.ravel()] = 1
    return labels_one_hot


a2 = np.array([3, 4, 6])
print(dense_to_one_hot(a2))

a3 = np.array([0, 10, 20])
print(a3 + a2.ravel())

a4 = np.array(range(100))
a4.flat[[10, 20, 30, 40, 50]] = 1
print(a4)
