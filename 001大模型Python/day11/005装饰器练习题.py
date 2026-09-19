"""
@Author:xuyinglai
@Date:2026/7/29
@DESC:
"""
import math

"""
一.定义一个函数接收一个整数 返回开平方结果
   对当前函数进行功能增强 传递负数时将负数变为正数 
    再获取开平方
"""


def f_decorator(func):
    print("使用装饰器的拓展功能")

    def wrapper(x):
        res = math.sqrt(abs(x))
        return res

    return wrapper


@f_decorator
def func(a):
    return math.sqrt(a)


print(func(-9))
print("**************************************")
############################################################
# def f_decorator(func):
#     def inner(a):
#         if a < 0:
#             a = abs(a)
#         result = func(a)
#
#         return result
#
#     return inner
#
#
# def func(a):
#     return a ** 0.5


func = f_decorator(func)
# print(func(9))
# print(func(-9))
"""


二.
背景：
    你有一个明星列表 list1，里面存了多个明星的信息（id、姓名、年龄）。
    你需要写一个函数 find_star(id)，它根据用户传入的 id，在列表中查找对应的明星信息。
    list1 = [
        {"id":1,"name":"yangmi","age":18},
        {"id":2,"name":"zhaoliying","age":18},
        {"id":3,"name":"liushishi","age":28},
        {"id":4,"name":"dilireba","age":38},
        {"id":5,"name":"gulinazha","age":48},
    ]

问题：
    如果在没有优化的情况下，每次调用 find_star，都要从头到尾遍历列表，效率较低。
    请设计一个装饰器 cache_decorator，对 find_star 进行增强，使得：

    当用户第一次查询某个 id 时，正常遍历列表并返回结果，同时把结果缓存起来。

    当用户再次查询同一个 id 时，不再遍历列表，而是直接从缓存中获取结果，并打印提示 "找到了用户，缓存命中了"。

    当用户查询的是第一次查找的 id 时，打印 "找到了用户，循环遍历找到了"，表示是通过遍历查找的。

要求：
    装饰器内部要维护一个字典 cache，用来存储已经查询过的 id 及其对应的明星信息。

    装饰器的内部函数 wrapper 要接收 *args, **kwargs，并根据第一个参数（即 id）判断是否在缓存中。

    如果缓存命中，直接返回结果；否则，调用原函数获取结果，存入缓存，再返回。

示例输入输出：
2
缓存中没有id 2数据 走列表查询
{'id': 2, 'name': 'zhaoliying', 'age': 18}
缓存中没有id 1数据 走列表查询
{'id': 1, 'name': 'yangmi', 'age': 18}
1 缓存命中了
{'id': 1, 'name': 'yangmi', 'age': 18}
缓存中没有id 9数据 走列表查询
没有此id:9的用户
"""


def cache_decorator(func):
    cache = {}

    def wrapper(*args, **kwargs):
        if args:
            key = args[0]
        else:
            key = kwargs.get('id')

        if key in cache:
            print(f"{key}缓存命中")
            return cache[key]
        else:
            print(f"缓存未命中id={key}，列表查询")
        result = func(*args, **kwargs)
        cache[key] = result
        return result

    return wrapper


stars = [
    {"id": 1, "name": "yangmi", "age": 18},
    {"id": 2, "name": "zhaoliying", "age": 18},
    {"id": 3, "name": "liushishi", "age": 28},
    {"id": 4, "name": "dilireba", "age": 38},
    {"id": 5, "name": "gulinazha", "age": 48},
]


@cache_decorator
def find_star(uid):
    for star in stars:
        if star['id'] == uid:
            print("循环遍历找到了")
            return star
    print(f"没有这个id{uid}的人")


print(find_star(1))
# print(find_star(1))
