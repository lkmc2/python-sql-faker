# coding=utf-8
from random_abstract import RandomData
import random
import datetime


class TimeRandom(RandomData):
    """时间生成器（一年前到现在的时间范围内任意选择一个时刻）"""

    def create(self):
        days = random.randrange(1, 365)
        seconds = random.randrange(0, 86400)
        now = datetime.datetime.now()
        delta = datetime.timedelta(days=days, seconds=seconds)
        # 现在的时间 - 时间偏移量
        return (now - delta).strftime('%Y-%m-%d %H:%M:%S')
