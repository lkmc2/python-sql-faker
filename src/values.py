# coding=utf-8
import random
import time
import datetime

class Values:
    @staticmethod
    def of(*args):
        class ValueCreator:
            def create(self):
                return random.choice(args)

        return ValueCreator

    @staticmethod
    def of_int_range(start, end):
        class ValueCreator:
            def create(self):
                return random.randint(start, end)

        return ValueCreator

    @staticmethod
    def of_float_range(start, end, precision=2):
        """最多精确到小数点后10位"""
        class ValueCreator:
            def create(self):
                return round(random.uniform(start, end), precision)

        return ValueCreator

    @staticmethod
    def of_time_range(start_time, end_time):
        class ValueCreator:
            def create(self):
                timestamp = random.randint(start_time, end_time)
                return datetime.datetime.fromtimestamp(timestamp)

        return ValueCreator

class Times:
    @staticmethod
    def of(year, month, day, hour=0, minute=0, second=0):
        return time.mktime(datetime.datetime(year, month, day, hour, minute, second).timetuple())