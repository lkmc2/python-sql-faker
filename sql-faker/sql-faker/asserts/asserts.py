# coding=utf-8
class Asserts:
    """条件检测器"""

    @staticmethod
    def is_true(condition, error_msg):
        # 条件不正确则抛异常
        if not condition:
            raise AttributeError(error_msg)