from bs4 import BeautifulSoup
from urllib import request
from datetime import datetime

response = request.urlopen('http://fund.eastmoney.com/fund.html')
html = response.read()
html = html.decode('gb2312')
with open('./files./2.txt', 'wb') as f:
    f.write(html.encode('utf8'))
    f.close()

with open('./files/2.txt', 'rb') as f:
    html = f.read().decode('utf8')
    f.close()

soup = BeautifulSoup(html, 'html.parser')
f_codes = soup.find('table', id='oTable').tbody.find_all('td', 'bzdm') # 基金代码
ret = ()
for f_code in f_codes:
    ret += ({
        'f_code': f_code.get_text()
        , 'f_name': f_code.next_sibling.find('a').get_text()
        , 'nav': f_code.next_sibling.next_sibling.get_text()
        , 'accnav': f_code.next_sibling.next_sibling.next_sibling.get_text()
        , 'updated': datetime.now().isoformat(' ', 'seconds')
    },)

print(ret)

import pymysql
from pymysql.cursors import Cursor, SSCursor
from common.config import db_config

connection = pymysql.connect(**db_config)
cursor = Cursor(connection)
cursor.executemany("""insert into fund(f_code,f_name,nav,accnav,updated) 
values(%(f_code)s,%(f_name)s,%(nav)s,%(accnav)s,%(updated)s)
ON duplicate KEY UPDATE updated=%(updated)s,nav=%(nav)s,accnav=%(accnav)s""", ret)
connection.commit()
connection.close()
