# coding=utf-8
import logging
import collections
from asserts.asserts import Asserts
from mapping import DATA_TYPE_MAPPING
from cache_dict import get_cache_obj
from db_utils import DBHelper

# 日志打印级别为DEBUG
logging.basicConfig(level=logging.DEBUG)


class Faker:
    """数据伪造器"""

    def __init__(self, table_name):
        self.table_name = table_name
        self.total_count = 0
        self.count = None
        self.param_dict = collections.OrderedDict()
        self.sql_list = []
        self.is_insert_to_db = False

    @classmethod
    def table_name(cls, name):
        """设置数据库表名"""
        return cls(name)

    def param(self, param_name, param_type):
        """设置字段名和对应的类型值"""
        self.param_dict.update({param_name: param_type})
        return self

    def insert_count(self, count):
        """设置插入数据条数"""
        self.count = count
        return self

    def execute(self):
        """插入数据到数据库"""
        self.is_insert_to_db = True
        # 执行主要逻辑
        self.__execute_main_logic()

    def only_show_sql(self):
        """只显示生成的SQL，不插入数据到数据库"""
        self.is_insert_to_db = False
        # 执行主要逻辑
        self.__execute_main_logic()

    def ignored(self):
        """不执行任何操作"""
        pass

    def __execute_main_logic(self):
        """执行主要逻辑"""
        # 1.检查参数
        self.__check_param()
        # 2.生成SQL语句
        self.__generate_sql()
        # 3.执行SQL语句，插入数据到数据库
        self.__execute_sql()

    def __execute_sql(self):
        # 执行SQL语句，插入数据到数据库

        # 如果不插入数据，则只显示生成数据条数在控制台
        if not self.is_insert_to_db:
            logging.debug('successfully create [ %s ] data' % self.count)
            return

        # 创建数据库连接池
        db = DBHelper()
        try:
            # 插入数据到数据库
            for sql in self.sql_list:
                self.total_count += db.execute(sql)
            # 提交操作
            db.commit()
            logging.debug('successfully insert [ %s ] data to database' % self.total_count)
        except:
            logging.error('failed to insert data, database is rollback')
            # 回滚操作
            db.rollback()
        finally:
            # 释放连接
            db.dispose()

    def __check_param(self):
        """检查参数"""
        Asserts.is_true(self.table_name, "table_name must not empty")
        Asserts.is_true(len(self.param_dict) >= 1, "param's count must bigger than 1")
        Asserts.is_true(self.count >= 1, "insert_count must bigger than 1")

    def __generate_sql(self):
        """生成SQL语句"""
        for x in range(self.count):
            param_names, param_values = self.__generate_param_name_and_value()

            sql = 'insert into %s(%s) values(%s)' % (self.table_name, param_names, param_values)
            self.sql_list.append(sql)
            logging.debug(sql)

    def __generate_param_name_and_value(self):
        """生成所有参数名和参数值"""
        sql_param_names = ''
        sql_param_values = ''
        for param_name, param_type in self.param_dict.iteritems():
            sql_param_names += param_name + ','
            sql_param_values += self.__create_param_values(param_type) + ','
        # 所有参数名，所有参数值
        return sql_param_names[:-1], sql_param_values[:-1]

    @staticmethod
    def __create_param_values(param_type):
        """创建所有参数值"""
        Asserts.is_true(type(param_type) == str or hasattr(param_type, 'create'),
                        "param_type must be DataType value or a class extends RandomData ")

        # DataType类型的值
        if type(param_type) == str:
            # 获取DataType类型对应的类
            param_type = DATA_TYPE_MAPPING.setdefault(param_type)

        # 实例化目标类
        target = get_cache_obj(param_type)

        # 字符串两边加上单引号
        return "'%s'" % target.create()
