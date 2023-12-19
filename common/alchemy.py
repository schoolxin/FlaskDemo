# -*- coding:utf-8 -*-
# @FileName  :alchemy.py
# @Time      :2023/12/19 14:50
# @Author    :dzz
# @Function  :
# 建立mysql链接
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine, Column, Integer, String, DateTime


engine = create_engine('mysql+pymysql://root:000000@hadoop102/woniunote', echo=False)
# 定义模型类继承的父类及数据连接会话
DBsession = sessionmaker(bind=engine)
dbSession = scoped_session(DBsession) # 线程安全
Base = declarative_base()


# 定义模型类
class Users(Base):
    __table_name__ = "users"
    # 如果需要在SQLAlchemy里面直接创建表结构，则详细定义列
    userid = Column(Integer, primary_key=True)
    username = Column(String(50))
    password = Column(String(32))
    nickname = Column(String(30))
    qq = Column(String(15))
    role = Column(String(10))
    credit = Column(Integer)
    createtime = Column(DateTime)
    updatetime = Column(DateTime)


Users.metadata.create_all(engine)  # 创建表
