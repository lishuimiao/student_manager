"""
异常处理
try:
    可能发生错误的代码
except Exception as result:：
    如果捕获到该异常类型执行的代码
else: #没有发生错误执行
    print('没有错误执行')
finally: 不管有没有捕获错误都执行
    f.close()
"""
# try:
#     f = open('/Users/samlee/Documents/日报/和尚.txt', 'r')
# except Exception as result:
#     f = open('/Users/samlee/Documents/日报/和尚.txt', 'w')
# else:
#     print('没错报哦')
# finally:
#     f.close()
"""
try嵌套
1. 尝试只读方式打开test.txt文件，如果文件存在则读取文件内容，文件不存在则提示用户即可。
2. 读取内容要求：尝试循环读取内容，读取过程中如果检测到用户意外终止程序，则`except`捕获异常并提示用户。
"""
import time


try:
    f = open('/Users/samlee/Documents/日报/今日内容.txt')
    try:
        while True:
            data = f.readline()
            if len(data) == 0:
                break
            time.sleep(2)
            print(data)
    except Exception as result:
        print('你又异常了')

except Exception as result:
    print('异常了喂')

"""
自定义异常
1.定义异常类，设置异常描述信息
2.定义功能，触发问题抛出异常对象，捕获异常描述
"""
# 1. 自定义异常类， 继承Exception， 魔法方法有init和str(设置异常描述信息)
class ShortInputError(Exception):
    def __init__(self, length, min_len):
        # 用户输入的密码长度
        self.length = length
        # 系统要求的最少长度
        self.min_len = min_len

    # 设置异常描述信息
    def __str__(self):
        return f'您输入的密码长度是{self.length}, 密码不能少于{self.min_len}'


def main():
    # 2. 抛出异常: 尝试执行：用户输入密码，如果长度小于3，抛出异常
    try:
        password = input('请输入密码：')
        if len(password) < 3:
            # 条件满足，抛出异常类创建的对象
            raise ShortInputError(len(password), 3)  #类名()就是传入参数创建类对象
    # 3. 捕获该异常
    except Exception as result:
        print(result)
    else:
        print('没有异常，密码输入完成')


main()


