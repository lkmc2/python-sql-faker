# coding=utf-8
import logging
from asserts.asserts import Asserts
from mapping import DATA_TYPE_MAPPING
import collections
from datatype import DataType
from values import Values, Times
from cache_dict import get_cache_obj

DataType = DataType
Values = Values
Times = Times


class Faker:
    """数据伪造器"""

    def __init__(self, table_name):
        self.table_name = table_name
        self.count = None
        self.param_dict = collections.OrderedDict()
        self.sql_list = []

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
        # 1.检查参数
        self.check_param()

        # 2.生成SQL语句
        self.generate_sql()

        # 3.执行SQL语句，插入数据到数据库
        for sql in self.sql_list:
            print sql

    def check_param(self):
        """检查参数"""
        Asserts.is_true(self.table_name, "table_name must not empty")
        Asserts.is_true(len(self.param_dict) >= 1, "param's count must bigger than 1")
        Asserts.is_true(self.count >= 1, "insert_count must bigger than 1")

    def generate_sql(self):
        """生成SQL语句"""
        for x in range(self.count):
            param_names, param_values = self.generate_param_name_and_value()

            sql = 'insert into %s(%s) values(%s)' % (self.table_name, param_names, param_values)
            self.sql_list.append(sql)
            logging.debug(sql)

    def generate_param_name_and_value(self):
        """生成所有参数名和参数值"""
        sql_param_names = ''
        sql_param_values = ''
        for param_name, param_type in self.param_dict.iteritems():
            sql_param_names += param_name + ','
            sql_param_values += self.create_param_values(param_type) + ','
        # 所有参数名，所有参数值
        return sql_param_names[:-1], sql_param_values[:-1]

    @staticmethod
    def create_param_values(param_type):
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
