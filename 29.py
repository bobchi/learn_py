from scipy.spatial.distance import cdist
import numpy as np

user1 = np.array([[500, 2000]])
user2 = np.array([[300, 1000]])

# 欧氏距离 两点间的直线距离，采用勾股定理来计算，结果有浮点数，消耗性能
print(cdist(user1, user2, 'euclidean'))

# 曼哈顿距离 两点间直角夹角后两条直线距离之和

