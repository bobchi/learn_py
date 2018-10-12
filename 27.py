from sklearn.metrics.pairwise import euclidean_distances
from scipy.spatial.distance import cdist
import numpy as np

fl = np.array([-10, 5, 20, 15, 30])

# 手动标准差计算
print(np.sqrt(((fl - fl.mean())**2).sum()/fl.size))
# 直接使用numpy内置方法
print(fl.std())
# 13.638181696985855

# 例如一个基金，计算出的标准差越小，理论上说明收益约稳定

# 消费能力计算 标准化的欧氏距离
u1 = np.array([[500, 2000, 1020,10000,890,500]])
u2 = np.array([[300, 1000, 600,3000,600,300]])
print(euclidean_distances(u1, u2))
print(cdist(u1, u2, 'seuclidean'))

