# -*- coding:utf-8 -*-
# @FileName  :main.py
# @Time      :2023/12/16 13:44
# @Author    :dzz
# @Function  :
import os

from flask import Flask

app = Flask(__name__, template_folder='template', static_url_path='/', static_folder='resource')
app.config['SECRET_KEY'] = os.urandom(24)  # 24位 生成随机数种子  用于产生sessionID


def getType2():
    type = {'1': 'Python1', '2': 'Java2'}
    return type


app.jinja_env.globals.update(mytype=getType2)


# 自定义模板页面的过滤器
def mylen(str):
    return len(str)


app.jinja_env.filters.update(mylens=mylen)

if __name__ == "__main__":
    from controller.myhtml import *
    from controller.jinja2 import *

    app.register_blueprint(myhtml)
    app.register_blueprint(jinja2)
    app.run(debug=True)
