#-*- coding:utf-8 -*-

def Hanoi(n, x, y, z):
    if n == 1:
        print(x, " ==> ", z)
    else:
        Hanoi(n-1, x, z, y)# 将前n-1个盘子移动到y上
        print(x, " ==> ", z) # 将最底下最后一个盘子从x移动到z上
        Hanoi(n-1, y, x, z)# 将y上的n-1个盘子移动到z上


n = int(input("> "))
print(Hanoi(n, 'X', 'Y', 'Z'))
