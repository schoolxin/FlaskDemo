# -*- coding:utf-8 -*-
# @FileName: demo.py
# @Time:2023/12/15 23:26
# @Author    :dengzz
from flask import Blueprint, request

print("demo", __name__)
demo1 = Blueprint('demo1', __name__)

# 控制器拦截器 蓝图拦截器
@demo1.before_request
def bp_before():
    url = request.path
    if url =='/demo1':
        return "无法访问demo1"
    else:
        pass

@demo1.route("/demo1")
def demos1():
    return "这是另一个模块中的页面"
@demo1.route("/demo2")
def demos2():
    return "这是另一个模块中的页面"
