# -*-coding:utf-8-*-

"""
/api_test2/ 目录下的路由注册
"""

from cgi.api_test2.api1 import API_1
from cgi.api_test2.resource_folder.index import index as resource_folder_index
from kepler.cgilib.register import Register


def index(exter_reg, name):
    # 注册路由
    inter_reg = Register(exter_reg, name)

    # 注册下一层级的资源，注册的路由为 /<name>/resource_folder/*
    resource_folder_index(inter_reg, "resource_folder")

    # 添加路由，访问路径为：/<name>/api1
    inter_reg.add_resource("api1", API_1())
