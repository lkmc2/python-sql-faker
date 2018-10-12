# coding=utf-8
from sql_faker import Faker, DataType, Values, Times, DBHelper, RandomData
import random
import pymysql

# 设置数据库信息
DBHelper.db_setting(db='python_sql_faker',
                    driver=pymysql,
                    user='root',
                    passwd='123456',
                    host='127.0.0.1',
                    port=3306)

#  给user表的四个字段填充5条数据
Faker.table_name("user") \
    .param("name", DataType.USERNAME) \
    .param("age", DataType.AGE) \
    .param("sex", DataType.SEX) \
    .param("address", DataType.ADDRESS) \
    .param("birthday", DataType.TIME) \
    .insert_count(5) \
    .execute()

Faker.table_name("user") \
    .param("id", DataType.ID) \
    .param("name", DataType.USERNAME) \
    .param("birthday", DataType.TIME) \
    .param("phone", DataType.PHONE) \
    .param("address", DataType.ADDRESS) \
    .param("age", DataType.AGE) \
    .param("sex", DataType.SEX) \
    .param("email", DataType.EMAIL) \
    .insert_count(5) \
    .execute()


# 自定义随机生成器必须继承自RandomData的类，重写create方法，提供一个可以随机生成的值
class EnglishNameRandom(RandomData):
    def create(self):
        return random.choice(['jack', 'andy', 'kim'])


# 使用自定义随机生成器EnglishNameRandom生成名字
Faker.table_name("user") \
    .param("id", DataType.ID) \
    .param("name", EnglishNameRandom) \
    .insert_count(1) \
    .execute()

# 使用Values.of(可变长参数)方法生成随机值，值在指定的参数中选取一个
Faker.table_name("user") \
    .param("id", Values.of(3, 5, 7)) \
    .param("name", DataType.USERNAME) \
    .insert_count(1) \
    .execute()

# 使用Values.of_int_range(起始值, 结束值)方法生成随机值，值在指定的范围中选取一个整数
Faker.table_name("user") \
    .param("id", Values.of_int_range(18, 28)) \
    .param("name", DataType.USERNAME) \
    .insert_count(1) \
    .execute()

# 使用Values.of_float_range(起始值, 结束值, 精度=2)方法生成随机值，值在指定的范围中选取一个浮点数
Faker.table_name("user") \
    .param("id", Values.of_float_range(13.88, 22.33)) \
    .param("name", DataType.USERNAME) \
    .insert_count(1) \
    .execute()

# 使用Values.of_float_range(起始值, 结束值, 精度)方法生成随机值，值在指定的范围中选取一个浮点数
Faker.table_name("user") \
    .param("id", Values.of_float_range(13.88, 22.33, 6)) \
    .param("name", DataType.USERNAME) \
    .insert_count(1) \
    .execute()

# 使用Values.of_float_range(开始时间, 结束时间)方法生成随机值，值在指定的范围中选取一个时间（精确到日）
Faker.table_name("user") \
    .param("id", Values.of_time_range(Times.of(2017, 3, 12), Times.of(2018, 4, 3))) \
    .param("name", DataType.USERNAME) \
    .insert_count(1) \
    .execute()

# 使用Values.of_float_range(开始时间, 结束时间)方法生成随机值，值在指定的范围中选取一个时间（精确到秒）
Faker.table_name("user") \
    .param("id", Values.of_time_range(Times.of(2017, 3, 12, 10, 23, 17), Times.of(2018, 4, 3, 2, 30, 18))) \
    .param("name", DataType.USERNAME) \
    .insert_count(1) \
    .execute()

# 给product表的9个字段填充1条数据
Faker.table_name("product") \
    .param("type", Values.of("优品", "良品", "次品")) \
    .param("person_count", Values.of_int_range(20, 50)) \
    .param("enter_price", Values.of_float_range(12.33, 34.57)) \
    .param("outcome_price", Values.of_float_range(100.004132, 240.281424, 6)) \
    .param("firstTime", Values.of_time_range(Times.of(2018, 3, 22), Times.of(2018, 10, 22))) \
    .param("secondTime",
           Values.of_time_range(
               Times.of(2018, 3, 22, 11, 23, 24),
               Times.of(2018, 10, 22, 22, 15, 17)
           )
     ) \
    .insert_count(1) \
    .only_show_sql()

# 指定name字段使用EnglishNameRandom类进行随机值的生成
Faker.table_name("user")\
       .param("name", EnglishNameRandom)\
       .param("age", Values.of_int_range(20, 50))\
       .param("address", DataType.ADDRESS)\
       .insert_count(5)\
       .only_show_sql()
