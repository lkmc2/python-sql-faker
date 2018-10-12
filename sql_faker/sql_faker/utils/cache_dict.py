# coding=utf-8

# 对象缓存字典
cache_dict = {}


def get_cache_obj(obj_type):
    """获取缓存对象"""
    if obj_type not in cache_dict:
        cache_dict.update({obj_type: obj_type()})
    return cache_dict.setdefault(obj_type)
