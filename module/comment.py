# -*- coding:utf-8 -*-
# @FileName  :comment.py
# @Time      :2023/12/21 10:07
# @Author    :dzz
# @Function  :
from main import db


class comment(db.Model):
    __tablename__ = "comment"
    commentid = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer)
    articleid = db.Column(db.Integer)
    content = db.Column(db.String(1024))
    ipaddr = db.Column(db.String(1024))
    replyid = db.Column(db.Integer)
    agreecount = db.Column(db.Integer)
    opposecount = db.Column(db.Integer)
    hidden = db.Column(db.Integer)
    createtime = db.Column(db.DateTime)
    updatetime = db.Column(db.DateTime)
