# -*-coding:utf-8-*-

"""
RESTFulApi 响应规范封装
"""

from flask import jsonify


def api_success(data=None):
    info = {
        'success': 1
    }
    if data:
        info['data'] = data
    return jsonify(info)


def api_fail(data=None):
    info = {
        'success': 0
    }
    if data:
        info['data'] = data
    return jsonify(info)
