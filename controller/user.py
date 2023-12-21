# -*- coding:utf-8 -*-
# @FileName  :user.py
# @Time      :2023/12/20 10:09
# @Author    :dzz
# @Function  :
import json

from flask_sqlalchemy import SQLAlchemy

from module.users import Users
from flask import Blueprint, jsonify, make_response

userapp = Blueprint('userapp', __name__)


@userapp.route('/user')
def user_demo():
    return Users().base_query_summary()


@userapp.route('/userall')
def userall_demo():
    users = Users().find_all_user()
    users_list = modle_list(users)
    return jsonify(users_list)  # jsonify 把标准的python列表或者字典或者组合转为json 并且响应的content-type也会被设置成application/json


def modle_list(res):
    # [{},{}] json 是JavaScript Notation 是JavaScript内置数据格式，由JavaScript的数组，对象构成
    users_list = []
    for user in res:
        user_dict = user.__dict__
        user_dict = {k: v for k, v in user_dict.items() if k != '_sa_instance_state'}
        users_list.append(user_dict)
        # print(user_dict)
        # map(lambda x: x(0) != '_sa_instance_state', user_dict.items())
        # [x for x in range(10) if x%100==0]
        # ["even" if x%2==0 else "odd" for x in range(100)]
    # print(users_list)

    return users_list


# 如果是链接查询，比如res1 = db.session.query(Articles.articleid,Articles.headline,Users.nickname).join(Users,Articles.userid==Users.userid).all() 如何构建json
@userapp.route('/userarticle')
def userarticle_demo():
    userarticle = Users().query_user_article()
    res_list = []
    for ua in userarticle:
        tuple_art, tuple_user = ua
        article = {k: v for k, v in tuple_art.__dict__.items() if k != '_sa_instance_state'}
        user = {k: v for k, v in tuple_user.__dict__.items() if k != '_sa_instance_state'}
        # print(article, "--->", user)
        user_art_dict = {'username': user.get('username'), 'articleid': article.get('articleid'),'articletitle': article.get('headline')}
        res_list.append(user_art_dict)
    resp = make_response(res_list)
    resp.charset = 'utf-8'

    return resp  # jsonify 把标准的python列表或者字典或者组合转为json 并且响应的content-type也会被设置成application/json
