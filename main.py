# -*- coding:utf-8 -*-
# @FileName  :main.py
# @Time      :2023/12/16 13:44
# @Author    :dzz
# @Function  :
import os

from flask import Flask, abort

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


@app.route("/")
def index():
    return render_template("index-base.html")
    # return render_template("article-base.html")


# 定义404 错误页面
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error-404.html')

@app.errorhandler(500)
def page_not_found(e):
    return render_template('error-500.html')

@app.route("/error")
def error_500():

    return abort(500)

if __name__ == "__main__":
    from controller.myhtml import *
    from controller.jinja2 import *

    app.register_blueprint(myhtml)
    app.register_blueprint(jinja2)
    app.run(debug=True)
