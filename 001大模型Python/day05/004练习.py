"""
@Author:xuyinglai
@Date:2026/7/22
@DESC:
"""


# (1) 获取任意个整数的和
def my_sum(*a):
    print(type(a))
    return sum(a)


print(my_sum(1, 2, 3, 4, 5, 6, 7, 8, 9))

'''

 (2) 获取任意个正整数的最大公约数
     6 4 8: 2
     7 5  
'''


def fun(*a):
    i = min(a)
    # print(i)
    # print(a)
    for i in range(i, 0, -1):
        for j in a:
            # print(j)
            if j % i != 0:
                break
        else:
            print(f"{i}是{a}de最大公约数")


fun(4, 18, 99, 8)
'''

（3）定义一个函数calculate，功能可以接收2个整数，及其任意个运算符，实现对这2个整数的计算。
    如果没有传入运算符，返回None
    calculate(1,2) 返回None
    calculate(1,2,"+") 返回3
    calculate(1,2,"+","-","*","/"), 返回[3,-1,2,0.5]
    如果做和除法相关操作时 除数为0
    calculate(1,0,"+","-","*","/","**"), 返回[1,1,0,"除数不能为0",1]'''


# def calculate(a, b, *c):
#     if not c:
#         return None
#     elif len(c) == 1:
#         return eval(f"{a}{c[0]}{b}")
#     elif len(c) == 2:
#         return eval(f"{a}{c[0]}{b}, {a}{c[1]}{b}")
#     elif len(c) == 3:
#         return eval(f"{a}{c[0]}{b}, {a}{c[1]}{b},{a}{c[2]}{b}")
#     for
#
# print(calculate(1, 2, "+", "*"))


def calculate(a, b, *ops):
    if not ops:
        return
    result_list = []
    for op in ops:
        try:
            res = eval(f"{a}{op}{b}")
        except ZeroDivisionError:
            res = "除数不能为0"
        result_list.append(res)
    return result_list


print(calculate(1, 2, "+"))
print(calculate(1, 2, "+", "*"))
