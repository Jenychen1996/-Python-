#!/usr/local/bin/env python3
#encoding = 'utf-8'
"""
用户输入文件名以及制定行号
"""

def file_view(file_name, line_nums):
	if line_nums.strip() == ":":
		begin = '1'
		end = '-1'

	(begin, end) = line_nums.split(":")

	if begin == '1' and end == '-1':
		prompt = '的全文'
	elif begin == '1':
		prompt = '从开始到%s' % end
	elif end == '-1':
		prompt = '从%s到结束' % begin
	else:
		prompt = '从%s行到%s行' % (begin, end)

	print("\n文件%s%s的内容如下\n" % (file_name, prompt))

	begin = int(begin) - 1
	end = int(end)
	lines = end - begin

	f = open(file_name)
	
	for i in range(begin):
		f.readline()

	if lines < 0:
		print(f.read())
	else:
		for j in range(lines):
			print(f.readline(), end='')

	f.close()


file_name = input("请输入指定的文件名：")
line_num = input("请输入需要显示的行号：如13:21, 21: , :21")
file_view(file_name, line_num)
