# coding=utf-8
import random
import datetime


class Values:
    """取值范围设置器"""

    @staticmethod
    def of(*args):
        """在给定的参数中随机选一个作为返回值"""
        class ValueCreator:
            def create(self):
                return random.choice(args)

        return ValueCreator

    @staticmethod
    def of_int_range(start, end):
        """在[start, end]区间随机返回一个整数值"""

        class ValueCreator:
            def create(self):
                return random.randint(start, end)

        return ValueCreator

    @staticmethod
    def of_float_range(start, end, precision=2):
        """在[start, end]区间随机返回一个浮点数，最多精确到小数点后10位"""

        class ValueCreator:
            def create(self):
                return round(random.uniform(start, end), precision)

        return ValueCreator

    @staticmethod
    def of_time_range(start_time, end_time):
        """在[start, end]区间随机返回一个时间值"""

        class ValueCreator:
            def create(self):
                timestamp = random.randint(start_time, end_time)
                return datetime.datetime.fromtimestamp(timestamp)

        return ValueCreator
