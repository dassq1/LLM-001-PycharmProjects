"""
@Author:xuyinglai
@Date:2026/7/22
@DESC:
"""


#
# def printInfo(num, **vardict):
#     print(num)
#     print(vardict)
#
#
# # return
#
# printInfo(10, key1=20, key2=30)
# printInfo(10, a=20, b=30)
def func(a, b, c):
    return a + b + c


tuple1 = (1, 2, 3)
print(func(*tuple1))
tuple2 = (1, 2, 3)
print(func(*tuple2))
