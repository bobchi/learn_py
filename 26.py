from sklearn.metrics.pairwise import euclidean_distances
import numpy as np

# 欧氏距离 比对各个数据矩阵的差异

users = np.array([[10,15,20],[120,200,150], [12,16,25]])

print(euclidean_distances(users))