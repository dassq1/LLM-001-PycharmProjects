"""
@Author:xuyinglai
@Date:2026/7/21
@DESC:
"""
# list1 = [i ** 2 for i in range(5)]
# print(list1)
list1 = [77, 66, 55, 44, 33, 22, 11]
# i = 0
# count = 0
#
# for i in range((len(list1) - 1)):
#     for j in range(len(list1) - 1 - i):
#         if list1[j] > list1[j + 1]:
#             list1[j], list1[j + 1] = list1[j + 1], list1[j]
#         count += 1
#
# print(list1, count)
print(id(list1))
list2 = list1[:]
list3 = list2
print(id(list2[:]))
print(id(list3))
