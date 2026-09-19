"""
@Author:xuyinglai
@Date:2026/7/22
@DESC:

"""
"""
1.列表特点是什么?
   现有列表 my_list = [10, 20, 30, 40, 50]，请编写代码实现：
    1.1 向列表末尾添加一个元素 60。
    1.2 取出列表中索引为 2 的元素。
    1.3 对列表排序
    1.4 计算列表中所有元素的和。"""
my_list = [20, 10, 30, 50, 40]
my_list.append(60)
print(my_list[2])
for i in range(len(my_list)):
    flag = True
    for j in range(len(my_list) - i - 1):
        if my_list[j] > my_list[j + 1]:
            flag = False
            my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    if flag:
        break
print(my_list)
print(sum(my_list))
"""

2.给定两个列表 `list1 = [1, 2, 3]` 和 `list2 = [4, 5, 6]`，使用列表推导式生成一个包含所有可能的元素对的列表，
   即 `[(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]
"""
list1 = [1, 2, 3]
list2 = [4, 5, 6]
my_list1 = [(i, j) for i in list1 for j in list2]
print(my_list1)
"""
3.集合特点是什么?
  现有集合 set1 = {1, 2, 3, 4, 5} 和 set2 = {3, 4, 5, 6, 7} 。
    3.1 求这两个集合的并集
    3.2 求这两个集合的交集
    3.3 求这两个集合的差集
    3.4 求这两个集合的对称差集
    3.5 从 set1 中移除元素 3"""
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
set3 = set1 | set2
print(set3)
set4 = set1 & set2
print(set4)
set5 = set1 - set2
print(set5)
set6 = set1.symmetric_difference(set2)
print(set6)
"""
4.字典的特点是什么?
  创建一个学生信息字典，包含：姓名、年龄、性别、成绩
  4.1获取字典中的姓名和成绩并打印
  4.2把成绩改成 100，年龄加 1
  4.3给学生添加一个键：city，值：北京
  4.4删除 gender 键
  4.5遍历输出所有键和值
"""
stu_list = []
while True:
    print("*" * 50)
    print("欢迎进入学生管理系统")
    print("1获取字典中的姓名和成绩并打印")
    print("2把成绩改成100，年龄加1")
    print("3给学生添加一个键：city,值：北京")
    print("4删除gender键")
    print("5遍历所有的键和值")
    num = input("请你输入编号:")

    if num == "1":
        if len(stu_list) == 0:
            print("管理系统里暂无数据")
        else:
            print("###########全部学生列表################")
            for stu in stu_list:
                print(f"name:{stu['name']}")
                print(f"age:{stu['age']}")
                print(f"gender:{stu['gender']}")
    elif num == "2":
        fo
