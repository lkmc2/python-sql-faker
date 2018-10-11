# coding=utf-8
from random_abstract import RandomData
import uuid


class IdRandom(RandomData):
    """id生成器（32位的UUID，不带连接符）"""

    def create(self):
        return str(uuid.uuid1()).replace('-', '')
