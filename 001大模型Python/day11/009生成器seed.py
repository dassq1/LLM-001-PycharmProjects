"""
@Author:xuyinglai
@Date:2026/7/30
@DESC:
"""


def show_info():
    print("吴亦凡")
    value = yield 10

    print(f"{value} 李易峰")
    value = yield 20

    print(f"{value} 蔡徐坤")
    value = yield 30

    print(f"{value} 罗志祥")


g = show_info()
print(g.send(None))

print(g.send("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAa"))
