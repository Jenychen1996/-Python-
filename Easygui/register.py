"""
实现一个用于登记用户账号信息的界面（如果是带 * 号的必填项，要求一定要有输入并且不能是空格）
"""
import easygui as g

msg = '请填入以下联系方式：'
title = '账号中心'
fieldNames = ['*用户名', '*真实姓名', '*固定电话', '*手机号码', 'QQ', '*电子邮件']
fieldValues = []
fieldValues = g.multenterbox(msg, title, fieldNames)

while True:
    if fieldValues == None:
        break
    errmsg = ''
    for i in range(len(fieldNames)):
        # strip（剥去，剥夺） 的作用是去掉前后空格
        option = fieldNames[i].strip()
        if fieldValues[i].strip() == '' and option[0] == '*':
            errmsg += ('[%s]为必填项。\n\n' % fieldNames[i])

    if errmsg == '':
        break
    fieldValues = g.multenterbox(errmsg, title, fieldNames, fieldValues)

print("用户的资料如下：%s" % str(fieldValues))
