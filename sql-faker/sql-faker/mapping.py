# coding=utf-8

from utils.datatype import DataType
from random_data.address_random import AddressRandom
from random_data.age_random import AgeRandom
from random_data.email_random import EmailRandom
from random_data.id_random import IdRandom
from random_data.phone_random import PhoneRandom
from random_data.sex_random import SexRandom
from random_data.time_random import TimeRandom
from random_data.username_random import UserNameRandom

# 数据类型映射关系
DATA_TYPE_MAPPING = {
    DataType.ID: IdRandom,
    DataType.USERNAME: UserNameRandom,
    DataType.PHONE: PhoneRandom,
    DataType.TIME: TimeRandom,
    DataType.ADDRESS: AddressRandom,
    DataType.AGE: AgeRandom,
    DataType.SEX: SexRandom,
    DataType.EMAIL: EmailRandom
}
