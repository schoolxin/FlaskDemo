# -*- coding:utf-8 -*-
# @FileName: article.py
# @Time:2023/12/20 23:09
# @Author    :dengzz
from main import db


class Articles(db.Model):
    __tablename__ = "article"
    articleid = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer)
    content = db.Column(db.String(1024))
    credit = db.Column(db.Integer)
    readcount = db.Column(db.Integer)
