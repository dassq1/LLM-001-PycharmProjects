"""
@Author:xuyinglai
@Date:2026/7/29
@DESC:今天交学费
"""


# def say_hello(func):
#     def wrapper(*args, **kwargs):
#         print("HELLO,开始计算")
#         res = func(*args, **kwargs)
#         return res
#
#     return wrapper
#
#
# def add(x, y):
#     res = x + y
#     print(f"相加的结果是{res}")
#     return res
#
#
# add_pro = say_hello(add)
# result = add_pro(10, 90)
# print(result)
##########################################################

# def say_hello(func):
#     def wrapper(*args, **kwargs):
#         print("HELLO,开始计算")
#         res = func(*args, **kwargs)
#         return res
#
#     return wrapper
#
#
# # @say_hello
# def add(x, y):
#     res = x + y
#     print(f"相加的结果是{res}")
#     return res
#
#
# result = add(10, 90)
# print(result)


########################################################################

# def say_hello(func):
#     def wrapper(*args, **kwargs):
#         print("HELLO,开始计算")
#         res = func(*args, **kwargs)
#         return res
#
#     return wrapper
#
#
# @say_hello('加法')
# def add(x, y):
#     res = x + y
#     print(f"相加的结果是{res}")
#     return res
# @say_hello
# def add(x, y):
#     res = x - y
#     print(f"相减的结果是{res}")
#     return res

##############################################################
# class SayHello:
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             print("准备开始计算")
#             return func(*args, **kwargs)
#
#         return wrapper
#
#
# @SayHello()
# def add(x, y):
#     res = x + y
#     print(f"{x}和{y}相加的结果是{res}")
#     return res
#
#
# # 手动
# # say = SayHello()
# # add = say(add)
# # result = add(10, 20)
# # print(result)
# # @语法糖
# print(add(1, 2))
####################################################
# todo 带参数的类装饰器
class SayHello:
    def __init__(self, msg):
        self.msg = msg

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print(f"准备开始{self.msg}计算")
            return func(*args, **kwargs)

        return wrapper


@SayHello("加法")
def add(x, y):
    res = x + y
    print(f"{x}和{y}相加的结果是{res}")
    return res


add(19, 99)
