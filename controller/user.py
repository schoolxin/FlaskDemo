# -*- coding:utf-8 -*-
# @FileName  :user.py
# @Time      :2023/12/20 10:09
# @Author    :dzz
# @Function  :
from flask_sqlalchemy import SQLAlchemy

from module.users import Users
from flask import Blueprint

userapp = Blueprint('userapp',__name__)

@userapp.route('/user')
def user_demo():
    return Users().base_query_summary()