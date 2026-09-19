"""
@Author:xuyinglai
@Date:2026/7/22
@DESC:
"""
import math


def juxing(a, b):
    for i in range(1, a + 1):
        print("*" * b)


x = int(input("输入行数:"))
y = int(input("输入列数:"))
juxing(x, y)


def is_num(a):
    if a % 3 == 0:
        return True
    else:
        return False


num = int(input("请输入一个数"))
falg = is_num(num)
if falg:
    print("能被3整除")
else:
    print("不能被3整除")


def id_prime(a):
    for i in range(2, int(math.sqrt(a) + 1)):
        if a % i == 0:
            return False
    else:
        return True


num = int(input("输入一个数"))
f = id_prime(num)
if f:
    print("是")
else:
    print("不是")
####################################################
"""
1.定义一个打印矩形的函数接收两个参数 行,列
   2 3 打印 2 行3列矩形
   3 5 打印 3行 5列的矩形

2.定义一个函数 接收一个数 判断是否能被3整除 如果可以 返回 true 否则返回false

3.定义一个函数 判断是否为质数 是 返回true  不是返回 false
"""
'''
1.定义一个打印矩形的函数接收两个参数 行,列
   2 3 打印 2 行3列矩形
   3 5 打印 3行 5列的矩形
'''


def print_rectangle(row, col):
    for i in range(row):
        for j in range(col):
            print("*", end="")

        print()


print_rectangle(2, 3)
print_rectangle(3, 5)

'''
2.定义一个函数 接收一个数 判断是否能被3整除 如果可以 返回 true 否则返回false
'''


def is_three(num):
    # if num % 3 == 0:
    #     return True
    # else:
    #     return False
    # return  True if num%3==0 else False
    return num % 3 == 0


print(is_three(9))

print("------")
'''
3.定义一个函数 判断是否为质数 是 返回true  不是返回 false
7 
2 3 4 5 6
10 
2 3 4 5 6 7 8 9
'''


def is_prime(num):
    # 确定1和本身之外的约数范围
    for i in range(2, num):
        if num % i == 0:
            return False

    return True


result = is_prime(10)

print(result)

print(is_prime(7))
