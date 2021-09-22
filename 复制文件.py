# 爱德生小程序
# 版本：1.1
# 功能：移动短视频文件

import os
import shutil
path = '/Users/cat/Documents/四维彩超/归档'


def dirlist(path):
    filelist = os.listdir(path)

    for filename in filelist:
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            dirlist(filepath)
        else:
            if os.path.splitext(filepath)[1]=='.avi':
                shutil.copy(filepath ,'/Users/cat/Documents/四维彩超/mp4')


            elif os.path.splitext(filepath)[1]=='.wmv':
                shutil.copy(filepath , '/Users/cat/Documents/四维彩超/mp4')






dirlist(path)

