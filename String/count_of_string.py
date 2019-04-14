#!/usr/local/bin/python3
# encoding = 'utf-8'
"""
1. 编写一个函数，分别统计出传入字符串参数（可能不只一个参数）的英文字母、空格、数字和其它字符的个数。
"""


def count(*param):
    length = len(param)
    for i in range(length):
        letters = 0
        space = 0
        digit = 0
        others = 0
        for each in param[i]:
            if each.isalpha():
                letters += 1
            elif each.isdigit():
                digit += 1
            elif each == ' ':
                space += 1
            else:
                others += 1
        print('第 %d 个字符串共有：英文字母 %d 个，数字 %d 个，空格 %d 个，其他字符 %d 个。' % (i + 1, letters, digit, space, others))


count('I love fishc.com.', 'I love you, you love me.')
