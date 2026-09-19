"""
客户信息管理系统
"""

import re


# =========================
# 客户类
# =========================

class Customer:

    def __init__(self, cid, name, age=None, phone=None, email=None):
        self.cid = cid
        self.name = name
        self.age = age
        self.phone = phone
        self.email = email

    # 控制显示格式
    def __str__(self):
        return (
            f"{'编号':<6}{str(self.cid):<10}"
            f"{'姓名':<6}{str(self.name):<10}"
            f"{'年龄':<6}{str(self.age):<10}"
            f"{'电话':<6}{str(self.phone):<12}"
            f"{'邮箱':<20}{str(self.email)}"
        )


# 保存客户

customer_list = []


# =========================
# 添加客户
# =========================

def add_customer():
    print("\n=========添加客户=========")

    # --------id--------

    for i in range(3):

        cid = input("请输入客户id:")

        if not cid.isdigit():

            print("id必须为纯数字")

            if i == 1:
                print("最后一次机会")

            continue

        # 判断重复

        for c in customer_list:

            if c.cid == cid:
                print("id已经存在")

                return

        break


    else:

        print("三次输入失败")

        return

    # --------姓名--------

    for i in range(3):

        name = input("请输入姓名:")

        if re.match(r"^[a-zA-Z\u4e00-\u9fa5]+$", name):
            break

        print("姓名必须为字符")

        if i == 1:
            print("最后一次机会")


    else:

        print("三次输入失败")

        return

    # --------年龄--------

    age = input("请输入年龄:")

    if age.isdigit():

        age = int(age)

    else:

        print("年龄错误，跳过")

        age = None

    # --------电话--------

    phone = input("请输入电话:")

    # 按实验要求：
    # 数字即可，不限制手机号长度

    if phone.isdigit():

        pass

    else:

        print("电话格式错误")

        phone = None

    # --------邮箱--------

    email = input("请输入邮箱:")

    if re.match(r"^\w+@\w+\.\w+$", email):

        pass

    else:

        print("邮箱格式错误")

        email = None

    customer = Customer(
        cid,
        name,
        age,
        phone,
        email
    )

    customer_list.append(customer)

    print("添加成功")


# =========================
# 删除客户
# =========================

def delete_customer():
    cid = input("请输入删除客户id:")

    for c in customer_list:

        if c.cid == cid:
            customer_list.remove(c)

            print("删除成功")

            return

    print("客户不存在")


# =========================
# 修改客户
# =========================

def update_customer():
    cid = input("请输入修改客户id:")

    for c in customer_list:

        if c.cid == cid:

            print("开始修改")

            age = input("请输入年龄(回车不修改):")

            phone = input("请输入电话(回车不修改):")

            email = input("请输入邮箱(回车不修改):")

            if age != "":

                if age.isdigit():
                    c.age = int(age)

            if phone != "":

                if phone.isdigit():
                    c.phone = phone

            if email != "":

                if re.match(r"^\w+@\w+\.\w+$", email):
                    c.email = email

            print("修改成功")

            return

    print("客户不存在")


# =========================
# 查询客户
# =========================

def search_customer():
    key = input("请输入id或者姓名:")

    for c in customer_list:

        if c.cid == key or c.name == key:
            print(c)

            return

    print("没有找到客户")


# =========================
# 显示客户
# =========================

def show_customer():
    if len(customer_list) == 0:
        print("暂无客户信息")

        return

    print("\n================客户列表================")

    print(
        f"{'编号':<6}"
        f"{'ID':<10}"
        f"{'姓名':<10}"
        f"{'年龄':<10}"
        f"{'电话':<12}"
        f"{'邮箱'}"
    )

    print("-" * 60)

    for c in customer_list:
        print(
            f"{c.cid:<10}"
            f"{c.name:<10}"
            f"{str(c.age):<10}"
            f"{str(c.phone):<12}"
            f"{str(c.email)}"
        )


# =========================
# 主菜单
# =========================

def main():
    while True:

        print("""
==============================
      客户信息管理系统

1 添加客户
2 删除客户
3 修改客户
4 查询客户
5 显示客户
6 退出

==============================
        """)

        choice = input("请选择:")

        if choice == "1":

            add_customer()



        elif choice == "2":

            delete_customer()



        elif choice == "3":

            update_customer()



        elif choice == "4":

            search_customer()



        elif choice == "5":

            show_customer()



        elif choice == "6":

            print("退出系统")

            break



        else:

            print("输入错误")


if __name__ == "__main__":
    main()
