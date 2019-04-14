#-*- coding:itf-8 -*-

print("--------迭代版本--------")


def iterate(n):
    result = n
    for i in range(1, n):
        result *= i

    return result


number = int(input("> "))
result = iterate(number)
print("%d的阶乘是%d" % (number, result))

print("--------递归版本---------")


def factorial2(n):
    if n == 1:
        return n
    else:
        return n * factorial2(n - 1)


result2 = factorial2(number)


print("%d的阶乘是%d" % (number, result2))
