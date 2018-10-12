from sql_faker import Faker, DataType, DBHelper

DBHelper.db_setting('python_sql_faker')

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