"""
@Author:xuyinglai
@Date:2026/7/28
@DESC:打印矩形
"""


def print_rectangle(width, height):
    for i in range(height):
        for j in range(width):
            print("*", end="")
        print()


def print_diamond(lines):
    if lines % 2 == 0:
        raise ValueError("lines必须是奇数")
    center = int(lines // 2)
    for i in range(lines):
        for j in range(lines):
            if abs(i - center) + abs(j - center) <= center:
                print("*", end="")
            else:
                print(" ", end="")
        print()


def multiply(a, b):
    """
    类似图形打印，而不是数值计算
    :param a:
    :param b:
    :return:
    """
    print(f"{a}" * b)
