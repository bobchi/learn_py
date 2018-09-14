import pandas

if __name__ == '__main__':
    # 读取表格，让fcode以字符串显示，索引列是fdate
    pd = pandas.read_csv('../csv/004616.csv', dtype={'fcode': pandas.np.str_}, index_col='fdate', parse_dates=['fdate'])
    # print(pd.sort_index)  # 日期降序排列
    # pd.index = pandas.to_datetime(pd.index)
    # print(pd['2017'].sort_index())  # 指定年份升序排列

    # 日增长率不为空及--，并负增长的数据
    ret = pd[pd['DGR'].notnull()]
    ret = ret[ret['DGR'] != '--']
    ret = ret[ret['DGR'].str.strip('%').astype(pandas.np.float) < 0]    # 获取全部下跌数据
    grouped = ret.groupby(lambda d: d.strftime('%Y-%m')).size()     # 按月份获取当月下跌次数
    print(grouped.sort_values(ascending=False))


