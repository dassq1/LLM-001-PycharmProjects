"""
@Author:xuyinglai
@Date:2026/7/29
@DESC:
"""


def outer():
    a = 1
    b = 2

    def inner():
        print(f"内部{a=},{b=}")

    return inner


inner_func = outer()
print(outer().__closure__)
print(inner_func.__closure__)
