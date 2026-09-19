"""
@Author:xuyinglai
@Date:2026/7/18
@DESC:
0.键盘输入一个数 判断是否能被3整除或者个位是3
1.键盘输入一个分数 判断分数等级
2.女方家长嫁女儿 条件
  1.身高 180cm 及其以上 整数
  2.财富 1千万以上 0.0000001
  3.长得 帅  布尔
  三个都满足 一定要嫁
  满足一个  比上不足比下有余 嫁
  都不满足 不嫁
3.输入三个正整数 获取最大值
"""
# num = int(input("输入一个数"))
# if num % 3 == 0 or num % 10 == 3:
#     print("该数被3整除或者个位是3")
# print("#" * 10)
# high = input("输入身高:")
# money = input("输入存款:")
# face = bool(int(input("输入帅不帅:")))
# if int(high) > 180 and int(money) > 100000000 and face:
#     print("一定要嫁")
# elif int(high) > 180 or int(money) > 100000000 or face:
#     print("上不足比下有余 嫁")
#     print(bool(face))
# else:
#     print("不嫁")
# print("#" * 10)
# a = int(input("输入第一个整数"))
# b = int(input("输入第二个整数"))
# c = int(input("输入第三个整数"))
# if a > b and a > c:
#     print(a)
# elif b > a and b > c:
#     print(b)
# elif c > a and c > b:
#     print(c)


# a = int(input("输入第一个数:"))
# b = int(input("输入第二个数:"))
# c = int(input("输入第三个数:"))
# max_num = a
# if b > max_num:
#     max_num = b
# if c > max_num:
#     max_num = c
# print(max_num)

# a = 10
# (a > 5) or (a += 1)  # a>5是True，a += 1不会执行 python不支持这种写法
# print(a) # 输出10，a没有自增
# a = 10
#
#
# def add_one():
#     global a
#     a += 1
#     return False  # 返回假值，保证or能走到这个函数
#
#
# (a > 5) or add_one()
# print(a)  # 输出10，函数没执行，验证短路

print(bin(66))
print(bin('x'))
