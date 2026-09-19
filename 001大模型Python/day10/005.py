"""
@Author:xuyinglai
@Date:2026/7/28
@DESC:
"""
import random

"""
题目要求：编写一个函数，生成指定长度的随机验证码，要求：
    1. 验证码包含大写字母、小写字母和数字；
    2. 长度由用户输入指定（范围：4-8 位）；
    3. 确保每个验证码中至少包含 1 个大写字母、1 个小写字母和 1 个数字；
    4. 输出生成的验证码。
    5.统计每一个字母出现的次数
    6. 如果长度不符合要求 抛出一个自定义异常 CountError 对异常进行捕获 
"""
# region
# import random
# from collections import defaultdict
#
#
# def fun(a):
#     d = defaultdict(list)
#     for i in range(0, a):
#         num = random.randint(0, 9)
#         d[i].append(num)
#
#     print(dict(d))
#
#
# fun(10)
# endregion
import string
from collections import defaultdict


class CountError(Exception):
    pass


def generate_code(length):
    if not 4 <= length <= 8:
        raise CountError(f"{length}的长度不合适")
    # 前三位
    u = random.choice(string.ascii_uppercase)
    l = random.choice(string.ascii_lowercase)
    d = random.choice(string.digits)
    rest = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=length - 3))
    code = list(u + l + d + rest)
    random.shuffle(code)
    return ''.join(code)


try:
    n = int(input("输入长度"))
    code = generate_code(n)
    print("生成验证码:", code)

    # 统计字符
    counter = defaultdict(int)
    for ch in code:
        counter[ch] += 1
    print("统计结果：", dict(counter))
    # c2 = defaultdict(int)
    # print(c2)

except ValueError:
    print("请输入整数")
except CountError as e:
    print("异常", e)
