import pandas as pd

if __name__ == '__main__':
    # 读取表格，让fcode以字符串显示，索引列是fdate
    fund = pd.read_csv('../csv/004616.csv', dtype={'fcode': pd.np.str_}, index_col='fdate', parse_dates=['fdate'])

    f20178 = fund.loc['2017-8', ['NAV']].reset_index()
    f20188 = fund.loc['2018-8', ['NAV']].reset_index()
    f20178.columns = ['fdate', 'NAV2017']

    # print(pd.concat([f20177, f20188], axis=1))

    # 补全缺省日期，构造连续时间
    f20178_date = pd.DataFrame(pd.date_range('2017-8', end='2017-9', closed='left'), columns=['fdate'])
    f20188_date = pd.DataFrame(pd.date_range('2018-8', end='2018-9', closed='left'), columns=['fdate'])
    # 将连续日期和原有日期合并
    f20178_new = pd.merge(f20178_date, f20178, how='left', on=['fdate'])
    f20188_new = pd.merge(f20188_date, f20188, how='left', on=['fdate'])
    # 合并
    res = pd.concat([f20178_new, f20188_new], axis=1)
    print(res.fillna(0))
    # print(f20178_new)


