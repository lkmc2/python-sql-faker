# coding=utf-8
from random_abstract import RandomData
import random


class PhoneRandom(RandomData):
    """手机号生成器（11位手机号）"""

    def create(self):
        return random.choice(phone_prefix) + str(random.randrange(12345678, 99999998))


# 手机号前缀
phone_prefix = (
    "134", "135", "136", "137", "138", "139", "147", "150", "151",
    "152", "157", "158", "159", "182", "187", "188", "130", "131",
    "132", "155", "156", "185", "186", "130", "131", "132", "155",
    "156", "185", "186", "170", "199"
)
