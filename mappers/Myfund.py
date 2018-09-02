# coding: utf-8
from sqlalchemy import Column, DECIMAL, DateTime, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Myfund(Base):
    __tablename__ = 'myfund'

    fcode = Column(String(20), primary_key=True)
    fname = Column(String(20))
    NAV = Column(DECIMAL(10, 4))
    ACCNAV = Column(DECIMAL(10, 4))
    updatetime = Column(DateTime)
    fdate = Column(DateTime)
    DGR = Column(String(20))
    DGV = Column(String(20))
    fee = Column(String(20))

    def __str__(self):
        return "基金代码:{0},基金名称:{1},单位净值:{2},累计净值:{3},基金日期:{4},日增长值:{5},日增长率:{6},费率:{7}" \
            .format(self.fcode, self.fname, self.NAV, self.ACCNAV, self.fdate, self.DGR, self.DGV, self.fee)
