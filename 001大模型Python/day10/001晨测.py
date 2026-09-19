"""
@Author:xuyinglai
@Date:2026/7/28
@DESC:
"""
"""
1. 以下哪种异常通常在尝试访问列表内不存在的下标时引发？（  ）
  A. KeyError	B. IndexError C. ValueError	D. TypeError

3、简答题
    0.try except else finally 各个部分的作用
    1.什么是上下文管理器协议
上下文管理器协议是 Python 实现资源自动管理的规范，一个类只要实现了`__enter__()`和`__exit__()`两个魔法方法，就满足该协议，可以配合`with`语句使用：

- `__enter__`：进入`with`代码块时触发，完成资源初始化、打开文件等操作；
- `__exit__`：离开`with`代码块时触发（哪怕中间出现异常也会执行），完成资源关闭、清理工作，避免手动`close`遗漏导致资源泄漏。常见例子：`with open(...)`文件操作就是依托文件类实现的上下文管理器协议。
    2.异常的抛出方式
三、编程题
1. 编写一段 Python 代码，尝试将字符串 "123abc" 转换为整数，
  如果转换失败，捕获 ValueError 异常，将异常信息记录到一个文本文件 error.log 中。
"""


class ValueError(Exception):
    print("XUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU")
    f = open(r"C:\Users\23716\Desktop\PycharmProjects\大模型\day10\error.log", 'w', encoding='utf-8')
    f.write("123455")
    f.close()


str1 = "123abc"
f = None

print(11111111)
if str1:
    num = int(str1)
    raise ValueError("出现异常")
print("************************************")

print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
"""
2. 定义一个函数check_age，该函数接受一个年龄参数。如果年龄小于 0，抛出一个自定义异常 InvalidAgeError；
   如果年龄大于 150，抛出 UnrealisticAgeError。这两个自定义异常类都继承自Exception类
   调用该函数并传入一个不合法的年龄值，捕获并处理异常。
"""


class InvalidAgeError(Exception):
    pass


class UnrealisticAgeError(Exception):
    pass


def check_age(age):
    if age < 0:
        raise InvalidAgeError("年龄不能小于0")
    elif age > 150:
        raise UnrealisticAgeError("年龄不能大于150")


try:
    check_age(-9)
except InvalidAgeError as e:
    print("捕获到异常", e)
except UnrealisticAgeError as e:
    print("捕获到异常", e)
finally:
    print("HHHHHHHHHHHHHHHHHHHHHHHHH")
