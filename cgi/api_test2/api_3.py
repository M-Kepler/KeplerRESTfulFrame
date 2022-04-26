# -*-coding:utf-8-*-

from kepler.cgilib.register import Resource


class API_3(Resource):

    def do_get(self, request):
        return "I'am api3."

    def do_post(self, request):
        pass
