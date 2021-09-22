# 爱德生小程序
# 版本：1.1
# 功能：重命名文件

import os

path = '/Users/cat/Documents/四维彩超/归档'


def dirlist(path):
    filelist = os.listdir(path)

    for filename in filelist:
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            dirlist(filepath)
        else:
            if os.path.splitext(filepath)[1]=='.avi':
                newname = os.path.basename(os.path.abspath(os.path.dirname(filepath)))
                newname = os.path.join(os.path.dirname(filepath),os.path.basename(os.path.abspath(os.path.join(filepath, "../..")))+newname)
                print(newname)
                os.rename(filepath,newname+filename+'.avi')
            elif os.path.splitext(filepath)[1]=='.wmv':
                newname = os.path.basename(os.path.abspath(os.path.dirname(os.path.dirname(filepath))))
                newname = os.path.join(os.path.dirname(filepath), os.path.basename(os.path.abspath(os.path.join(filepath, "../..")))+newname)
                os.rename(filepath, newname +filename + '.wmv')

dirlist(path)

