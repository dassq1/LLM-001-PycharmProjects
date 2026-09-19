"""
@Author:xuyinglai
@Date:2026/7/23
@DESC:
"""
from functools import reduce

# student_list = [{"name": "xu", "age": 100}, {"name": "yinng", "age": 20}, {"name": "lai", "age": 15}]
# print(sorted(student_list, key=lambda x: x["age"]))

# map_result = map(lambda x: x * x, [0, 1, 2, 3, 4, 5, 6])
# print(list(map_result))

# filter_result = filter(lambda x: x >= 0, [0, -0, -9, 9, 222])
# print(list(filter_result))

reduce_result = reduce(lambda x, y: x ** y, [6, 2, 3, 4, 5])
print(reduce_result)
