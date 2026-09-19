# 练习题1：
#     定义函数 calculate(num, func):
#                 return func(num)
#     定义匿名函数作为参数传给 calculate，分别实现求绝对值、平方根、四舍五入保留最多两位小数
#     提示：内置函数 abs,round(小数,保留的位数),

# 练习题2：
#     现有一组数据如下：[{"name":"lily", "age":26, "salary": 15000}, {...}, {...},{...}]
#     数据自己随意。
#     通过匿名函数作为参数传给sorted，filter，map，reduce，nlargest,nsmallest等，分别实现
#     （1）按照薪资从高到低排序
#     （2）找出薪资前3高的员工
#     （3）找出薪资低于15000的员工
#     （4）求所有员工的薪资总和
#     （5）找出年龄最小的员工

'''
# 练习题1：
#     定义函数 calculate(num, func):
#                 return func(num)
#     定义匿名函数作为参数传给 calculate，分别实现求绝对值、平方根、四舍五入保留最多两位小数
#     提示：内置函数 abs,round(小数,保留的位数),
'''
from functools import reduce
from heapq import nlargest, nsmallest


def calculate(num,func):
    return func(num)

result = calculate(-10,lambda x:abs(x))
print(result)

result = calculate(9,lambda x:x**0.5)
print(result)

result = calculate(1.567,lambda x:round(x,2))
print(result)
print("----------------------------------------------")

'''
# 练习题2：
#     现有一组数据如下：[{"name":"lily", "age":26, "salary": 15000}, {...}, {...},{...}]
#     数据自己随意。
#     通过匿名函数作为参数传给sorted，filter，map，reduce，nlargest,nsmallest等，分别实现
#     （1）按照薪资从高到低排序
#     （2）找出薪资前3高的员工
#     （3）找出薪资低于15000的员工
#     （4）求所有员工的薪资总和
#     （5）找出年龄最小的员工

'''

person_data = [
    {"name":"李白", "age":26, "salary": 12000},
    {"name":"杜甫", "age":21, "salary": 11000},
    {"name":"王安石", "age":22, "salary": 15000},
    {"name":"李商隐", "age":23, "salary": 16000},
    {"name":"白居易", "age":20, "salary": 19000},
    {"name":"李清照", "age":19, "salary": 20000},
]

print("排序前",person_data)

# person_data=sorted(person_data,key=lambda x:x['salary'],reverse=True)
person_data=sorted(person_data,key=lambda x:-x['salary'])
print("排序后",person_data)
# 找出薪资前3高的员工
r = nlargest(3,person_data,key=lambda x:x['salary'])
print(r)

# 找出薪资低于15000的员工
f = filter(lambda x:x['salary']<15000,person_data)
print(list(f))

# 找出年龄最小的员工
r = nsmallest(1,person_data,lambda x:x['age'])
print(r)


# 求所有员工的薪资总和

# r = reduce(lambda x,y:x['salary']+y['salary'],person_data)

'''
x: {"name":"李白", "age":26, "salary": 12000}
y:{"name":"杜甫", "age":21, "salary": 11000}
23000
'''
r = reduce(lambda x,y:x+y['salary'],person_data,0)
print(r)



# m = map(lambda x:x['name'],person_data)
# 获取每一条记录内 薪水的值
m = map(lambda x:x['salary'],person_data)
# print(sum(list(m)))
print(sum(m))



