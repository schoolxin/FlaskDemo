# -*- coding:utf-8 -*-
# @FileName  :main.py
# @Time      :2023/12/16 13:44
# @Author    :dzz
# @Function  :
import os

from flask import Flask, abort
from sqlalchemy import MetaData

from common.database import db
import pymysql

pymysql.install_as_MySQLdb()  # 解决python2(MySQLdb中使用的) 的问题 ModuleNotFoundError: No module named 'MySQLd
app = Flask(__name__, template_folder='template', static_url_path='/', static_folder='resource')
app.config['SECRET_KEY'] = os.urandom(24)  # 24位 生成随机数种子  用于产生sessionID

# 使用集成方式处理SQLAlchemy
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:000000@hadoop102:3306/woniunote?charset=utf8'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:000000@hadoop102:3306/woniunote?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 跟踪数据库的修改 及时发送信号给Flask
app.config['SQLALCHEMY_ECHO'] = True  # 跟踪数据库的修改 及时发送信号给Flask
# 初始化数据库
db.init_app(app)  # Flask环境跟db绑定了
# metadata = MetaData()
# metadata.reflect(bind=db)

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


if __name__ == "__main__":  # 其他模块在引入main的时候 下面的代码不会被执行 也可以解决循环引用的问题
    print("ddd")
    from controller.myhtml import *
    from controller.jinja2 import *

    app.register_blueprint(myhtml)
    app.register_blueprint(jinja2)

    from controller.user import *

    app.register_blueprint(userapp)

    app.run(debug=True)
