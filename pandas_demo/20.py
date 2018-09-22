import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from common.config import db_url

if __name__ == "__main__":
    engine = create_engine(db_url)
    res = engine.execute('select * from user_orders').fetchall()
    orders = pd.DataFrame(res, columns=['username', 'orderdate', 'pay'])

    # 获得订单表中用户当月/日消费次数
    ground_date = orders.groupby(['username', orders.apply(lambda x:x['orderdate'].strftime('%Y-%m'), axis=1)]).size()

    # 获得订单表中用户当月消费总额
    cost = orders.groupby(['username', orders.apply(lambda x:x['orderdate'].strftime('%Y-%m'), axis=1)]).agg({'pay': np.sum})

    # 按消费总额，给客户评定等级
    levels = ['青铜', '白银', '黄金', '王者']
    user_levels = pd.cut(orders['pay'], bins=[10,20,40,50,100], right=False, labels=levels)
    print(user_levels)

