from datatype import DataType
from faker import Faker
import random


class EnglishNameRandom:
    def create(self):
        return random.choice(['jack', 'andy', 'kim'])


Faker.table_name("user") \
    .param("id", DataType.ID) \
    .param("name", DataType.USERNAME) \
    .param("birthday", DataType.TIME) \
    .param("phone", DataType.PHONE) \
    .param("address", DataType.ADDRESS) \
    .param("age", DataType.AGE) \
    .param("sex", DataType.SEX) \
    .param("email", DataType.EMAIL) \
    .insert_count(1) \
    .execute()

Faker.table_name("user") \
    .param("id", EnglishNameRandom) \
    .param("name", DataType.USERNAME) \
    .insert_count(1) \
    .execute()
