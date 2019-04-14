class NewStr(str):
    def __sub__(self, other):
        result = []
        for each in self:
            if each != other:
                result.append(each)

        return "".join(result)

    """
    def __sub__(self, other):
        return self.replace(other, '')
    """


a = NewStr("I love FishC.com iiiiiiiiiii")
b = NewStr('i')

print(a - b)



