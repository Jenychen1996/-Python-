# -*- coding:utf-8 -*-

def Narcissus1():
    '小甲鱼方法'
    for each in range(100, 1000):
        temp = each
        sum = 0
        while temp:
            # 第一次sum = 0 + 个位数 ** 3 ; temp = 除个位数
            # 第二次sum = 个位数 ** 3 + 十位数 ** 3 ; temp = 百位数
            # 第三次sum = 个位数 ** 3 + 十位数 ** 3 + 百位数 ** 3 ; temp
            sum = sum + (temp % 10) ** 3
            temp = temp // 10

        if sum == each:
            print(each)


def Narcissus2():
    for sum2 in range(100, 1000):
        if sum2 == ((sum2 // 100) ** 3 + (sum2 // 10 % 10) ** 3 + (sum2 % 10) ** 3):
            print("%d 为水仙花数。" % sum2)


print("水仙花数为：")
Narcissus1()
Narcissus2()
