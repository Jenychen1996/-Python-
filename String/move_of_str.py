class NewStr(str):
    def __lshift__(self, other):
        return self[other:] + self[:other]

    def __rshift__(self, other):
        return self[-other:] + self[:-other]


a = NewStr("I love FishC.com")
print(a >> 3)
print(a << 3)
