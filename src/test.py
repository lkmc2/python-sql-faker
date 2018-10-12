from sql_faker import Faker, DataType, DBHelper

import pymysql
from DBUtils.PooledDB import PooledDB

# DBHelper.db_setting('python_sql_faker')
#
# db = DBHelper()
#
# res = db.execute("insert into user(id, name) values('666', 'jack')")
#
# db.execute("select * from user where id = '666'")

POOL = PooledDB(creator=pymysql,
                              maxconnections=5,
                              host='localhost',
                              user='root',
                              passwd='123456',
                              db='python_sql_faker',
                              port=3306)
conn = POOL.connection()
cur = conn.cursor()

cur.execute("insert into user(id, name) values('666', 'jack')")

cur.execute("select * from user where id = '666'")

data = cur.fetchall()

print data

conn.rollback()

cur.execute("select * from user where id = '666'")

data = cur.fetchall()

print 'haha', data

# db.dispose()

# Faker.table_name("user") \
#     .param("id", DataType.ID) \
#     .param("name", DataType.USERNAME) \
#     .param("birthday", DataType.TIME) \
#     .param("phone", DataType.PHONE) \
#     .param("address", DataType.ADDRESS) \
#     .param("age", DataType.AGE) \
#     .param("sex", DataType.SEX) \
#     .param("email", DataType.EMAIL) \
#     .insert_count(5) \
#     .execute()