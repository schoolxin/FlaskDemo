# -*- coding:utf-8 -*-
# @FileName  :orm_demo02.py
# @Time      :2023/12/19 11:18
# @Author    :dzz
# @Function  :
import pymysql
from pymysql.cursors import DictCursor


class MYSQL:
    def __init__(self):
        conn = pymysql.connect(host='hadoop102', user='root', password='000000', database='woniunote', charset='utf8',
                               port=3306)
        self.cur = conn.cursor(DictCursor)
        conn.autocommit(True)

    def query(self, sql):
        self.cur.execute(sql)
        return self.cur.fetchall()

    def insert(self, sql):
        self.cur.execute(sql)


# 封装成标准的模型类 供子类继承
# 增加field()方法来执行查询那些列，*代表所有列
class Model:
    # 构造方法，传递字典参数作为Insert的Key和Value
    def __init__(self, **kwargs):
        # 动态的给实例设置属性和值
        for k, v in kwargs.items():
            self.__setattr__(k, v)
        print(self.__dict__)

    # 通过链式查询  操作指定的查询列
    def field(self, columns):
        self.columns = columns  # 动态添加类实例属性
        return self

    # 带列表的查询
    def select(self, **where):
        # print(len(where))
        table = self.__class__.__getattribute__(self, 'table_name')
        if hasattr(self, 'columns'):
            sql = "select %s from %s" % (self.columns, table)
        else:
            sql = "select * from %s" % table
        if where:
            sql += " where "
            for k, v in where.items():
                sql += f"{k}='{v}' and "
            sql += "1=1"
        print(sql)
        return MYSQL().query(sql)

    def insert(self):
        # insert into table (k) values (v)
        sql = "insert into %s " % self.table_name
        keys = list(self.__dict__.keys())
        print(type(keys))
        values = list(self.__dict__.values())
        print(','.join(keys))
        print("','".join(values))
        print(sql)
        sql += "(" + ','.join(keys) + ") values('"
        sql += "','".join(values) + "')"
        print(sql)
        MYSQL().insert(sql)


# 定义子类
class Users(Model):
    table_name = "users"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


user = Users()
# print(user.__getattribute__("table_name"))
result = user.field('userid,username').select(userid=1)
print(result)
