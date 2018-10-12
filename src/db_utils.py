# coding=utf-8
import logging
import pymysql
from DBUtils.PooledDB import PooledDB


class DBHelper:
    """数据库连接助手"""
    __POOL = None

    def __init__(self, db, creator=pymysql, user='root', passwd='123456', host='localhost', port=3306):
        self.db = db
        self.creator = creator
        self.user = user
        self.passwd = passwd
        self.host = host
        self.port = port

        self.conn = self.get_conn()
        self.cur = self.conn.cursor()

    def get_conn(self):
        """获取连接"""
        global __POOL
        if DBHelper.__POOL is None:
            __POOL = PooledDB(creator=self.creator, maxconnections=5, host=self.host, user='root', passwd='123456',
                              db=self.db, port=self.port)
        return __POOL.connection()

    def insert(self, sql):
        """插入SQL数据"""
        logging.debug(sql)
        effect_num = self.cur.execute(sql)
        self.conn.commit()
        return effect_num

    def select(self, sql):
        """查询SQL数据"""
        self.cur.execute(sql)
        select_res = self.cur.fetchall()
        return select_res

    def dispose(self):
        """释放连接"""
        self.cur.close()
        self.conn.close()


db = DBHelper('python_sql_faker')

res = db.select('select * from user')

print res

db.dispose()
