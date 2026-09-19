"""
@Author:xuyinglai
@Date:2026/7/24
@DESC:
"""
"""
0.参数的传递形式有哪几种?使用时有什么注意点

1.创建一个集合，包含数字 1 到 5 。再创建一个字典，键为集合中的数字，值为该数字的立方。
"""
set1 = {1, 2, 3, 4, 5}
dict1 = {x: x ** 3 for x in set1}
print(dict1)

"""

2.定义一个函数 cal，它接受两个整数参数 a 和 b，返回这两个数的商和余数，
  并调用该函数计算 15和4的商和余数。如果b为0，则商和余数为None
"""


def cal(a: int, b: int):
    if b:
        return (a // b, a % b)
    else:
        return (None, None)


print(cal(15, 4))
"""

3.定义一个函数 greet，它接受一个字符串参数 name，并且有一个默认参数 message，
默认值为 "Hello"，函数功能是打印出问候语，如 "Hello, Alice"。
调用该函数时，分别传入和不传入 message 参数进行测试。
  
"""


def greet(name, message="Hello"):
    return (f"{name},{message}")


print(greet("Alice"))
print(greet("Alice", "你好"))

"""

4.定义一个函数 find_all_even，它接受任意数量的整数参数，返回所有参数中的偶数。例如调用 find_all_even(1, 2, 3, 4, 5) 应返回 [2,4]。

"""


# def find_all_even(*a):
#     result = []
#     for i in a:
#         if i % 2 == 0:
#             result.append(i)
#     return result
def find_all_even(*a):
    return [x for x in a if x % 2 == 0]


print(find_all_even(1, 2, 3, 4, 5, 6))
