from sqlalchemy import create_engine
import pandas as pd
from common.config import db_url

engine = create_engine(db_url)
res = engine.execute('select * from users_info')
users = pd.DataFrame(res.fetchall(), columns=['id', '姓名', '年龄', '性别', '爱好'])
# 增加一列
users['state'] = users['年龄'] + 10
# 定位函数loc 和直接取数相比user[2:5] 包含2和5列，即闭区间
# users = users.loc[2:5, ['姓名', '性别']]
# users = users.iloc[1:3, 2:5]
# 去重 以id列去重，保留第一个
users.drop_duplicates(subset=['id'], keep='first', inplace=True)
# 建索引
# users = users.set_index('id')
# 也可以这样写 直接覆盖原users不用赋值
users.set_index('id', inplace=True)

users.index = pd.to_numeric(users.index)
print(users.loc[101:106])
