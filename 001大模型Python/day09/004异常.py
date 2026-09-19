# # """
# # @Author:xuyinglai
# # @Date:2026/7/27
# # @DESC:
# # """
# #
# #
# # def int_add(x, y):
# #     assert isinstance(x, int) and isinstance(y, int), "参数类型错误"
# #     return x + y
# #
# #
# # print(int_add(1, 2))
# # print(int_add(1, '2'))
# print(10 * '%')
# try:
#     a = int(input("请输入第一个数："))
#     b = int(input("请输入第二个数："))
#     result = a / b
#     print(f"{a}除以{b}的结果是{result}")
# except ZeroDivisionError as e:
#     print("0不能为除数", e)
# except ValueError as e:
#     print("必须输入数字", e)
# print(issubclass(ZeroDivisionError, ArithmeticError))
# print(issubclass(ZeroDivisionError, Exception))
# print(issubclass(ValueError, Exception))
# print(issubclass(KeyboardInterrupt, Exception))
# print(issubclass(KeyboardInterrupt, BaseException))
# region
# try:
#     a = int(input("请输入第一个数 "))
#     b = int(input("请输入第二个数 "))
#     result = a / b
#     print(f"{a}除以{b}的结果是{result}")
# except (ZeroDivisionError, ValueError, Exception) as e:
#     if isinstance(e, ZeroDivisionError):
#         print("程序异常", e)
#     elif isinstance(e, ValueError):
#         print("程序异常", e)
#     else:
#         print("出现异常", e)
#
# print("Hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
# endregion
'''
完整写法
1.try：尝试去做可能会出现异常的事情。
2.except：出现异常时的处理（出现异常时怎么补救）。
3.else：如果一切顺利（没有异常出现）要做的事。
4.finall：无论有没有异常，都要做的事。'''


# region
# try:
#     a = int(input("输入第一个数 "))
#     b = int(input("输入第二个数 "))
#     result = a / b
#     print(f"{a}除以{b}的结果是{result}")
# except(ZeroDivisionError, ValueError, Exception) as e:
#     if isinstance(e, ZeroDivisionError):
#         print("程序异常", e)
#     elif isinstance(e, ValueError):
#         print("必须输入数字", e)
#     else:
#         print(f"程序异常", e)
# else:
#     print("一切顺利，没有异常")
# finally:
#     print("不管出没出现异常，都会执行")
# endregion
# 手动抛出异常
# region
# try:
#     age = int(input("请输入年纪 "))
#     if 18 <= age <= 120:
#         print("成年")
#     elif 0 <= age < 18:
#         print("未成年")
#     else:
#         raise ValueError("年龄应该是0~120之间的整数", ValueError)
# except Exception as e:
#     print(f"程序异常", e)
# endregion
class SchoolNameError(Exception):
    def __init__(self, msg):
        super().__init__("【校名异常】" + msg)


def check_school_name(name):
    if len(name) > 10:
        raise SchoolNameError(f"'{name}'学校名过长")
    else:
        print("学校名合法的")


try:
    check_school_name('asdfghj2345678234')
except SchoolNameError as e:
    print(f"程序异常", e)
