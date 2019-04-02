#!/usr/local/bin/env python3

"""
1. Type the first file name
2. Type the second file name
"""
def file_compare(file1, file2):
	f1 = open(file1)
	f2 = open(file2)

	count = 0
	differ = []

	for line1 in f1:
		line2 = f2.readline()
		count += 1
		if line1 != line2:
			differ.append(count)

	f1.close()
	f2.close()
	return differ


file1 = input("Please type the first file name :")
file2 = input("Please type the second file name :")
differ = file_compare(file1, file2)

if len(differ) == 0:
	print("%s and %s is the same." % (file1, file2))
else:
	print("%s and %s have %d different." % (file1, file2, len(differ)))
	for each in differ:
		print("The %d line is different." % each)
