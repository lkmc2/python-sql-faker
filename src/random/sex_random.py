# coding=utf-8
from random_abstract import RandomData
import random


class SexRandom(RandomData):
    """性别生成器（0：男， 1：女）"""

    def create(self):
        return random.choice([0, 1])
