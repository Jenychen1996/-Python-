"""
编写一个程序，统计当前目录下每个文件类型的文件数，
"""
import os

def file_count(dir_path):
    # 1.列出路径下的所有文件
    dir_files = list(os.listdir(dir_path))

    count_dir = 0
    count_py = 0
    count_txt = 0
    count_mp3 = 0
    count_zip = 0
    count_other = 0

    # 2.判断为文件夹还是文件
    for each in dir_files:
        # 1.如果是文件夹，则文件夹数量+1
        if os.path.isdir(each):
            count_dir += 1
        # 2.如果为文件，则执行两步，
        # （1）分离文件名和后缀
        # （2）判断后缀，分离文件
        else:
            if os.path.splitext(each)[1] == '.py':
                count_py += 1
            elif os.path.splitext(each)[1] == '.txt':
                count_txt += 1
            elif os.path.splitext(each)[1] == '.mp3':
                count_mp3 += 1
            elif os.path.splitext(each)[1] == '.zip':
                count_zip += 1
            else:
                count_other += 1

    print("%s路径下共有%d文件夹及文件，\n其中文件夹有%d个，\n【.py】文件有%d个，\n【.txt】文件有%d个，\n【.mp3】文件有%d个，\n【.zip】文件有%d个，\n其余文件有%d个" \
          % (dir_path, len(dir_files), count_dir, count_py, count_txt, count_mp3, count_zip, count_other))


dir_path = input("Please input the dir path:")
file_count(dir_path)
