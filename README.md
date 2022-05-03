- [需求描述](#需求描述)
- [模块设计](#模块设计)
  - [概要说明](#概要说明)
    - [目录结构](#目录结构)
    - [API 接口](#api-接口)
    - [工作原理](#工作原理)
  - [方案选型](#方案选型)
    - [flask-restful 插件](#flask-restful-插件)
- [使用效果](#使用效果)
  - [URL 和 代码目录可以对应起来](#url-和-代码目录可以对应起来)
  - [统一封装响应格式](#统一封装响应格式)
  - [支持参数解析](#支持参数解析)
  - [支持参数校验](#支持参数校验)
  - [支持接口调试](#支持接口调试)
- [TODO LIST](#todo-list)

# 需求描述

- 需要符合 RESTFul 风格 API

  - 希望把所有的 URL 注册在一个地方

  - 希望 URL 可以和代码目录保持一直

- 支持参数解析

- 支持参数类型校验、可选性、xss 等基本安全校验

- 支持封装响应格式，统一标准

- 支持对 接口 进行调试

# 模块设计

## 概要说明

### 目录结构

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
│   ├── api1.py                  -----> 资源
│   ├── index.py                 =====> 注册该路径下的资源，URL 为 /kepler/api_test2/xxx
│   └── __init__.py
└── __init__.py

```

**打印出来的 `APP.url_map` 如下，对比可以发现，路由和代码路径都是一一对应的， `index.py` 作为了对注册， `.py` 文件作为资源**

```sh
Map([
    <Rule '/kepler/api_test2/resource_folder/api2/' (HEAD, GET, POST, OPTIONS) -> kepler.cgilib.register._do_method.149896>,
    <Rule '/kepler/api_test2/resource_folder/api3/' (HEAD, GET, POST, OPTIONS) -> kepler.cgilib.register._do_method.149933>,
    <Rule '/kepler/api_test1/manage/network/' (HEAD, GET, OPTIONS) -> kepler.cgilib.register._do_method.866>,
    <Rule '/kepler/api_test1/helloworld/' (HEAD, GET, POST, OPTIONS) -> kepler.cgilib.register._do_method.224429>,
    <Rule '/kepler/api_test2/api1/' (HEAD, GET, POST, OPTIONS) -> kepler.cgilib.register._do_method.886>,
    <Rule '/' (HEAD, GET, OPTIONS) -> index>,
    <Rule '/static/<filename>' (HEAD, GET, OPTIONS) -> static>
])
```

### API 接口

```sh
cd /usr/local/lib/python3.8/dist-packages/
sudo ln -s /mnt/f/workspaces/KeplerRESTfulFrame/lib/kepler_restful_frame.pth ./
```

- 测试 `utils.cgi.register/Resource` restful 接口资源类，是否可以实现 `do_[http_mothod]` 的资源方法

- `utils.cgi.register/Register` 接口注册类，是否能按restful标准注册URL处理资源函数, 而且需要支持URL多级目录（即看目录就可以知道url访问的是哪个资源，开源的restful框架没有这个能力）

- `utils.cgi.param_parse/check_params` 参数检查，借助 `jsonschema` 库做 schema 格式检查

- `utils.cgi.param_parse/extract_params` 参数解析获取

### 工作原理

## 方案选型

### flask-restful 插件

[Flask RESTful 插件官网](http://www.pythondoc.com/Flask-RESTful/index.html)

# 使用效果

## URL 和 代码目录可以对应起来

```sh
# 代码路径为 api_test2/api1
$curl --location http://localhost:5000/kepler/api_test2/api1

I'am api_test2.resource_test.

```

## 统一封装响应格式

```sh
$curl http://127.0.0.1:5000/kepler/api_test1/manage/network/?category_id=121

{
  "code": 0,
  "data": {
    "category_id": "121",
    "i18n_test": "cgi.api_test1.manage.i18n_test",
    "random_int": 78
  },
  "message": ""
}

```

## 支持参数解析

```sh
$curl "http://127.0.0.1:5000/kepler/api_test1/manage/network/?category_id=121&name=huangjinjie"

##### 得到以下参数：
===== args: CombinedMultiDict([ImmutableMultiDict([('category_id', '121'), ('name', 'huangjinjie')])])

```

## 支持参数校验

**参数类型校验**

**参数可选性校验**

```sh
# 没传入必选参数 category_id 时：
$curl --location http://127.0.0.1:5000/kepler/api_test1/manage/network

# 得到以下报错，由于开了 debug 模式，所以提示信息比较详细
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
  "http://www.w3.org/TR/html4/loose.dtd">
<html>
  <head>
    <title>kepler.cgilib.param_parse.ErrorMessage: &lt;ValidationError: &quot;&#x27;category_id&#x27; is a required property&quot;&gt; // Werkzeug Debugger</title>

    ##### 这里有说到 category_id 是不必选属性

```

## 支持接口调试

# TODO LIST

- [ ] 支持接口调试

- [ ] URL 传参的时候，怎么用 jsonschema 做参数类型校验？URL 参数都是字符串类型的

- [ ] 请求处理前，进行上下文初始化
