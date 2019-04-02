#!/usr/local/bin/env python3

"""
1. Type the file name
2. Type the content
"""

def write_file(file_name):
	f = open("file_name", 'w')

	print("Please type the content, and type the ':w' to save and exit.")

	while True:
		content = input()
		
		if content != ":w":
			f.write('%s\n' % content)
		else:
			f.close()
			break


file_name = input("Please type the file name:")
write_file(file_name)
