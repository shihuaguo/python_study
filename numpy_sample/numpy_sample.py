import numpy as np

#从list创建array
list_a = [1, 2, 3, 4]
array = np.array(list_a)
print("array.shape={0}, size={1}, ndim={2}, dtype={3}".format(array.shape, array.size, array.ndim, array.dtype))

#创建N维数组
m_10_10_1 = np.ones([10, 10])
m_10_10_0 = np.zeros([10, 10])
m_diag_10 = np.eye(10)
print("m_10_10_1=\n{0}\nm_10_10_0=\n{1}\nm_diag_10=\n{2}".format(m_10_10_1,m_10_10_0,m_diag_10));

#创建随机数组
array_rand_10 = np.random.rand(10, 10)
print(array_rand_10)

random_f_0_100 = np.random.uniform(0, 100)
print(random_f_0_100)

random_i_0_100 = np.random.randint(0, 100)
print(random_i_0_100)

#matrix multiply
m_3_2 = np.ones([3,2])
m_2_1 = np.random.rand(2,1)
m_3_1 = np.dot(m_3_2, m_2_1)
print(m_3_1)
