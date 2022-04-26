# -*-coding:utf-8-*-

import random
from kepler.cgilib.register import Resource
from kepler.cgilib.response import api_success
from kepler.cgilib.param_parse import extract_params, check_params

MODULE_NAME = "cgi.api_test1.manage"


class NetWork(Resource):
    # get 请求的json schema
    get_params_schema = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "age": {"type": "integer"},
            "category_id": {"type": "string"},
            "address": {
                "type": "object",
                "properties": {
                    "city": {"type": "string"},
                    "country": {"type": "string"}
                }
            }
        },
        "required": []
    }
    """
    {
        "name": "Froid",
        "age" : 26,
        "address" : {
            "city" : "New York",
            "country" : "USA"
        }
    }
    """

    @check_params(param_config=get_params_schema)
    def do_get(self, request):
        params = extract_params(request)
        category_id = params.get("category_id")
        ret = api_success(data={
            "category_id": category_id,
            "random_int": random.randint(1, 100),
            "i18n_test": ("%s.i18n_test" % MODULE_NAME) % {
                "name": "huangjinjie"
            }
        })
        return ret
