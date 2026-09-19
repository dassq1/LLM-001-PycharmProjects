"""
@Author:xuyinglai
@Date:2026/7/24
@DESC:
"""
import math
from functools import reduce
from heapq import nlargest, nsmallest

"""
练习题1：
    定义函数 calculate(num, func):
                return func(num)
    定义匿名函数作为参数传给calculate，分别实现求绝对值、平方根、四舍五入保留最多两位小数
    提示：内置函数 abs,round(小数,保留的位数),"""


def calculate(num, func):
    return func(num)


def operator1(o):
    match o:
        case "abs":
            return lambda num: abs(num)
        case "sqort":
            return lambda num: math.sqrt(num)
        case "round":
            return lambda num: round(num, 2)


f1 = operator1("round")
print(f1(12.123456))
"""
练习题2：
    现有一组数据如下：[, {...}{"name":"lily", "age":26, "salary": 15000}, {...},{...}]
    数据自己随意。
    通过匿名函数作为参数传给sorted，filter，map，reduce，nlargest,nsmallest等，分别实现
    （1）按照薪资从高到低排序
    （2）找出薪资前3高的员工
    （3）找出薪资低于15000的员工
    （4）求所有员工的薪资总和
    （5）找出年龄最小的员工
"""

stu_list = [{"name": "lily", "age": 26, "salary": 15000},
            {"name": "张三", "age": 22, "salary": 990000},
            {"name": "李四", "age": 18, "salary": 99004},
            {"name": "王五", "age": 21, "salary": 99008},
            {"name": "赵六", "age": 19, "salary": 9904},
            {"name": "陈一", "age": 28, "salary": 99002}
            ]
p1 = sorted(stu_list, key=lambda x: x['salary'], reverse=True)
print(p1)
p2 = nlargest(3, stu_list, key=lambda x: x['salary'])
print(p2)

p3 = filter(lambda x: x["salary"] <= 15000, stu_list)
print(list(p3))
p4 = reduce(lambda x, y: x + y['salary'], stu_list, 0)
print(p4)
p5 = nsmallest(1, stu_list, key=lambda x: x['age'])
print(p5)
