import numpy as np


class Network(object):
    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x)
                        for x, y in zip(sizes[:-1], sizes[1:])]

    def sigmoid(z):
        return 1.0/(1.0+np.exp(-z))

    def feedforward(self, a):
        for b, w in zip(self.biases, self.weights):
            a = self.sigmoid(np.dot(w, a) + b)


a = [2, 3, 1]
net = Network(a)
print(net.biases)
print(net.weights)

b = zip(a[:-1], a[1:])
print('b={}'.format(b))
for x, y in b:
    print('x={}, y={}'.format(x, y))

for x, y in zip(a[:-1], a[1:]):
    print('x={}, y={}'.format(x, y))
