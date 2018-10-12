from custom.english_name_random import EnglishNameRandom
from sql_faker import Faker, DataType, Values, Times

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

Faker.table_name("user") \
    .param("id", EnglishNameRandom) \
    .param("name", DataType.USERNAME) \
    .insert_count(1) \
    .execute()

Faker.table_name("user") \
    .param("id", Values.of(3, 5, 7)) \
    .param("name", DataType.USERNAME) \
    .insert_count(1) \
    .execute()

Faker.table_name("user") \
    .param("id", Values.of_int_range(18, 28)) \
    .param("name", DataType.USERNAME) \
    .insert_count(1) \
    .execute()

Faker.table_name("user") \
    .param("id", Values.of_float_range(13.88, 22.33)) \
    .param("name", DataType.USERNAME) \
    .insert_count(1) \
    .execute()

Faker.table_name("user") \
    .param("id", Values.of_float_range(13.88, 22.33, 6)) \
    .param("name", DataType.USERNAME) \
    .insert_count(1) \
    .execute()

Faker.table_name("user") \
    .param("id", Values.of_time_range(Times.of(2017, 3, 12), Times.of(2018, 4, 3))) \
    .param("name", DataType.USERNAME) \
    .insert_count(1) \
    .execute()

Faker.table_name("user") \
    .param("id", Values.of_time_range(Times.of(2017, 3, 12, 10, 23, 17), Times.of(2018, 4, 3, 2, 30, 18))) \
    .param("name", DataType.USERNAME) \
    .insert_count(1) \
    .execute()