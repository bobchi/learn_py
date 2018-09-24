import pandas as pd
import numpy as np
import json


# 判断字符串是否符合json格式，是返回True，否则False
def is_json(string):
    try:
        json.loads(string)
        return True
    except:
        return False


if __name__ == '__main__':
    with open('../log/httpd.log', encoding='utf-8') as f:
        log_lst = [json.loads(s) for s in f if is_json(s)]
        f.close()
    logs = pd.DataFrame(log_lst)
    # 得出总行数和列数
    # print(logs.shape)

    # 案例1：统计接口访问量，并按降序排列
    # print(logs.groupby('path').size().sort_values(ascending=False))

    # 案例2：统计访问量最高的时段 以小时计
    # 构建一个2017-10-10的时间Series
    date_r = pd.date_range('2017-10-10 00:00:00', end='2017-10-11 00:00:00', closed='left', freq='h')
    # 把日志中的时间dt字段字符串转化为时间
    logs['dt'] = pd.to_datetime(logs['dt'])
    # 使用pandas中的cut函数，给日志增加一个dr时间字段，并把时间Series与日志时间匹配
    logs['dr'] = pd.cut(logs['dt'], bins=date_r, right=False)
    print(logs.groupby('dr').size().sort_values(ascending=False))
    # print(logs['dr'])
