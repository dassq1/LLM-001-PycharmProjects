"""
@Author:xuyinglai
@Date:2026/7/20
@DESC:
"""

# score = int(input("输入一个分数:"))
# match score:
#     case a if score < 60:
#         print("不及格")
#     case b if 80 > score >= 60:
#         print("良好")
#     case c if 80 <= score < 100:
#         print("优秀")
#     case d if score == 100:
#         print("666")
#     case _:
#         print("输入分数不合法")
#
# # 2222222
# year = int(input("输入一个年份:"))
# month = int(input("输入一个月份:"))
# match year:
#     case a if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
#         match month:
#             case 1 | 3 | 5 | 7 | 8 | 10 | 12:
#                 print(f"{year}的{month}月份有31天")
#             case 2:
#                 print(f"{year}的{month}月份有29天")
#             case 4 | 6 | 9 | 11:
#                 print(f"{year}的{month}月份有30天")
#             case _:
#                 print("输入错误")
#
#     case _:
#         match month:
#             case 1 | 3 | 5 | 7 | 8 | 10 | 12:
#                 print(f"{year}的{month}月份有31天")
#             case 2:
#                 print(f"{year}的{month}月份有28天")
#             case 4 | 6 | 9 | 11:
#                 print(f"{year}的{month}月份有30天")
#             case _:
#                 print("输入错误")
#


"""
1. 获取1~100内奇数的和
2.获取三位数的水仙花数 [100,999]
   153 = 1*1*1 + 5*5*5 + 3*3*3
3. 输出 1~150内所有的数 要求 如果能被3整除 5 整除 7 整除
   1
   2
   3 foo
   4
   5 baz
   6 foo
   7 biz
   .....
   15 foo baz
   ....
   21 foo biz
   ....
   35 baz biz
   .....
   105 foo baz biz


"""
# sum = 0
# for i in range(1, 101):
#     if i % 2 == 0:
#         sum += i
# print(sum)

# count1 = 0
# for i in range(100, 1000):
#     a = i % 10
#     b = i // 10 % 10
#     c = i // 100
#     if a ** 3 + b ** 3 + c ** 3 == i:
#         print(i)
#         count1 += 1
# print(f"{count1}")
# print("#" * 100)
#
# for i in range(1, 151):
#     tag = ""
#     if i % 3 == 0:
#         tag += "foo "
#     if i % 5 == 0:
#         tag += "baz "
#     if i % 7 == 0:
#         tag += "biz"
#     # 清除末尾多余空格
#     tag = tag.strip()
#     if tag:
#         print(f"{i} {tag}")
#     else:
#         print(i)
# step = 0
# lucky_num = randint(0, 10)
# num = int(input("输入一个数字:"))
# while num != lucky_num:
#
#     if num > lucky_num:
#         print("猜大了")
#
#         step += 1
#     elif num < lucky_num:
#         print("猜小了")
#
#         step += 1
#     num = int(input("输入一个数字:"))
#
# print("猜中了")
# step += 1
# print(step)

print('*' * 100)
count = 0
for i in range(1, 101):
    if i % 3 == 0 or i % 10 == 3:
        count += 1
        print(i, end=' ')
        if count % 5 == 0:
            print()
