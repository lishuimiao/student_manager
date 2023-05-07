"""
需求：将小于房子面积的家具搬进房屋内
分析：涉及到2个事物：房子、家具，拟2个类
房子类：
    实例属性：
            房子位置
            房子面积
            剩余面积
            房子内家具(列表)
    房子方法：方法1：添加家具
            1.添加家具到房屋
            2.判断家具面积<房屋，append(家具对象.name)，添加家具到家具列表
            3.房屋剩余面积-掉家具占用面积

            方法2：__str__ 打印对象信息

    显示房屋信息，也就是实例信息
家具类：
    实例属性：
            名称
            面积
添加家具流程：
    1.使用家具类实例一件家具
    2.使用房子类实例化一个加
"""


class Furniture():
    def __init__(self, area, name):
        self.name = name
        self.area = area


class home():
    def __init__(self, location, area):
        self.location = location
        self.area = area
        self.free_area = area
        self.Furniture_list = []

    def add_Furniture(self, safa):
        if self.free_area >= safa.area:
            self.Furniture_list.append(safa.name)
            self.free_area -= safa.area
            print(self.area)
        elif safa.area > self.free_area:
            print('放不进去了')

    def __str__(self):
        return f'房子面积{self.area},房子里的家具：{self.Furniture_list},房屋剩余面积为：{self.free_area}'


safa = Furniture(name='safa', area=10)
my_home = home('广州', 100)
my_home.add_Furniture(safa)
print(my_home)
