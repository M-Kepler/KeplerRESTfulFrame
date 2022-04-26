# -*- coding:utf-8 -*-

"""
Flask 请求上下文
"""

from flask import g
from flask import request


class CgiContextManager(object):
    @property
    def set_cookies(self):
        if not hasattr(g, 'kepler__context_set_cookies'):
            g.kepler__context_set_cookies = dict()
        return g.kepler__context_set_cookies

    @set_cookies.setter
    def set_cookies(self, value):
        assert isinstance(value, dict), 'Set-cookies must be a dict obj'
        g.kepler__context_set_cookies = value

    @property
    def cookies(self):
        return request.cookies

    @property
    def user(self):
        if not hasattr(g, 'kepler__context_user'):
            g.kepler__context_user = None
        return g.kepler__context_user

    @user.setter
    def user(self, value):
        g.kepler__context_user = value
