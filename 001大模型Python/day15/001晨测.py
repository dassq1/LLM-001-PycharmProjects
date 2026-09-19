"""
@Author:xuyinglai
@Date:2026/8/1
@DESC:
"""
import os
import time

"""
1. 进程和线程的对比

2.多线程多进程分别用于什么场景?

3.正则中的 search  match  findall split 分割什么区别


二、编程题

1. 使用multiprocessing模块创建两个进程，一个进程打印从 1 到 5 的数字，另一个进程打印从 6 到 10 的数字。
"""
import multiprocessing


def print_number(start, end):
    for i in range(start, end):
        print(f"我是进程{os.getpid()}，打印{i}", end=' *** ')
        time.sleep(5)
    print()


if __name__ == "__main__":
    p1 = multiprocessing.Process(target=print_number, args=(1, 5))
    p2 = multiprocessing.Process(target=print_number, args=(6, 10))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("两个进程执行完毕")
"""

2. 使用threading模块创建4个线程 卖1000张票 不能有重票和负票。

3.写一个正则 判断是否为 正确的手机号码 第一位是1第二位是3456789 后面任意
"""
import re

str1 = 16603760981
pattern = r"^1[3,4,5,6,7,8,9]\d{9}$"

"""
4.写一个正则 判断是否为 正确的邮箱  字母@字母.com zs@qq.com

"""
