"""
@Author:xuyinglai
@Date:2026/7/27
@DESC:
"""
"""
1.
 1.1如何查看一个类的方法解析顺序
"""
# mro
"""
 print(student)
    class A:
        def eat(self):
            print("A的eat")

    class B(A):
        def eat(self):
            super().eat()
            print("B的eat")
    class C(A):
        def eat(self):
            print("C的eat")
            super().eat()

    class D(B, C):
        def eat(self):
            super().eat()
            print("D的eat")
 1.2创建类D的对象 调用 eat() 展示结果是什么?
"""
# C A B D
"""
 
2.定义一个 BankAccount 类，有属性id(可以赋值也可以不赋值),私有属性 __balance（初始余额为 0） ,提供存钱和取钱的方法，
   取钱时如果余额不足则打印提示信息。
"""


class BankAccount:
    def __init__(self, id, balance):
        self.id = id
        self.__balance = balance

    # 查看与余额
    def get_balance(self):

        return self.__balance

    def put_balance(self, value):
        if self.__balance >= value:
            self.__balance -= value
            print(f"取钱成功取出{value}元")
        else:
            print(f"余额不足")

    # 存钱
    def set_balance(self, value):
        self.__balance += value


b1 = BankAccount(1, 1000)
print(b1.get_balance())
b1.put_balance(200)
"""

3.创建一个图形类体系，展示多态特性：
要求：
- 基类 `Shape`：
  - 定义方法 `area()` 和 `perimeter()`，方法体用pass表示
  - 重写__str__() 返回 面积xx,周长xx
- 派生类： 重写父类的方法
  - `Rectangle`（矩形）：属性 `width`、`height`
     重写 str 展示 长 宽 面积 周长
  - `Circle`（圆形）：属性 `radius`
  重写 str 展示 半径 面积 周长
  - `Triangle`（三角形）：属性 `a`、`b`、`c`（三边长）
     重写 str 展示 三边 面积 周长
- 创建函数 `print_shape_info(shape)`，接收任何形状对象并打印其面积和周长
- 演示多态：传入不同的对象调用同一函数
"""


class Shape:
    # def __init__(self):
    #     pass

    def area(self):
        pass

    def perimeter(self):
        pass

    def __str__(self):
        return (f"面积是{self.area}，周长是{self.perimeter}")


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return (self.width * self.height)

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return (f"长是：{self.height},宽是{self.width},面积是{self.area()},周长是{self.perimeter()}")


class Tri(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        z = (self.a + self.b + self.c) / 2
        return (z * (z - self.a) * (z - self.b) * (z - self.c)) ** 0.5

    def perimeter(self):
        return self.a + self.b + self.c

    def __str__(self):
        return (f"a是：{self.a},b是{self.b},c是{self.c},面积是{self.area()},周长是{self.perimeter()}")


def print_shape_info(shape):
    print(shape)


r1 = Rectangle(2, 5)
print_shape_info(r1)

t1 = Tri(3, 4, 5)
print_shape_info(t1)
