"""
@Author:xuyinglai
@Date:2026/7/29
@DESC:
"""


def outer():
    num = 10

    # print(hex(id(num)))

    def inner():
        print(num)

    # print(id(inner))

    return inner


f = outer()


# print(id(f))

# f()
# print(f.__closure__)
# print(f.__closure__[0])
# print(f.__closure__[0].cell_contents)
#####################################################
# def outer():
#     num = 10
#
#     def inner():
#         nonlocal num
#         num += 1
#         print(num)
#
#     return inner
#
#
# f1 = outer()
# f1()
# f1()
# f1()
# print(8 * "*")
# f2 = outer()
# f2()
# f1()    # 14

########################################################################
def beaauty(char, n):
    def show_msg(msg):
        print(char * n + msg + char * n)

    return show_msg


func = beaauty("*", 5)
func("HELLO")


#######################################
class Beauty:
    def __init__(self, char, n):
        self.char = char
        self.n = n

    def show_msg(self, msg):
        print(self.char * self.n + msg + self.char * self.n)


b1 = Beauty('%', 5)
b1.show_msg("WORLD")
