# 烤地瓜程序
"""
提取属性：烤的时间，状态、调料
提取方法：根据烧烤时间决定红薯是生的还是熟的；传入时间，修改时间属性值，根据时间修改红薯状态。定义调料方法，传入调料追加调料列表
定义__str__方法，print实例时触发__str__方法return 红薯的情况
"""

class Sweet_Potato():
    def __init__(self):
        self.cook_time = 0
        self.potato_state = '生的'
        self.fixings = []

    def cook_potato(self, time):
        self.cook_time = time
        if 0 <= self.cook_time <= 3:
            self.potato_state = '生的'
        elif 3 <= self.cook_time < 5:
            self.potato_state = '半生不熟'
        elif 5 <= self.cook_time <= 8:
            self.potato_state = '熟了'
        elif 8 < self.cook_time:
            self.potato_state = '烤娇了'

    def add_fixing(self, fixing):
        self.fixings.append(fixing)

    def __str__(self):
        return f'地瓜烤了{self.cook_time}分钟,状态:{self.potato_state},里边放了{self.fixings}'


potato = Sweet_Potato()
potato.cook_potato(9)
potato.add_fixing('孜然')
print(potato.fixings)