"""
编写一个程序，计算当前文件夹下所有文件的大小
"""
import os
def file_size(dir_path):
    # 1. 列出路径下所有的文件
    dir_path_files = os.listdir(dir_path)
    # 2. 判断是否为文件
    for each in dir_path_files:
        if os.path.isfile(each):
            print("文件%s的大小为：%fKB" % (each, os.path.getsize(each)))


dir_path = input("请输入访问路径：")
file_size(dir_path)

