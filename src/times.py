# coding=utf-8
import time
import datetime


class Times:
    """时间范围设置器"""

    @staticmethod
    def of(year, month, day, hour=0, minute=0, second=0):
        """创建一个时间值"""
        return time.mktime(datetime.datetime(year, month, day, hour, minute, second).timetuple())
