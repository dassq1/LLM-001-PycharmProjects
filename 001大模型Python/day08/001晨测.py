"""
@Author:xuyinglai
@Date:2026/7/25
@DESC:
"""
from heapq import nlargest

'''
0.集合的存储特点
  定义两个集合 求 交 并  差 对称差集
'''
set1 = {1, 2, 3, 4, 5, 6}
set2 = {10, 9, 8, 7, 6, 5}
set3 = set1 & set2
print(set3)
print(set1 | set2)
print(set1 - set2)
print(set2 - set1)
print(set1 ^ set2)
print(set1.symmetric_difference(set2))
'''
1.什么样的函数是匿名函数 有什么作用 语法结构是什么
答：由lambda关键字创建的没有函数名称和return的函数，lambda 形参列表：表达式 
    常作为sorted map filter reduce 等高阶函数的参数，简化代码，无需单独定义命名函数
'''
person_data = [
    {"name": "安琪拉", "age": 26, "salary": 15001},
    {"name": "米莱迪", "age": 27, "salary": 14002},
    {"name": "妲己", "age": 29, "salary": 15009},
    {"name": "虞姬", "age": 22, "salary": 13006},
    {"name": "小乔", "age": 21, "salary": 15003}
]
# 获取薪资最高的3个员工信息
p = nlargest(3, person_data, key=lambda x: x['salary'])
print(p)
'''
 排序 首先按照年龄从大到小 再按照薪资从小到大
'''
p2 = sorted(person_data, key=lambda x: (-x['age'], x['salary']))
print(p2)
'''


4.定义一个名为 Dog 的类，该类有两个实例属性 name（名字）和 age（年龄），以及一个方法 bark（叫），bark 方法打印出 "Woof! "。
  定义一个静态方法 能获取任意整数的偶数和
  创建一个 Dog 类的对象，并调用 bark 方法。
  调用求和的方法
 扩展：在bark 方法中打印"Woof! My name is [name] and I am [age] years old."，其中name和age访问实例属性
'''


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name}Woof!我今年 {self.age}岁了")

    @classmethod
    def get_sum(cls, *args):
        count = 0
        for i in args:
            if i % 2 == 0:
                count += i

        return count


d1 = Dog("旺财", 10)
d1.bark()
print(Dog.get_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
