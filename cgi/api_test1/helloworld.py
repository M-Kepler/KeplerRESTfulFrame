# -*-coding:utf-8-*-

from flask_restful import reqparse
from flask_restful import fields
from kepler.cgilib.register import Resource

# 参数解析
parser = reqparse.RequestParser()
parser.add_argument("username", type=str, help="please input user_name")
parser.add_argument("age", trim=True, default=24, type=int,
                    required=True, help="please input user_name")


class HelloWorld(Resource):
    # 可以使用 ORM 模型或者自定义的模型的时候，
    # 会自动的获取模型中的相应的字段，生成 json 数据，然后再返回
    # 可以定义好返回的结构
    resource_fields = {
        "username": fields.String,
        # 没有值时还可以指定默认值
        "age": fields.Integer(default=24),
        # 内部使用school，返参可以重命名为 education
        "education": fields.String(attribute="school"),
        # 可以定义列表或字典类型
        "tags": fields.List(fields.String),
        "more": fields.Nested({
            "signature": fields.String
        })
    }

    def do_get(self, request):
        args = parser.parse_args()
        return args

    def do_post(self, request):
        pass
