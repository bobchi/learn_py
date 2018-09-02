# coding: utf-8
from sqlalchemy import Column, DECIMAL, DateTime, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Fund(Base):
    __tablename__ = 'myfund'

    fcode = Column(String(20), primary_key=True)
    fname = Column(String(20))
    NAV = Column(DECIMAL(5, 4))
    accnav = Column(DECIMAL(5, 4))
    updated = Column(DateTime)
