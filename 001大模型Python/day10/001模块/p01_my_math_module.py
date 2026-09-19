"""
@Author:xuyinglai
@Date:2026/7/28
@DESC:数学计算模块
"""
__all__ = ['add', 'subtract', 'multiply', 'divide', '_remainder']


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def _remainder(a, b):
    return a % b


if __name__ == "__main__":
    print(__name__, "现在主模块，执行下面的测试代码", type(__name__))
    print(_remainder(2027, 4))
