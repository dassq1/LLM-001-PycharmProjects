"""
@Author:xuyinglai
@Date:2026/7/21
@DESC:


1.break有什么作用

2.continue有什么作用

3.输出2~100内质数
4.附加  可乐3元一瓶 一个瓶子换1块钱 20元最多买几瓶可乐
  思路: 1.一次买一瓶
       2.一次购买当前钱数的最多瓶子数
"""
from math import sqrt

for i in range(2, 101):
    for j in range(2, int(sqrt(i)) + 1):
        if i % j == 0:
            break
    else:
        print(i, end=" ")
print("*" * 100)
a = 20

i = a % 3
j = a // 3
count = 0
while i + j // 3 + i + j % 3 >= 3:
    count += j
    a = i + j
    i = a % 3
    j = a // 3
    if j == 0:
        break

print(count)
