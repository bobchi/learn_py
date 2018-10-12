from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from sklearn import neighbors
import matplotlib.pyplot as plt

# # 样本数据，矩阵格式，也可以使多维向量
# x = [[0], [1], [2], [3]]
# # 分类标签
# y = ['兔兔', '妈妈', '爸爸', '爷爷']
# # 选取多少个最近邻
# n = KNeighborsClassifier(n_neighbors=3)
# # 开始训练
# n.fit(x, y)
# print(n.predict([[2.1]]))

# 生成一个2x4的数组
x_y1 = np.random.randint(10, 20, size=(2, 4))
# 生成另外一个样本
x_y2 = np.random.randint(15, 25, size=(2, 4))

# 生成散点图
plt.scatter(x_y1[0], x_y1[1], c='r')
plt.scatter(x_y2[0], x_y2[1], c='b')
# plt.show()
# zip 函数把向量中的数字两两对应合并成多个元祖 如[(10, 13), (15, 19), (10, 11), (17, 18)]
x1 = list(zip(x_y1[0], x_y1[1]))
x2 = list(zip(x_y2[0], x_y2[1]))
print(x1)
print(x2)
# concatenate 函数把数组转换为二维向量
fit_x = np.concatenate((x1, x2))
# 生成取值样本共16个
fit_label = ['兔兔', '妈妈', '爸爸', '爷爷'] * 2
# 设置邻近值为4
n_ret = neighbors.KNeighborsClassifier(n_neighbors=4)
# 加入数据开始运算
n_ret.fit(fit_x, fit_label)
# 任意设置一个坐标点，预测最近样本
print(n_ret.predict([[5, 14]]))

# 在坐标中标出样本
plt.scatter([15], [12], c='g')
plt.show()
# print((x1, x2))
# print(fit_x)

