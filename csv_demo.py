from sqlalchemy import create_engine
from common.config import db_url
from sqlalchemy.orm import sessionmaker
from mappers.Myfund import Myfund
import csv

engine = create_engine(db_url, echo=True)
session = sessionmaker(engine)()

result = session.query(Myfund).limit(10).all()

print(result)

# 写入到csv文件
with open('./csv/fund.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['编码', '名称', 'NAV', 'ACCNAV', '日期', 'DGR', 'DGV'])
    for r in result:
        writer.writerow([r.fcode, r.fname, r.NAV, r.ACCNAV, r.fdate, r.DGR, r.DGV])
    f.close()

