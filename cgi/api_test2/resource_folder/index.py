# -*-coding:utf-8-*-

from kepler.cgilib.register import Register
from cgi.api_test2.resource_folder.api2 import API_2
from cgi.api_test2.resource_folder.api3 import API_3


def index(exter_reg, name):
    inter_reg = Register(exter_reg, name)

    # 为资源添加路由，访问路径为：/<name>/resource_folder/api2
    inter_reg.add_resource("api2", API_2())

    inter_reg.add_resource("api3", API_3())
