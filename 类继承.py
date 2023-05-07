"""
类的继承
1.子类继承父类方法属性时，若多个父类方法属性名称一致，子类对象调用方法属性时优先调用第一个父类的方法属性，可以调整子类继承括号中的顺序调整
2.若子类的方法属性名称与父类的方法属性名称一致时，优先使用子类的方法属性
3.若子类想要同时使用自己的方法属性，也能使用父类的方法属性，则需要在子类中定义方法，调用父类初始化方法再调用具体方法 父类._init_(self) 不初始化
怎么用呢
4.如果需要再调用自己的方法，若先调用了父类方法再调用子类方法，则子类方法需要重新初始化，不然有被覆盖问题。在子类具体方法下重新调用子类初始化方法
5.多重继承：C继承了 A、B两个类，当D继承C时同时继承了ABC的方法属性
"""


# class Master(object):
#     def __init__(self):
#         self.Mifang = '[煎饼果子]'
#
#     def make_cake(self):
#         print(f'使用秘方{self.Mifang}制作绝世大饼')
#
#
# class xdf_school(object):
#     def __init__(self):
#         self.Mifang = '[摊饼]'
#
#     def make_cake(self):
#         print(f'使用秘方{self.Mifang}制作绝世摊饼')
#
#
# class Prentice(Master, xdf_school):
#     def __init__(self):
#         self.Mifang = '[榴莲披萨]'
#
#     def make_cake(self):
#         self.__init__()
#         print(f'使用独家秘方配置{self.Mifang}')
#
#     def master_cake(self):
#         Master.__init__(self)
#         Master.make_cake(self)
#
#     def xdf_cake(self):
#         xdf_school.__init__(self)
#         xdf_school.make_cake(self)
#
#
# class tusun(Prentice):
#     pass


# zhangsan = tusun()
# zhangsan.make_cake()
# zhangsan.master_cake()

"""私有方法"""
class Master(object):
    def __init__(self):
        self.Mifang = '[煎饼果子]'

    def make_cake(self):
        print(f'使用秘方{self.Mifang}制作绝世大饼')


class xdf_school(Master):
    def __init__(self):
        self.Mifang = '[摊饼]'

    def make_cake(self):
        print(f'使用秘方{self.Mifang}制作绝世摊饼')


class Prentice(xdf_school):
    def __init__(self):
        self.Mifang = '[榴莲披萨]'
        self.__money = 1000000

    def __info_print(self):
        print(f'我的存款有：{self.__money}不给你哦')

    def get_money(self):
        return self.__money

    def set_money(self, money):
        self.__money = money

    def make_cake(self):
        self.__init__()
        print(f'使用独家秘方配置{self.Mifang}')

    def master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)

    def xdf_cake(self):
        xdf_school.__init__(self)
        xdf_school.make_cake(self)


class tusun(Prentice):
    pass



zhangsan = Prentice()
#
zhangsan.set_money(50)
print(zhangsan.get_money())