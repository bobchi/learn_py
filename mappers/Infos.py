from sqlalchemy import Column, Integer, String, TEXT, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class News(Base):
    __tablename__ = 'news'
    news_id = Column(Integer, primary_key=True, autoincrement=True)
    news_title = Column(String(50), nullable=False)
    news_class = Column(String(50), nullable=False)
    news_abstract = Column(TEXT)
    news_updatetime = Column(TIMESTAMP)
    news_clicknum = Column(Integer, default=0)

