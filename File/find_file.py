#!/usr/local/bin/python3

import os
def find_file(dir_path, file_name):
	
	os.chdir(dir_path)

	for each in os.listdir(os.curdir):
		if each == file_name:
			print(os.getcwd() + os.sep + each)
		if os.path.isdir(each):
			find_file(each, file_name)
			os.chdir(os.pardir)

dir_path = input("Please input the path:")
file_name = input("Please input the file name:")
find_file(dir_path, file_name)
