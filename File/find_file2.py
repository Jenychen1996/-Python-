"""
 编写一个程序，用户输入开始搜索的路径，
 查找该路径下（包含子文件夹内）所有的视频格式文件（要求查找mp4 rmvb, avi的格式即可），
 并把创建一个文件（vedioList.txt）存放所有找到的文件的路径，
"""
import os


def search_file(dir_path, target):
    os.chdir(dir_path)

    for each in os.listdir(os.curdir):
        ext = os.path.splitext(each)[1]
        if ext in target:
            vedio_list.append(os.getcwd() + os.sep + each + os.linesep)
            # print(each)
        if os.path.isdir(each):
            search_file(each, target)
            os.chdir(os.pardir)


dir_path = input("请输入目标路径：")
target = ['.mp4', '.rmvb', '.avi']

vedio_list = []

search_file(dir_path, target)

current_path = os.getcwd()
f = open(current_path + os.sep + 'vediolist.txt', 'w')
f.writelines(vedio_list)
f.close()

