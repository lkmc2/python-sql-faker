# coding=utf-8
import sys
sys.path.append("..")

from datatype import DataType
from values import Values
from times import Times
from db_utils import DBHelper
from random_data.random_abstract import RandomData
from faker import Faker

# 数据类型
DataType = DataType

# 取值范围设置器
Values = Values

# 时间范围设置器
Times = Times

# 数据库连接池助手
DBHelper = DBHelper

# 随机值抽象类
RandomData = RandomData

# 数据伪造器
Faker = Faker