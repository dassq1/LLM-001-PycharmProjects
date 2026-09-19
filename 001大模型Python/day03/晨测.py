# """
# @Author:xuyinglai
# @Date:2026/7/20
# @DESC:
# """
# # 0.身份运算符有什么作用
# # is 判断对象是否在同一个内存地址
# # 1.海象运算符有什么作用
# # 在赋值的同时返回所赋的值
# # -------
# # 0.将十进制数 25 转换为二进制数，结果是多少？
# # 除基取余法 25/2=12...1
# #         12/2=6...0
# #         6/2=3...0
# #         3/2=1...1
# #         1/2=0...1
#
# # 1.定义三个变量 名字 年龄 身高1.723 使用格式化输出 身高保留两位小数
# name = "XYL"
# age = 123
# high = 1.723
# print(f"name={name}, age={age}, high={high:.2f}")
# # 2.模拟用户登录验证，获取键盘上的输入，如果用户名root,密码是123456，提示登录成功，否则提示登录失败
# name = input("请输入姓名:")
# passwd = input("请输入密码:")
# if name == "root" and passwd == "123456":
#     print("登录成功")
# else:
#     print("登录失败")
# # 3.键盘获取三个整数值 筛选出最小值
# a = int(input("请输入第一个数值:"))
# b = int(input("请输入第二个数值:"))
# c = int(input("请输入第三个数值:"))
# min_num = a
# if b < min_num:
#     min_num = b
# if c < min_num:
#     min_num = c
# print(min_num)
# # 4.键盘输入一个年份 判断是否为闰年
# isyear = int(input("输入一个年份 判断是否为闰年:"))
# if isyear % 4 == 0 and isyear % 100 != 0 or isyear % 400 == 0:
#     print(f"{isyear}是闰年")
# else:
#     print(f"{isyear}不是闰年")
c = "Hello World"
d = "Hello World"

print(id(c))  # 打印内存编号
print(id(d))  # 和c完全相同
print(c is d)  # True，地址一致pycharm中如此，命令行不然
print(c == d)  # True，内容一致
