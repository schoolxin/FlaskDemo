# -*- coding:utf-8 -*-
# @FileName  :myhtml.py
# @Time      :2023/12/16 13:47
# @Author    :dzz
# @Function  :
from flask import Blueprint, render_template, session

jinja2 = Blueprint('jinja2', __name__)

# 在模板中调用python自定义的函数
# 1.使用上下文处理器来注册自定义的函数到Jinja2模板中 context_processor 并且返回一个字典类型的数据(重要的点)
# 2.按照标准的函数调用的方式 如果要为自定义函数传递参数，则需要使用两层闭包进行包裹
@jinja2.context_processor
def getType():
    type = {'1': 'Python', '2': 'Java'}
    return dict(getTypes=type)

@jinja2.context_processor
def myfunc():
    def mytype(args):
        type = {'1': 'Python', '2': 'Java'}
        return mytype
    return dict(getTypes=mytype)
# {{getTypes(100)}}



@jinja2.route('/jinja2')
def jinja2_demo():
    session['username'] = '222'
    article = {
        'title': 'python',
        'count': 100
    }
    content = "<font color='red'>这是一段红色字体</font>"
    return render_template("jinja2-demo.html", article=article, count=10, content=content)
