"""
 定义一个类继承于 int 类型，并实现一个特殊功能：当传入的参数是字符串的时候，返回该字符串中所有字符的 ASCII 码的和
 （使用 ord() 获得一个字符的 ASCII 码值）
"""
class Nint(int):
    def __new__(cls, string):
        if isinstance(string, str):
            total = 0
            for each in string:
                total += ord(each)

            string = total

        return int.__new__(cls, string)


print(Nint(123))
print(Nint(1.5))
print(Nint('A'))
print(Nint('FishC'))
print(Nint('FishC.com'))

