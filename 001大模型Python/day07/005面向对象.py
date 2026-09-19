"""
@Author:xuyinglai
@Date:2026/7/24
@DESC:
"""
"""1.定义一个矩形类 有长宽两个实例属性
  定义方法 返回 周长
  定义方法 返回 面积
  定义方法 返回 所有信息
  矩形的长:6 宽3 面积:18 周长:18
"""


class Juxing:
    def __init__(self, length, wideth):
        self.length = length
        self.wideth = wideth

    def show_circle(self):
        return 2 * (self.wideth + self.length)

    def show_area(self):
        return self.length * self.wideth

    def show_info(self):
        return (self.__doc__)


p = Juxing(6, 3)
print(p.show_area())

"""       
2.定义一个类 生日类 有三个属性 年 月 日
    定义一个方法 返回 生日是:xxxx年xx月xx日
    定义一个类员工类 有两个实例属性 name 生日  
    定义一个方法 返回信息
    张三 的 生日是:xxxx年xx月xx日 """


class Birthday:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def re_birth(self):
        return (f"{self.year}年，{self.month}月，{self.day}日")


class Worker:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday

    def show_info(self):
        return f"{self.name}的生日是{self.birthday.re_birth()}"


birthday = Birthday(2026, 7, 24)
p = Worker("zhangsan", birthday)
print(p.show_info())
