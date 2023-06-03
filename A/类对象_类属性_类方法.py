# -*- coding:utf-8 -*-
# f = open('E:\test\�����ĵ�.txt','w+','encoding')
# print(f.)
# #f.write()
# f.close()

"""
�����?
������
�෽��
    ʲôʱ�����෽��������������Ҫʹ������󣬻���˽����������?
    ������
    ����˽��������
    �����෽��
    ͨ����������˽��������
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
        print('����һ��dog')

a = dog()
a.get_tooth()
dog.get_tooth()



