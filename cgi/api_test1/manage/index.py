
# -*-coding:utf-8-*-

from cgi.api_test1.manage.network_setting import NetWork
from kepler.cgilib.register import Register


def index(exter_reg, name):
    inter_reg = Register(exter_reg, name)
    # 注册的路由为 /manage/network/
    inter_reg.add_resource("network", NetWork())
