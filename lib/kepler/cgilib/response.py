# -*-coding:utf-8-*-

"""
RESTFulApi 响应规范封装

response: {
    "code": 0,      # 错误码
    "message": "",  # 错误信息
    "data": ...     # 响应数据
}
"""

from flask import jsonify


def api_success(code=0, data="", message=""):
    info = {
        "code": code,
        "message": message,
        "data": data
    }
    return jsonify(info)


def api_fail(code=-1, data="", message=""):
    info = {
        "code": code,
        "message": message,
        "data": data
    }
    return jsonify(info)
