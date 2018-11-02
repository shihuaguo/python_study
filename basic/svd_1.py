from numpy import arange,array
from numpy import reshape
from numpy import diag
from numpy import zeros
from scipy.linalg import svd,pinv

#import numpy as np;

A = arange(1,7)
print(A)
A = reshape(A,(3,-1))
print(A)

#计算SVD
U,s,V = svd(A)
print(U)
print(s)
print(V)

#根据svd重建矩阵
sigma = zeros(A.shape)
sigma[:A.shape[1],:A.shape[1]] = diag(s);
B = U.dot(sigma.dot(V))
print(B)

#计算伪逆
A = array([
    [0.1, 0.2],
    [0.3, 0.4],
    [0.5, 0.6],
    [0.7, 0.8]
])
B = pinv(A);
print(B)

#通过svd计算伪逆 A+ = V^T . D+ . U^T
U, s, V = svd(A)
d = 1.0/s
D = zeros(A.shape)
D[:D.shape[1], :D.shape[1]] = diag(d)
B = V.T.dot(D.T).dot(U.T)
print(B)
