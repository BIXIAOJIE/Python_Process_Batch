from 渲染文件 import render
import os
path ='/Volumes/250G存储/四维小视频/转换输出目录'
def dirlist(path):
    filelist = os.listdir(path)
    for filename in filelist:
        os.chdir(path)
        if os.path.splitext(filename)[1] == '.mp4':
            render(filename)


dirlist(path)
