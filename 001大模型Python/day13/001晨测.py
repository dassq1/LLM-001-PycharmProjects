"""
@Author:xuyinglai
@Date:2026/7/31
@DESC:
"""
import random
import string

"""
0. 什么是装饰器 迭代器 生成器
"""

"""

1. 使用生成器生成指定数量个斐波那契数 并测试
"""


def func(size):
    a, b = 1, 1
    count = 0
    while count < size:
        yield a
        a, b = b, a + b
        count += 1


s = func(10)
for i in s:
    print(i)
"""


2. 创建一个迭代器类MyIterator，用于获取指定数量个偶数
"""


class MyIterator:
    def __init__(self, size):
        self.count = 0
        self.start = 0
        self.size = size

    def __iter__(self):
        return self

    def __next__(self):
        result = self.start
        self.count += 1
        if self.count > self.size:
            raise StopIteration

        self.start += 2
        return result


m = MyIterator(5)
# print(m.__next__())
# print(m.__next__())
for i in m:
    print(i)
"""


3.定义一个装饰器 添加后 执行函数 所有的字母都是大写
        def hello():
            从小写字母中随机获取5个值 拼接为字符串
            return 字符串
        使用装饰器 将字母转为大写
"""


#
# def f_decorator(func):
#     print("使用装饰器")
#
#     def wrapper(x):
#         x = x.lower()
#
#
#     return wrapper
# @f_decorator
def hello():
    x = string.ascii_lowercase
    res = random.choices(x, k=5)
    return ''.join(res)

# print(hello())
