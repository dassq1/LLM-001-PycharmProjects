# """
# @Author:xuyinglai
# @Date:2026/7/27
# @DESC:
#
# 声明银行账户类 Account
# （1）包含 账号、余额属性
#
# （2）包含取款方法，当取款金额为负数时，抛出 BanlanceNotEnoughError ，异常信息为“取款金额有误，不能为负数”，
#     当取款金额超过余额时，抛出 UnsupportedError ，异常信息为“取款金额不足，不支持当前取款操作”
#     满足要求则正常取钱
#
# （3）包含存款方法，当取款金额为负数时，抛出UnsupportedError，异常信息为“存款金额有误，不能为负数” 充足
#    存款金额正常 则正常存储
#
# 2、编写测试类，创建账号对象，并调用取款和存款方法，并传入非法参数，测试发生对应的异常。
# """
#
#
class BanlanceNotEnoughError(Exception):
    pass


class UnsupportedError(Exception):
    pass


class Account:
    def __init__(self, id, money):
        self.id = id
        self.money = money

    def withdraw(self, value):
        if value < 0:
            raise BanlanceNotEnoughError("取款金额有误，不能为负数")
        elif value > self.money:
            raise UnsupportedError("取款金额不足，不支持当前取款操作")
        else:
            self.money -= value
            print(f"取出来{value}元钱，剩余{self.money}元钱")

    def store(self, value):
        if value < 0:
            raise UnsupportedError("存款金额有误，不能为负数")
        else:
            self.money += value
            print(f"可以正常存入{value}元钱，现在余额{self.money}元钱")


a1 = Account(1, 100)
a1.withdraw(100)
a1.store(200)
a1.store(-1)
