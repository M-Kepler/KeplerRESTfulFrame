# -*-coding:utf-8-*-

from cgi.api_test1.helloworld import HelloWorld
from cgi.api_test1.manage.index import index as manage_index
from kepler.cgilib.register import Register


def index(exter_reg, name):
    inter_reg = Register(exter_reg, name)

    # 注册下一层级的资源，注册的路由为 /<name>/manage/*
    manage_index(inter_reg, "manage")

    # 为资源添加路由，访问路径为：/<name>/helloworld
    inter_reg.add_resource("helloworld", HelloWorld())
