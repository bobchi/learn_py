import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

if __name__ == '__main__':
    # 将csv数据读取为pandas对象
    fund = pd.read_csv('./csv/001112.csv', dtype={'fcode': str})
    # 转化时间字符串为时间
    fund['fdate'] = pd.to_datetime(fund['fdate'])
    # 设置时间列为索引，并升序排列
    fund = fund.set_index('fdate').sort_index(ascending=False)
    # x轴为数据2017后的索引 y为2017后的NAV
    x = fund.loc['2017'].index
    y = fund.loc['2017']['NAV']
    # 将xy数据转化为矩阵:
    # 将时间转化为时间戳
    x = x.astype(np.int64)
    # 将时间戳转化为1列多行的二维数组
    x = x.values.reshape(-1, 1)
    y = y.values.reshape(-1, 1)

    # 放入数据开始训练
    lr = LinearRegression()
    lr.fit(x, y)
    # 构建一个时间戳，来预测y轴的值
    test_x = pd.to_datetime(np.array(['2017-9-30', '2017-10-1'])).astype(np.int64).values.reshape(-1, 1)
    # 预测到Y轴的值 [[1.41483561]
    #  [1.41626252]]
    new_y = lr.predict(test_x)
    # 把拟合线画出来：如果y为训练预测出的值，则线条为直线拟合线
    x_date = fund.loc['2017'].index
    # 走势点图
    plt.scatter(x_date, fund.loc['2017']['NAV'])
    plt.plot(x_date, lr.predict(x), 'r')
    plt.show()
    print(new_y)


