# -*-coding:utf-8-*-

from kepler.cgilib.register import Resource


class API_1(Resource):

    def do_get(self, request):
        return "I'am api_test2.aip1.\n"

    def do_post(self, request):
        pass
