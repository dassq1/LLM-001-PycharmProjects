"""
@Author:xuyinglai
@Date:2026/7/28
@DESC:
"""
# import p01_my_math_module as my
import p02_my_shape_module
#
# print(f"10+2={my.add(10, 2)}")
# print(f"10-2={my.subtract(10, 2)}")
# print(f"图像 {p02_my_shape_module.print_rectangle(5, 6)}")
# p02_my_shape_module.multiply(9, 9)
# print(my.multiply(12, 13))

# todo 指定导入模块的具体成员

# todo 导入模块所有非私有的成员
from p02_my_shape_module import *
from p01_my_math_module import *
from p01_my_math_module import multiply as math_multiply
from p02_my_shape_module import multiply as shape_multiply

print(math_multiply(12, 2))
shape_multiply(12, 2)
print(_remainder(5, 2))
import sys

# for i in sys.path:
#     print(i)
# print(sys.path)
import math

print(dir(math))
print(dir(math_multiply))
print(dir(p02_my_shape_module))
