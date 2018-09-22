import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from common.config import db_url

if __name__ == "__main__":
    engine = create_engine(db_url)
    res = engine.execute('select * from reviews').fetchall()
    # 转换成DataFrame
    ret = pd.DataFrame(res, columns=['id', 'subject_id', 'username', 'r_content', 'r_time'])

    # 需求1：把同用户同文章id下重复的评论id找出来
    # subset是比对的重复栏目名,如果keep为False,则只要是重复的都为True，否则保留第一个其余为True
    # rev = ret.duplicated(subset=['subject_id', 'username', 'r_content'], keep=False)
    # # 把重复值筛选出来
    # rev = ret[rev]
    # ids = rev['id']
    # # 执行结果 1,11,13
    # print(','.join([str(s) for s in ids]))

    # 需求2：统计用户发帖数量
    # rev = ret.groupby(['username', 'subject_id']).size()
    # print(rev)

    # 案例3：按日期统计当天发帖数量
    def test(x):        
        return x['r_time'].strftime('%Y-%m-%d')


    _date = ret.groupby(['username', ret.apply(test, axis=1)]).size()
    print(_date)

