import pandas as pd
import numpy as np

s = pd.Series(['tutu', 'pangzi', 'bao'], index=['girl', 'mother', 'father'])
d = pd.Series({'girl': 'tutu', 'mama': 'pangzi', 'baba': 'bao'})
r = pd.Series([x for x in range(0, 10)])

rand = pd.Series(pd.np.random.rand(5))  # 生成5个随机数0-1之间
ran = pd.Series(pd.np.random.randint(0, high=20, size=10))  # 从0到20生成10个随机数
ran = ran.sort_values(ascending=False)  # 倒排序
# print(ran[ran >= 6])
# print(ran)
# print(ran*2)  #
q = ['特等奖', '一等奖', '二等奖', '三等奖', '谢谢惠顾']
q = np.random.choice(q, size=10, p=[0.05, 0.15, 0.2, 0.3, 0.3])
# print(q)
ser = pd.Series(q)
print(ser.to_json())
