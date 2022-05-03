# -*-coding:utf-8-*-

"""
Author       : M_Kepler
EMail        : m_kepler@foxmail.com
Last modified: 2022-05-02 11:12:41
Filename     : base_unittest.py
Description  : 单元测试基本框架
               支持跳过用例
"""


import time
import unittest
from functools import wraps


class BaseUnitTest(unittest.TestCase):

    # 是否把结果输出出来
    OUTPUT = False

    # 跳过的用例：跳过原因
    SKIP_CASE = {
        "test_func1": "skip_reason1"
        # "test_func2": "skip_reason2"
    }

    def unittest_case(func):
        """
        装饰器，根据 SKIP_CASE 来制定哪些用例需要执行，那些不执行
        否则需要执行/取消某几个用例时要到每个函数加上/取消装饰器，太麻烦
        """
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            # python3 中已经没有 func.func_name 了，用 func.__name__ 替代
            if func.__name__ in self.SKIP_CASE.keys():
                print("\n===== skip func [%s] for reason [%s]" % (
                    func.__name__, self.SKIP_CASE.get(func.__name__)))
                return unittest.skip(self.SKIP_CASE.get(func.__name__))(
                    func)(self, *args, **kwargs)

            begin = time.strftime(
                "%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
            print("\n===== start func %s at %s" % (func.__name__, begin))

            ret = func(self, *args, **kwargs)
            if BaseUnitTest.OUTPUT:
                print(ret)

            end = time.strftime("%Y-%m-%d %H:%M:%S",
                                time.localtime(time.time()))
            print("===== end func %s at %s" % (func.__name__, end))

        return wrapper

    @classmethod
    def setUpClass(cls):
        """
        测试数据构造
        """
        print("===== creating test data...")
        pass

    @classmethod
    def tearDownClass(cls):
        """
        回退测试数据
        """
        print("===== destroying test data...")
        pass
