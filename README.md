- [目录结构](#目录结构)
- [说明](#说明)

# 目录结构

```sh
~/workspaces/KeplerRESTfulFrame$ tree

app.py                           =====> Flask APP 入口，为所有添加了统一前缀 kepler
                                 =====> 注册 api_test1 api_test2 这些资源

cgi/
├── api_test1
│   ├── helloworld.py            -----> 资源
│   ├── index.py                 =====> 注册该路径下的资源，URL 为 /kepler/api_test1/xxx
│   └── manage
│       ├── index.py             =====> 注册该路径下的资源，URL 为 /kepler/api_test1/manage/xxx
│       ├── __init__.py
│       └── network_setting.py   -----> 资源
|
├── api_test2
│   ├── api_3.py                 -----> 资源
│   ├── index.py                 =====> 注册该路径下的资源，URL 为 /kepler/api_test2/xxx
│   └── __init__.py
└── __init__.py

```

**打印出来的 `APP.url_map` 如下，对比可以发现，路由和代码路径都是一一对应的， `index.py` 作为了对注册， `.py` 文件作为资源**

```
Map([
    <Rule '/kepler/api_test1/manage/network/' (OPTIONS, HEAD, GET)    -> kepler.cgilib.register._do_method.449591>,
    <Rule '/kepler/api_test1/helloworld/' (OPTIONS, POST, HEAD, GET)  -> kepler.cgilib.register._do_method.28956146>,
    <Rule '/kepler/api_test2/api3/' (OPTIONS, POST, HEAD, GET)        -> kepler.cgilib.register._do_method.438958>,
    <Rule '/' (OPTIONS, HEAD, GET)                                    -> index>,
    <Rule '/static/<filename>' (OPTIONS, HEAD, GET)                   -> static>
])
```

# 说明

```sh
cd /usr/local/lib/python3.8/dist-packages/
sudo ln -s /mnt/f/workspaces/KeplerRESTfulFrame/lib/kepler_restful_frame.pth ./
```

- 希望把所有的 URL 注册在一个地方

- 希望 URL 可以和代码目录保持一直

- 测试 `utils.cgi.register/Resource` restful 接口资源类，是否可以实现 `do_[http_mothod]` 的资源方法

- `utils.cgi.register/Register` 接口注册类，是否能按restful标准注册URL处理资源函数, 而且需要支持URL多级目录（即看目录就可以知道url访问的是哪个资源，开源的restful框架没有这个能力）

- `utils.cgi.param_parse/check_params` 参数检查，借助 `jsonschema` 库做 schema 格式检查

- `utils.cgi.param_parse/extract_params` 参数解析获取
