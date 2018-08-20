import pymysql
from pymysql.cursors import Cursor, SSCursor
from common.config import db_config

connection = pymysql.connect(**db_config)

# try:
#     with connection.cursor() as cursor:
#         cursor.execute('select * from fund')
#         result = cursor.fetchone()
#         print(result)
# finally:
#     connection.close()

cursor = Cursor(connection)
cursor.execute('insert into fund(name) values(%s)', ('测试基金3', ))
connection.commit()
connection.close()

result = cursor.fetchall()
print(result)



