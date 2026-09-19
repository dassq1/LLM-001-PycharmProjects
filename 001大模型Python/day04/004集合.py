"""
@Author:xuyinglai
@Date:2026/7/21
@DESC:随机产生[20,29]范围内的随机数

添加到一个集合内 要求数据不重复 集合存储10个值
"""
from random import randint

set1 = set()
count = 0
while len(set1) < 10:
    num = randint(20, 29)

    set1.add(num)
    count += 1
print(set1)
print(count)

# print(set1[0]) 'set' object is not subscriptable
