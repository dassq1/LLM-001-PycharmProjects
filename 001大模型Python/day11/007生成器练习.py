"""
@Author:xuyinglai
@Date:2026/7/29
@DESC:
"""
"""1.使用生成器获取指定数量个斐波那契数
"""


def func(size):
    a, b = 1, 1
    count = 0

    while count < size:
        yield a
        a, b = b, a + b
        count += 1


s = func(5)
# print(func(2))
for i in s:
    print(i)

"""
2.使用生成器.send() 改变数据
   定义一个函数返回数字
   步长默认为 1 
   send(none) 1
   send(none) 2
   send(none) 3
   send(2) 6
   send(none) 9
   send(none) 12
   send(3) 18
   send(none) 24
"""

print(8 * "*")


def number_generator():
    """
    生成器
    :return:
    """
    step = 1
    num = 0
    while True:
        received = yield num
        if received is not None:
            step += received
        num += step


gen = number_generator()
print(gen.send(None))
print(gen.send(1))
