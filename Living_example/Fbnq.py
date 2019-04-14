#-*- coding:utf-8 -*-

print("----------迭代实现-----------")


def Fbnq(n):
    n1 = 1
    n2 = 1
    # n3 = 1
    if n < 0:
        print("Error.")
        return -1

    while n - 2 > 0:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        n -= 1

    return n3


result = Fbnq(20)
if result != -1:
    print(result)


print("----------递归实现-----------")
def Fbnq2(n):
    if n < 1:
        print("Error.")

    if n == 1 or n == 2:
        return 1
    else:
        return Fbnq2(n - 1) + Fbnq2(n - 2)


result2 = Fbnq2(20)
if result2 != -1:
    print(result2)
