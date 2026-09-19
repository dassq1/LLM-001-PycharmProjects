"""
@Author:xuyinglai
@Date:2026/7/31
@DESC:
"""
import multiprocessing
import time

"""
主进程向一个文件内不断的写入数据 写一行就换行 log.txt hello hello

f.flush() 及时落盘
子进程 不断的读取写入的数据 查看一共写了多少行并输出 等主进程不写入时 自动结束
"""


def write_file():
    with open("log.txt", 'w') as f:
        for i in range(10):
            f.write("HELLO\n")
            f.flush()
            print(f"写程序，已经写了{i + 1}行")
            time.sleep(1)
    print("写程序结束")


def read_file():
    time.sleep(0.5)
    with open("log.txt", 'r') as f:
        while True:
            print(f.read(1), end='')


if __name__ == "__main__":
    p1 = multiprocessing.Process(target=write_file)
    p2 = multiprocessing.Process(target=read_file)

    p1.start()
    p2.start()
