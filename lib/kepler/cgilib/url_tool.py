# -*-coding:utf-8-*-


class UrlTool(object):
    # uri和参数连接符，如 /api/v1/user?age=10
    URI_CONN_CHAR = '?'
    # url中参数分隔符，如 dev_id=111&dev_name=222
    PARAM_SPLIT = '&'
    # 参数赋值符 如 dev_id=111
    PARAM_EQUL_CHAR = '='

    @classmethod
    def parse_url(cls, url):
        """
        :desc 获取url的参数
        :param url，包括uri和参数
        :return 返回参数字典
        :example
            url = "/api/v1/vpn/users?ip=ipdefault&port=portsdwr"
            param_dict = get_url_params(url)
            print(param_dict)
            {
                'uri': '/api/v1/vpn/users',
                'ip': 'ipdefault',
                'port': 'portsdwr'
            }
        """
        param_dict = dict()
        uri = url.split(cls.URI_CONN_CHAR)
        params = uri[1].split(cls.PARAM_SPLIT)
        for arg in params:
            arg_split = arg.split(cls.PARAM_EQUL_CHAR)
            param_dict[arg_split[0]] = arg_split[1]
        param_dict['uri'] = uri[0]
        return param_dict

    @classmethod
    def make_url(cls, base_url, param_dict):
        """
        :desc 为url拼装get请求的参数
        :param base_url
        :param param_dict
        :example:
            base_url = /api/v1/user
            param_dict = {
                'age': 24,
                'city': 'shenzhen'
            }
            return: /api/v1/user?age=24&city=shenzhen
        """
        base_url = base_url + cls.URI_CONN_CHAR
        params = list()
        for k, v in param_dict.items():
            param = k + cls.PARAM_EQUL_CHAR + str(v)
            params.append(param)
        url = base_url + cls.PARAM_SPLIT.join(params)
        return url
