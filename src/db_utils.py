# coding=utf-8
import pymysql
from DBUtils.PooledDB import PooledDB

# 数据库配置信息
db_info = {}


class DBHelper:
    """数据库连接助手"""
    __POOL = None

    def __init__(self):
        self.conn = self.get_conn()
        self.cur = self.conn.cursor()

    @staticmethod
    def get_conn():
        """获取连接"""
        global __POOL
        if DBHelper.__POOL is None:
            __POOL = PooledDB(creator=db_info['creator'],
                              maxconnections=5,
                              host=db_info['host'],
                              user=db_info['user'],
                              passwd=db_info['passwd'],
                              db=db_info['db'],
                              port=db_info['port'])
        return __POOL.connection()

    @staticmethod
    def db_setting(db, creator=pymysql, user='root', passwd='123456', host='localhost', port=3306):
        """设置数据库配置信息"""
        db_info.update({
            'db': db,
            'creator': creator,
            'user': user,
            'passwd': passwd,
            'host': host,
            'port': port
        })

    def execute(self, sql):
        """执行SQL语句"""
        effect_num = self.cur.execute(sql)
        return effect_num

    def commit(self):
        """提交操作"""
        self.conn.commit()

    def rollback(self):
        """回滚操作"""
        self.conn.rollback()

    def dispose(self):
        """释放连接"""
        self.cur.close()
        self.conn.close()
