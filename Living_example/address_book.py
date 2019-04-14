#-*- coding:utf-8 -*-

"""
小甲鱼方式
"""
"""
print('|--- 欢迎进入通讯录程序 ---|')
print('|--- 1：查询联系人资料  ---|')
print('|--- 2：插入新的联系人  ---|')
print('|--- 3：删除已有联系人  ---|')
print('|--- 4：退出通讯录程序  ---|')

contacts = dict()

while 1:
    instr = int(input('\n请输入相关的指令代码：'))

    if instr == 1:
        name = input('请输入联系人姓名：')
        if name in contacts:
            print(name + ' : ' + contacts[name])
        else:
            print('您输入的姓名不再通讯录中！')

    if instr == 2:
        name = input('请输入联系人姓名：')
        if name in contacts:
            print('您输入的姓名在通讯录中已存在 -->> ', end='')
            print(name + ' : ' + contacts[name])
            if input('是否修改用户资料（YES/NO）：') == 'YES':
                contacts[name] = input('请输入用户联系电话：')
        else:
            contacts[name] = input('请输入用户联系电话：')

    if instr == 3:
        name = input('请输入联系人姓名：')
        if name in contacts:
            del (contacts[name])  # 也可以使用dict.pop()
        else:
            print('您输入的联系人不存在。')

    if instr == 4:
        break

print('|--- 感谢使用通讯录程序 ---|')
"""
"""
自己实现
"""
'''
实施一个通讯录
欢迎进入通讯录程序
1、查询联系人资料
2、插入已有联系人
3、删除已有联系人
4、退出通讯录程序
'''

"""
def MyMain():
    print("|-----欢迎进入通讯录程序-----|")
    print("|-----1、查询联系人资料-----|")
    print("|-----2、插入已有联系人-----|")
    print("|-----3、删除已有联系人-----|")
    print("|-----4、退出通讯录程序-----|")
    print("\n")
    num = int(input("请输入相关的指令代码："))
    while True:
        if num == 1:
            return Query()
        elif num == 2:
            return Insert()
        elif num == 3:
            return Delete()
        elif num == 4:
            return Exit()
        else:
            print("代码有误，请重新输入。\n")
            return MyMain()


def Query():
    name = input("请输入联系人姓名：")
    for each in ContactInfoDict:
        if name == each:
            print(name, ":", ContactInfoDict[name])
        else:
            print("您所输入的用户不在通讯录内。\n")

    return MyMain()

def Insert():
    name = input("请输入联系人姓名：")
    for each in ContactInfoDict:
        if name == each:
            print("您输入的姓名在通讯录中已存在--> %s : %s" % (each[0], ContactInfoDict[name]))
            value = str(input("是否修改用户资料（YES/NO）"))
            if value == "YES":
                break
            else:
                return MyMain()
        else:
            break
    number = input("请输入联系人电话：")
    ContactInfoDict[name] = number
    print(ContactInfoDict)
    return MyMain()

def Delete():
    name = input("请输入联系人姓名：")
    del ContactInfoDict[name]
    return MyMain()

def Exit():
    print("感谢使用通讯录程序\n")
    exit(0)


ContactInfoDict = {"name": "number"}

MyMain()

"""
