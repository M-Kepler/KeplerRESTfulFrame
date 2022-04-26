# -*-coding:utf-8-*-

"""
/api_test2/ 目录下的路由注册
"""

from cgi.api_test2.api_3 import API_3
from kepler.cgilib.register import Register


def index(exter_reg, name):
    # 注册路由
    inter_reg = Register(exter_reg, name)

    # 添加资源
    inter_reg.add_resource("api3", API_3())
