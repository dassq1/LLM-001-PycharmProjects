"""
@Author:xuyinglai
@Date:2026/7/30
@DESC:# 创建Process类对象
"""
import time
from multiprocessing import Process


# 定义任务函数1
def print_even(start, end):
    start = start if start % 2 == 0 else start + 1
    for i in range(start, end, 2):
        print(f"偶数{i}")
        time.sleep(1)


# 定义任务函数2
def print_odd(start, end):
    start = start if start % 2 != 0 else start + 1
    for i in range(start, end, 2):
        print(f"奇数{i}")
        time.sleep(1)


#
# if __name__ == "__main__":
#     print("主程序")
#     # print_even(1, 100)
#     p1 = Process(target=print_even, args=(1, 100))
#     p2 = Process(target=print_odd, args=(1, 100))
#     p1.start()
#     p2.start()
#######################################$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$##############
import os

print("******************************************")
