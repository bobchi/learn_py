from sqlalchemy import create_engine, desc, text
from mappers.Infos import News
from sqlalchemy.orm import sessionmaker

# mysql+pymysql 必须要加数据库驱动,驱动可不同，pymysql 是上次安装的, echo=True是调试参数
engine = create_engine('mysql+pymysql://root:root@localhost/py_test?charset=utf8mb4', echo=True)

# 创建一个与数据库的回话连接
Session = sessionmaker(bind=engine)
session = Session()

# 查询全部
news = session.query(News)
print(news.all()[0].__dict__)    # 转换为字典
print(news.all()[0].news_title)  # 读取第一条的标题
# 查询第一条
first = news.first()
# 条件查询
news.filter(News.news_id > 1).order_by(desc(News.news_id)).limit(2).offset(0).all()
# 原生查询
news.filter(text('news_id>:nid and news_class=:nclass')).params(nid=1, nclass='python').all()
# 主键查询
session.query(News).get(2)

# 新增
# news_add = News(news_title='测试新闻123')
# session.add(news_add)
# session.commit()

# 修改
news.filter(News.news_id == 2).update({'news_class': 'php'})
session.commit()


