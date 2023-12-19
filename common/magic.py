# -*- coding:utf-8 -*-
# @FileName  :magic.py
# @Time      :2023/12/18 9:46
# @Author    :dzz
# @Function  :
class User:
    table_name = "users"  # 类属性

    def __init__(self):
        self.username = 'qiang'  # 实例变量

    def method(self, value):
        print("hello%s" % value)

    def chain(self):
        print("通过返回当前类实例进行连续的方法调用")
        return self
    def hello(self):
        print("hello in chain")
        return self


if __name__ == "__main__":
    print(User.__dict__)  # 通过类名可以获取类的属性和方法列表
    user = User()
    print(user.__class__.__dict__)  # 通过实例名获取类名
    print(user.__dict__)  # 获取实例属性或变量
    user.password = "0000"
    print(user.__dict__)  # 获取实例属性或变量
    user.__setattr__("nickname", '强哥')
    print(user.__dict__)  # 获取实例属性或变量
    setattr(user, "nickname1", '强哥')  # setattr全局函数
    print(user.__dict__)  # 获取实例属性或变量
    print(user.__getattribute__('nickname1'))
    user.__getattribute__('method')('hello')
    # 链式操作
    user.chain().chain()
    user.hello().chain()
    print(User.__getattribute__(user,'table_name'))


    # 通过双下划线区分 是否为自定义属性或方法
    # for k,v in User.__dict__.items():
    #     print("k:%s--->v:%s"%(k,v))

#