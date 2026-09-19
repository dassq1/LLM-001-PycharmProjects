"""
@Author:xuyinglai
@Date:2026/7/30
@DESC:
"""
import time
from multiprocessing import Process


# 定义任务函数1
class EvenProcess(Process):
    def __init__(self, start, end):
        self.start_num = start if start % 2 == 0 else start + 1
        self.end = end
        super().__init__()

    def run(self):
        for i in range(self.start_num, self.end, 2):
            print("even", i)
            time.sleep(1)


# 定义任务函数2
class OddProcess(Process):
    def __init__(self, start, end):
        self.start_num = start if start % 2 != 0 else start + 1
        self.end = end
        super().__init__()

    def run(self):
        for i in range(self.start_num, self.end, 2):
            print("odd", i)
            time.sleep(1)


if __name__ == "__main__":
    print("主程序")
    # print_even(1, 100)
    p1 = EvenProcess(1, 100)
    p2 = OddProcess(1, 100)
    p1.start()
    p2.start()
