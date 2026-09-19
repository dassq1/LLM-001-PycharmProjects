"""
@Author:xuyinglai
@Date:2026/7/31
@DESC:
"""
import math


def func(list1):
    result = 0
    for i in list1:
        result += i if i % 2 == 0 else 0

    return result


num = [1, 2, 3, 4, 5, 6, 7]
print(func(num))
print("***********2.编写一个程序，读取用户输入的一个整数，判断它是否为质"
      "数。如果是质数，输出 “是质数”；否则输出 “不是质数”。********************")


def func(num):
    if num <= 1:
        print(f"{num}不是质数")
        return
    for i in range(2, int(math.sqrt(num) + 1)):

        if num % i == 0:
            print(f"{num}不是质数")
            return

    print(f"{num}是质数")


# num = int(input("输入一个整数："))
# func(num)

print("*******************3.编写一个函数，接受两个字符串作为参数，"
      "返回这两个字符串拼接后的结果，并且将拼接后的字符串中的所有字母转换为大写。*********************")
import string


def func(str1, str2):
    res = str1 + str2
    return res.upper()


print(func("123", "hello"))
print("*******************4.编写一个程序，"
      "生成一个包含 1 到 100 之间所有能被 3 整除但不能被 5 整除的整数的列表，"
      "并输出该列表。******************")
list1 = []
for i in range(1, 100):
    list1.append(i) if i % 3 == 0 and i % 5 != 0 else ""

print(list1)

print("*******5.编写一个函数，"
      "接受一个字典作为参数，字典的键是商品名称，值是商品价格。"
      "函数返回价格最高的商品名称。*****************")


def func(dict1):
    return max(dict1, key=lambda k: dict1[k])


def func2(dict1):
    if not dict1:
        return "为空"
    list2 = [(price, name) for name, price in dict1.items()]
    max_tuple = max(list2)
    print(max_tuple)
    return max_tuple[1]


dict1 = {"苹果": 5.5, "香蕉": 3.2, "榴莲": 28.8, "橙子": 4.0}
print(func(dict1))
