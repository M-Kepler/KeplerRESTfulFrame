# -*-coding:utf-8-*-

from kepler.cgilib.register import Resource


class API_3(Resource):

    def do_get(self, request):
        return "I'am api_test2.resource_folder.aip3.\n"

    def do_post(self, request):
        pass
