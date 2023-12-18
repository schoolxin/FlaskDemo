# -*- coding:utf-8 -*-
# @FileName  :mysqldb.py
# @Time      :2023/12/18 9:14
# @Author    :dzz
# @Function  :
import pymysql
from pymysql.cursors import DictCursor, SSDictCursor

# 链接数据
# 执行sql语句
# 关闭数据库链接
conn = pymysql.connect(host='hadoop102', user='root', password='000000', database='woniunote', charset='utf8',port=3306)
conn.autocommit(True)
# 1.实例化游标实例
cur = conn.cursor(cursor=SSDictCursor)

# 2.定义SQL语句
sql = "select * from users where userid = 2"
# sql = "update users set qq='12345' where userid=2"
# 3.通过游标执行
cur.execute(sql)
# 4.处理执行结果
result = cur.fetchall()
print(result)
cur.close()
if __name__ == "__main__":
    run_code = 0
