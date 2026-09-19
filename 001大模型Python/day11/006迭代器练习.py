"""
@Author:xuyinglai
@Date:2026/7/29
@DESC:
"""


# def func(start):
#     if start == 0:
#         return 0
#     return func(start - 1) + func(start - 2)
#
#
# class My_Odd:
#     def __init__(self, size):
#         self.size = size  # 记录要求的个数
#         self.start = 10  # 下表
#         self.count = 0
#         self.num = 2
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         index = self.start
#         self.count += 1
#         if self.count > self.size:
#             raise StopIteration
#         num = func(self.start - 1) + func(self.start - 2)
#         return num
#
#
# m1 = My_Odd(5)
# print(m1.__next__())
################################################################

# todo 自定义迭代器，实现获取多个任意奇数
class My_Odd:
    def __init__(self, size):
        self.size = size
        self.start = 1
        self.count = 0  # 记录奇数总个数

    def __iter__(self):
        """
        返回迭代器自身
        :return:
        """
        return self

    def __next__(self):
        result = self.start
        self.count += 1
        if self.count > self.size:
            raise StopIteration
        self.start += 2
        return result


m1 = My_Odd(5)
print(m1.__next__())
print(m1.__next__())
print(m1.__next__())
print(m1.__next__())
print(m1.__next__())
print("**************************************************")


# todo 自定义迭代器实现列表的倒序
class MyReverse:
    def __init__(self, list2):
        self.list2 = list2
        self.index = len(list2) - 1

    def __iter__(self):
        return self

    def __next__(self):
        result = self.list2[self.index]
        if self.index < 0:
            raise StopIteration
        self.index -= 1

        return result


l2 = [1, 3, 4, 2, 0]
m2 = MyReverse(l2)
print(m2.__next__())
print(m2.__next__())
print(m2.__next__())
print(m2.__next__())
###################################################################
print("****************自定义迭代器，实现任意个斐波那契数***********************")


# 1,1,2,3,5,8,13,21
class MyFb:
    def __init__(self, size):
        self.size = size
        self.a = 1
        self.b = 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        result = self.a
        self.count += 1
        # count初始值为0
        if self.count > self.size:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b

        return result


m1 = MyFb(1)
print(m1.__next__())
print(m1.__next__())
