#-*- coding:utf-8 -*-

import urllib.request
import easygui as g
def main():
    temp = g.multenterbox(msg='请填写喵的尺寸...', title='下载一只喵', fields=['宽', '高'], values=[])

    width = temp[0]
    height = temp[1]

    url = 'http://www.placekitten.com' + '/' + str(width) + '/' + str(height)

    response = urllib.request.urlopen(url)

    path = g.diropenbox('请选择存放喵的文件夹：', default='.')

    file_name = path + '/' + 'cat_' + str(width) + '_' + str(height) + '.jpg'
    with open(file_name, 'wb') as f:
        f.write(response.read())

if __name__ == '__main__':
    main()

