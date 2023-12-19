# -*- coding:utf-8 -*-
# @FileName  :orm_demo.py
# @Time      :2023/12/18 11:28
# @Author    :dzz
# @Function  :
# 自定义ORM 框架
import pymysql
from pymysql.cursors import DictCursor


# ORM  将数据类型转换成Python对象
# 数据库中的表---->Pytho的类
# 表里面的列---->类的属性
# 表的行--->类的实例 字典对象表述
# 字典对象的key对应列 Value对应值
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


class User:
    table_name = "users"

    # 构造方法，传递字典参数作为Insert的Key和Value
    def __init__(self, **kwargs):
        # 动态的给实例设置属性和值
        for k, v in kwargs.items():
            self.__setattr__(k, v)
        print(self.__dict__)

    # 封装查询操作
    def select(self, **where):
        # print(len(where))
        sql = "select * from %s" % self.table_name
        if where:
            sql += " where "
            for k, v in where.items():
                sql += f"{k}='{v}' and "
            sql += "1=1"
        print(sql)
        return MYSQL().query(sql)
        # print(sql.rfind('and'))

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


if __name__ == "__main__":
    user = User(credit='100', nickname='蜗牛1', qq='1223', username='zhansan', password='111223', role='1')
    result = user.select(userid=1)
    user.insert()
    # print(result)
