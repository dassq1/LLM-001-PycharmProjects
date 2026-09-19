"""
@Author:xuyinglai
@Date:2026/7/20
@DESC:
"""
import math

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f"{j} * {i} = {i * j}\t", end='')
#     print()
# for i in range(1, 7):
#     print(" " * (6 - i), end=" ")
#     print("* " * i)
# for i in range(1, 7):
#     print(" " * i, end=" ")
#     print("* " * (6 - i))


num = int(input("输入一个数:"))
p = int(math.sqrt(num))

for i in range(2, p + 1):
    if num % i == 0:
        print(f"{num}不是质数")
        break
else:
    print(f"{num}是质数")
