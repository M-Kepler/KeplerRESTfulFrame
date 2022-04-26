# -*-coding:utf-8-*-

"""
CGI 主入口
"""

from flask import Flask
from cgi.api_test1.index import index as api_test1_index
from cgi.api_test2.index import index as api_test2_index
from kepler.cgilib.register import Register

APP = Flask(__name__)

# 定义url入口点，根目录是/，每一个 Register则作为一个子目录，

# 为所有 URL 的添加前缀 kepler
url_register = Register(APP, "kepler")

# 注册 /api_test1/ 目录下的资源，路径为 /kepler/api_test1/*
api_test1_index(url_register, "api_test1")
api_test2_index(url_register, "api_test2")


@APP.route("/", methods=["GET"])
def index():
    return "hello world"


if __name__ == "__main__":
    print(APP.url_map)
    APP.run(host="127.0.0.1", port=5000, debug=True)
