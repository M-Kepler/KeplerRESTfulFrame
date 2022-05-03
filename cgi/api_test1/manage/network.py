# -*-coding:utf-8-*-

import random
from kepler.cgilib.register import Resource
from kepler.cgilib.response import api_success
from kepler.cgilib.param_parse import extract_params, check_params

MODULE_NAME = "cgi.api_test1.manage"


class NetWork(Resource):
    """
    get 请求的json schema
    {
        "name": "Froid",
        "age" : 26,
        "address" : {
            "city" : "New York",
            "country" : "USA"
        }
    }
    """

    get_params_schema = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "age": {"type": "integer"},
            "category_id": {"type": "string"},
            "hobbies": {"type": "array"},
            "address": {
                "type": "object",
                "properties": {
                    "city": {"type": "string"},
                    "country": {"type": "string"}
                }
            }
        },
        "required": ["category_id"]
    }

    @check_params(param_config=get_params_schema)
    def do_get(self, request):
        params = extract_params(request)
        print("===== args: %s" % params)

        category_id = params["category_id"]
        name = params.get("name", "")
        age = params.get("age", 0)
        hobbies = params.get("hobbies", [])

        ret = api_success(data={
            "category_id": category_id,
            "name": name,
            "age": age,
            "hobbies": hobbies,
            "random_int": random.randint(1, 100),
            "i18n_test": ("%s.i18n_test" % MODULE_NAME) % {
                "name": "huangjinjie"
            }
        })

        return ret
