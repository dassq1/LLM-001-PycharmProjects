"""
@Author:xuyinglai
@Date:2026/7/30
@DESC:
"""
import os
import time
from multiprocessing import Process

# print(os.cpu_count())
# print(os.getpid())

print("*", __name__)


def speak():
    for index in range(10):
        print(f"我在说话{index},进程pid是:{os.getpid()}")
        time.sleep(2)


def study():
    for index in range(15):
        print(f"我在学习{index},进程pid是:{os.getpid()}")
        time.sleep(2)


if __name__ == '__main__':
    p1 = Process(target=speak)
    p2 = Process(target=study)
    p1.start()
    p2.start()
