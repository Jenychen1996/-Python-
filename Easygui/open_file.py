import easygui as g
import os

# fileopenbox()函数的作用是打开选择文件的窗口，这里选择的是.txt文件
file_path = g.fileopenbox(default="*.txt")

# 使用with as的方法打开文件，当文件不用时，会自动关闭文件
with open(file_path) as old_file:
    # os.path.basename(路径)函数的作用是“去掉目录路径，仅返回文件名”
    title = os.path.basename(file_path)
    # 定义textbox的消息
    msg = "文件【%s】的内容如下：" % file_path
    text = old_file.read()
    # textbox()函数的作用是展示文件内容
    text_after = g.textbox(msg, title, text)

# text_after[:-1]的作用是出去文本的最后一个字符，然后两者进行比较
if text != text_after[:-1]:
    # textbox的返回值会增加一个换行符
    # buttonbox函数的作用是“展示一个可供选择的界面，返回值为你当前选择的函数”
    choice = g.buttonbox("检测到文件内容发生改变，请选择以下操作：", "警告", ("覆盖保存", "放弃保存", "另存为..."))
    if choice == "覆盖保存":
        # 使用with as 语法对文件进行操作，当文件不使用时会自动关闭文件
        with open(file_path, 'w') as old_file:
            # 使用文件的write函数将修改后的文本写入
            old_file.write(text_after[:-1])

    if choice == "放弃保存":
        pass

    if choice == "另存为...":
        # filesavebox函数的作用是“打开当前路径，然后选择保存的路径”
        another_path = g.filesavebox(default=".txt")
        # os.path.splitext()函数的作用是“将文件的文件名和扩展名分离，返回(f_name, f_extension)元组”
        if os.path.splitext(another_path)[1] != '.txt':
            another_path += '.txt'
        with open(another_path, 'w') as new_file:
            new_file.write(text_after[:-1])
