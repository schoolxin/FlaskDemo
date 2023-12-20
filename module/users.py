# -*- coding:utf-8 -*-
# @FileName  :users.py
# @Time      :2023/12/20 10:02
# @Author    :dzz
# @Function  :
# from common.database import db
from sqlalchemy import Table, or_

from main import db


class Users(db.Model):
    __tablename__ = "users"
    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(32))
    nickname = db.Column(db.String(32))
    avatar = db.Column(db.String(32))
    qq = db.Column(db.String(32))
    role = db.Column(db.String(32))
    credit = db.Column(db.String(32))

    def __str__(self):
        return self.username

    # def __repr__(self):
    #     return self.username

    def find_user_byId(self, userid):
        # row = db.session.query(Users).filter(Users.userid==userid).first()
        # filter_by 只适用于等值查询，其参数为字典参数的传值方式
        # filter 适用于复杂的查询，其参数为条件运算 需要是类.属性名

        row = db.session.query(Users).filter_by(userid=userid).first()  # 支持多表查询

        # row1 = Users.query.filter_by(userid=userid).first() # 不支持多表查询
        # print(row1.username)
        return row

    # 基础查询汇总
    def base_query_summary(self):
        res = db.session.query(Users).all()
        # for row in res:
        #     print(row)
        # res1 = db.session.query(Users.userid, Users.username).all()
        # res1 = db.session.query(Users.userid, Users.username).filter_by(userid=1,qq='12345678').all()  --226658397
        res1 = db.session.query(Users).filter(or_(Users.userid >= 2, Users.qq == '226658397')).all()
        print(res1)

        return res[0].nickname
