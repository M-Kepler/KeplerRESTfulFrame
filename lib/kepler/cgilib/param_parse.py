# -*-coding:utf-8-*-

"""
HTTP 请求参数解析
"""

from functools import wraps

from flask import request
from jsonschema import FormatChecker, ValidationError, validate


def extract_params(request):
    """
    解析获取参数

    :return dict
    :e.g.
        params = extract_params(request)
    """
    cache = getattr(request, "_extract_param_cache", None)
    if cache is not None:
        return cache
    else:
        con_type = request.headers.get("Content-Type")
        if isinstance(con_type, str):
            if "application/json" in con_type:
                return request.get_json()
        return request.values


class ErrorMessage(Exception):

    def __init__(self, msg):
        self.value = msg

    def __str__(self):
        return repr(self.value)


def check_params(param_config=None, header_config=None, *args, **kwargs):
    """
    json 格式参数校验

    :example
        # 定义 json schema
        get_params_schema = {
        "type": "object",
        "properties": {
            # 字符串类型
            "name": {"type": "string"},
            # 整数类型
            "age": {"type": "integer"},
            "address": {
                # 对象类型（即dict)
                "type": "object",
                "properties": {
                    "city": {"type": "string"},
                    "country": {"type": "string"}
                }
            }
        },
        # 必须的参数
        "required": ["name"]
    }
    # 参数例子:
    {
        "name": "Froid",
        "age" : 26,
        "address" : {
            "city" : "New York",
            "country" : "USA"
        }
    }
    @check_params(param_config=get_params_schema)
    def do_get(self, request):
        pass
    """

    def deco(f):
        def extract_params(request):
            if request.method == "POST":
                return request.get_json()
            else:
                return request.args

        def extract_headers(headers, config):
            required_header = {}
            all_present = True
            if config:
                for header_name, header_type in config.iteritems():
                    required_header[header_name] = headers(header_name)
                    if required_header[header_name]:
                        required_header[header_name] = header_type(
                            required_header[header_name])
                    else:
                        all_present = False
            required_header["_all_params_present_"] = all_present
            return required_header

        @wraps(f)
        def decorated_function(*args, **kwargs):
            try:
                params = extract_params(request)
                validate(params, param_config, format_checker=FormatChecker())
                if header_config:
                    header_params = extract_headers(
                        headers=request.headers.get,
                        config=header_config)
                    if not header_params.get("_all_params_present_"):
                        return Exception("invalid headers")
                    return f(header_params=header_params, *args, **kwargs)
                else:
                    return f(*args, **kwargs)
            except ValidationError as e:
                raise ErrorMessage(e)
        return decorated_function
    return deco
