# coding=utf-8
from random_abstract import RandomData
import random


class AgeRandom(RandomData):
    """年龄生成器（18到60岁）"""
    def create(self):
        return random.randrange(18, 60)
