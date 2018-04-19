import os

path = '/Volumes/250G存储/四维小视频/归档'


def dirlist(path):
    filelist = os.listdir(path)

    for filename in filelist:
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            print(filename)
            dirlist(filepath)








dirlist(path)

