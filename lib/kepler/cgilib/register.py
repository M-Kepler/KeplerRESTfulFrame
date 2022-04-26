# -*-coding:utf-8-*-

"""
RESTFulApi 路由注册
"""

import functools

import rpdb
from flask import Flask
from flask import request as flask_request
from kepler.cgilib.cgi_context_manage import CgiContextManager


class Resource(object):
    method_enum = ['GET', 'PUT', 'POST', 'DELETE']
    cgi_context = CgiContextManager()

    @staticmethod
    def rpdb_entry_for_cgi(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            items = flask_request.path.split('/')
            items = filter(bool, items)
            id_name = '.'.join(items)
            method = flask_request.method.lower()
            unix_sock = '/var/run/kepler:%s:%s' % (id_name, method)
            rpdb.set_trace(unix_sock)
            result = func(*args, **kwargs)
            return result
        return wrapper

    def _do_method(self):
        method = flask_request.method
        caller_name = 'do_%s' % method.lower()
        caller = getattr(self, caller_name, None)
        if caller:
            check_params = getattr(caller, '_check_params_handler', None)
            if hasattr(check_params, '__call__'):
                # TODO
                check_params()
            # caller = self.rpdb_entry_for_cgi(caller)
            return caller(flask_request)
        else:
            raise Exception('unsupport method:%s' % method)


class Register(object):
    def __init__(self, parent, name=''):
        assert parent
        self.child_registers = {}
        self.url_rules = {}
        self.filters = []
        self.base_url = '/'
        self.name = name

        if isinstance(parent, Register):
            assert parent.base_url[-1] == '/'
            self.flask_object = parent.flask_object
            self.base_url = parent.base_url + name + '/'
            self.filters = list(parent.filters)  # inherit from parent
        elif isinstance(parent, Flask):
            # 这样就可以加上URL加上应用前缀了
            self.base_url = self.base_url + self.name + '/'
            self.flask_object = parent
        else:
            raise TypeError(
                'parent to create register must be register or flask')

    def add_filters(self, filter_list):
        assert isinstance(filter_list, (list, tuple)), 'Bad filters'
        for f in filter_list:
            assert hasattr(f, '__call__'), 'Bad filter: %s' % f
            assert f not in self.filters, '%s already exists' % f
            self.filters.append(f)

    def route(self, rule, **options):
        def deco(f):
            endpoint = options.pop('endpoint', None)
            self.add_url_rule(rule, endpoint, f, **options)
            return f
        return deco

    @staticmethod
    def result_format(func, catch_exception):
        pass

    @staticmethod
    def make_request_handler_wrapper(func, filters, catch_exception):
        f = func
        for fitem in reversed(filters):
            f = fitem(f)
            assert hasattr(f, '__call__'), 'Bad filters:%s' % fitem
        # f = _context_init(f)
        # 返回数据格式化
        # f = result_format(f, catch_exception)
        # f = functools.wraps(func)(f)
        return f

    def add_url_rule(self, rule, endpoint=None, view_func=None, **options):
        assert '/' not in rule
        assert self.flask_object
        new_url = self.base_url + rule + '/'
        new_endpoint = view_func.__module__ + '.' \
            + view_func.__name__ + '.' \
            + str(hash(view_func))
        debug = self.flask_object.debug
        wrapper = self.make_request_handler_wrapper(func=view_func,
                                                    filters=self.filters,
                                                    catch_exception=debug)
        self.flask_object.add_url_rule(rule=new_url, endpoint=new_endpoint,
                                       view_func=wrapper, **options)
        self.url_rules[rule] = view_func

    def add_resource(self, name, resource):
        assert isinstance(resource, Resource), 'Bad resource:%s, %s' % (
            name, resource)
        found_method = []
        for method in Resource.method_enum:
            func_name = 'do_%s' % method.lower()
            func = getattr(resource, func_name, None)
            if func and hasattr(func, '__call__'):
                found_method.append(method)
        if found_method:
            self.add_url_rule(rule=name,
                              view_func=resource._do_method,
                              methods=found_method)


if __name__ == "__main__":
    pass
