"""
@Author:xuyinglai
@Date:2026/7/30
@DESC:生成器是简化版的迭代器
"""
from collections.abc import Iterator


def show():
    print("XUXUXUX")
    yield 20


result = show()
print(result)
print(isinstance(result, Iterator))
print(result.__next__())

############################################
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")


def get_num():
    print("李白")
    yield
    print("杜甫")
    yield 20
    print("王安石")
    yield 30


n = get_num()
print(n)
print(n.__next__())
print(next(n))
##################################
print("&&&&&&&&&&&&&&&&使用生成器获取指定个数的偶数&&&&&&&&&&&&&&&&&")


def get_even_count(size):
    """
    获取size个偶数
    :param size:
    :return:
    """
    start = 0
    count = 0
    while count < size:
        yield start
        start += 2
        count += 1


g = get_even_count(5)
print(g)
for i in g:
    print(i)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
