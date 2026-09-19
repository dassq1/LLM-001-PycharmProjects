"""
@Author:xuyinglai
@Date:2026/7/24
@DESC:
"""

student_list = [{"name": "zhang3", "age": 36},
                {"name": "li4", "age": 18},
                {"name": "wang5", "age": 27}
                ]
# 按年龄排序
print(sorted(student_list, key=lambda x: x["age"]))
# map()函数对序列中的元素逐一处理
map_result = map(lambda x: x * x, [1, 2, 3, 4, 5, 6, ])
print(type(map_result))


# nums = [1, 2, 3, 4]
# # 每个数字 ×2
# nums = map(lambda x: x * 2, nums)
# print(list(nums))  # [2, 4, 6, 8]

def dog(name: str, age: (1, 99), species: '狗狗的品种') -> tuple:
    return (name, age, species)


print(dog.__annotations__)
