"""
@Author:xuyinglai
@Date:2026/7/31
@DESC:2. Pipe
A进程随机发送一个数字 [1,100]
B进程随机发送一个字母 [A-Z]
两个进程互相接收对方发送的信息,将收到的数据写到磁盘内
"""
import random
import string
from multiprocessing import Process, Pipe


def process_a(conn):
    for _ in range(5):
        num = random.randint(1, 100)
        conn.send(num)
        print(f"[A]进程发送数字{num}")
        reversed = conn.recv()
        print(f"[A]收到的字母{reversed}")

        with open("A_received.txt", 'a', encoding="utf-8") as f:
            f.write(f"{reversed}\n")
    conn.close()


def process_b(conn):
    for _ in range(5):
        letter = random.choice(string.ascii_letters)
        conn.send(letter)
        print(f"[B]发送字母{letter}")

        reversed = conn.recv()
        print(f"[B]收到数字{reversed}")
