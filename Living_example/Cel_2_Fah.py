# -*- coding:utf-8 -*-

"""
定义一个类实现摄氏度到华氏度的转换（转换公式：华氏度 = 摄氏度*1.8+32）
"""
class C2F(float):
    def __new__(cls, arg=0.0):
        return float.__new__(cls, arg * 1.8 + 32)


print(C2F(32))


class Celsius:
    def __init__(self, value=26.0):
        self.value = value

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = float(value)

class Fahrenheit:
    def __get__(self, instance, owner):
        return instance.cel * 1.8 + 32

    def __set__(self, instance, value):
        instance.cel = (float(value) - 32) / 1.8

class Temperature:
    cel = Celsius()
    fah = Fahrenheit()

temp = Temperature()
print(temp.cel)
print(temp.fah)
temp.cel = 30
print(temp.fah)
temp.fah = 100
print(temp.cel)

