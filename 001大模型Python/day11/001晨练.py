"""
@Author:xuyinglai
@Date:2026/7/29
@DESC:
"""
"""
    0.闭包有什么作用?如何实现闭包?

    1.一共有几种作用域:
      global  nonlocal分别有什么作用
     __name__的值是什么

    2.创建一个简单的 Python 模块math_operations.py，
    其中定义两个函数add和multiply，分别用于实现两个数的加法和乘法运算。
    在Morning.py 文件中导入该模块，并调用这两个函数计算3 + 5和3 * 5的结 果。
"""

"""

    3.键盘输入出生日期 年月日 计算一共出生了多少天
    请您输入出生日期
    2000-09-08
    从出生到现在一共过了xxxx天
"""
# from datetime import datetime, date
#
# date1 = input("请您输入出生日期:")
# date11 = datetime.strptime(date1, "%Y-%m-%d")
# date11 = date11.date()
# date2 = date.today()
# delta = date2 - date11
# print(delta)
# print(f"从出生到现在一共过了{delta.days}天")

"""
    4.words = ['apple', 'banana', 'cherry', 'date', 'apricot']
    按照名字的首字母进行分组 提示: defaultdict(list)
    # 输出: {'a': ['apple', 'apricot'], 'b': ['banana'], 'c': ['cherry'], 'd': ['date']}
"""
from collections import defaultdict

words = ['apple', 'banana', 'cherry', 'date', 'apricot']
# TODO: 创建一个默认值为列表的字典
group_dict = defaultdict(list)

# TODO: 遍历每个单词，按首字母放入对应的组
for word in words:
    # word[0] 取出第一个字符（即首字母）
    # 如果该首字母还没出现过，group_dict[word[0]] 会自动变成 []，然后 append
    # 如果该首字母已经出现过，直接 append 到已有的列表末尾
    # group_dict[word[0]].append(word)
    first_char = word[0]
    list1 = group_dict[first_char]
    list1.append(words)
# TODO: 为了方便阅读，将 defaultdict 转成普通 dict 打印（符合题目要求的输出格式）
print(dict(group_dict))
# 输出: {'a': ['apple', 'apricot'], 'b': ['banana'], 'c': ['cherry'], 'd': ['date']}
