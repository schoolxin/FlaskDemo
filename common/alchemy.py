# -*- coding:utf-8 -*-
# @FileName  :alchemy.py
# @Time      :2023/12/19 14:50
# @Author    :dzz
# @Function  :
# 建立mysql链接
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine, Table, MetaData
import common

engine = create_engine('mysql+pymysql://root:000000@hadoop102/woniunote', echo=False)
# 定义模型类继承的父类及数据连接会话
DBsession = sessionmaker(bind=engine)
dbSession = scoped_session(DBsession)  # 线程安全
Base = declarative_base()
metadata = MetaData()
metadata.reflect(bind=engine)

common.show()


# 定义模型类
# class Users(Base):
#     __table_name__ = "users"
#     # 如果需要在SQLAlchemy里面直接创建表结构，则详细定义列
#     userid = Column(Integer, primary_key=True)
#     username = Column(String(50))
#     password = Column(String(32))
#     nickname = Column(String(30))
#     qq = Column(String(15))
#     role = Column(String(10))
#     credit = Column(Integer)
#     createtime = Column(DateTime)
#     updatetime = Column(DateTime)
#
#
# Users.metadata.create_all(engine)  # 创建表

class Users(Base):
    # __tablename__ = 'users'
    __table__ = Table('users', metadata, autoload=True)  # autoload自动加载表的元数据 并作为该类的类属性


if __name__ == "__main__":
    # print(Users.__dict__)
    result = dbSession.query(Users).filter(Users.userid >= 1)
    result1 = dbSession.query(Users.userid, Users.username).filter(Users.userid >= 1)  # 指定查询的列 返回的是元组，不再是模型对象
    # print(result1)
    # result = dbSession.query(Users).filter_by(userid=5)
    # for row in result:
    #     print(row)
    #     print(row.userid, row.username)

    # 新增
    # user = Users(credit='100', nickname='蜗牛1', qq='1223', username='zhansan', password='111223', role='1')
    # dbSession.add(user)
    # dbSession.commit()
    # 删除和修改
    row = dbSession.query(Users).filter_by(userid=9).first()
    # row = dbSession.query(Users).filter_by(userid=9).delete()
    print(row)
    # row.username = '火箭2'
    dbSession.delete(row) # 删除

    dbSession.commit()



