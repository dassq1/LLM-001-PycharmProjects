"""
@Author:xuyinglai
@Date:2026/7/28
@DESC:
"""
import random

# print(dir(random))
# for i in dir(random):
#     print(i)
# print(random.random())
# print(random.uniform(100, 10))
# print(random.randint(1, 2))
# print(random.randrange(1, 10, 2))
seq1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
print(random.choice(seq1))
str1 = "12345qwertasdfgxcvbn"
str2 = "112"
print(random.choice(str1))
print(random.choices(str1, k=3))
print(random.choices(str2, weights=[0.1, 1, 0.9], k=1))
print(random.sample(str1, k=5))
random.shuffle(seq1)
print(seq1)
