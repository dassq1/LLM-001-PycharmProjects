"""
@Author:xuyinglai
@Date:2026/7/24
@DESC:
"""


def fun(n: int):
    if n == 1:
        return 1
    return n * fun(n - 1)


num = int(input("输入一个整数："))
print(fun(num))
"""
2.猴子吃桃
    猴子吃桃:
    有一堆桃子猴子第一天吃了其中的一半,并多吃了一个,猴子以后每天都吃其中一半,然后再多吃一个,
    第十天要吃桃子的时候发现只剩一个桃子(即还没有吃),请问之前一共有多少个桃子?
    设第9天有x个桃子 
    设第8天有x个桃子
    设第7天有x个桃子
    设第6天有x个桃子"""


def fun(day: int):
    if day == 10:
        return 1
    return (fun(day + 1) + 1) * 2


print(fun(11))
