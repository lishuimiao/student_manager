# -*- coding:gbk -*-
# f = open('E:\test\测试文档.txt','w+','encoding')
# print(f.)
# #f.write()
# f.close()

"""
类对象
类属性
类方法
    什么时候定义类方法？当方法中需要使用类对象，或者私有类属性是
    创建类
    创建私有类属性
    创建类方法
    通过类对象调用私有类属性
"""

# class dog(object):
#     __tooth = 100
#
#     @classmethod
#     def get_tooth(cls):
#         return cls.__tooth
#
#
# a = dog()
# result = a.get_tooth()
# print(result)

class dog(object):
    tooth = 100

    @staticmethod
    def get_tooth():
        print('这是一个dog')

a = dog()
a.get_tooth()
dog.get_tooth()


