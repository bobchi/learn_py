import matplotlib.pyplot as plt
import numpy as np

# 创建两个数直接的数列
# x = np.arange(2, 15)
# y = x**2

# 创建一个等差数列，默认50个。endpoint=False不包含后一位, num=20控制样本数量
# x = np.linspace(1, 10, endpoint=False, num=20)
x = np.linspace(1, 10)
y = x**2
# print(x)
plt.plot(x, y)
plt.show()
