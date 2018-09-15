import pandas

pd = pandas.read_csv('../csv/fund.csv', dtype={'编码': pandas.np.str_})  # 读取csv，编码列以字符串输出
ret = pd.sort_values(by='编码', ascending=False)  # NAV列排序，根据倒排序，即降序
ret = ret[['编码', '名称', 'NAV']][0:5].to_csv('./csv/fund_5.csv', encoding='utf-8')  # 指定列指定行数重新生成csv
print(ret)  # 等同于ret[0:4] 从头开始显示4条



