# module name :ads
# module version:0.1
# doc_name: ads.py

from moviepy.editor import *
import os


#render(filename)一个渲染函数，传入需要的文件名，然后制作一个十秒的小视频
def render(filename):
    print('这是一个渲染视频的小程序，这个小程序实现了以下功能')
    print('将一段轻音乐添加到一个十秒钟的视频中')
    print('视频的左下角附有文字\'美国GE-E8思维彩超\'')
    print('视频的右下角附有文字\'爱德生妇产医院\'')
    print('现在开始渲染视频')
    #剪辑小视频
    clip = VideoFileClip(filename, target_resolution=(296, 536)).subclip(1, 10)
    audioclip = AudioFileClip('/Volumes/250G存储/四维小视频/素材/gentle.mp3').subclip(1, 10)
    clip = clip.set_audio(audioclip)
    txtclip1 = TextClip('美国GE-E8四维彩超', fontsize=20, color='white', font='/Volumes/250G存储/四维小视频/素材/华康娃娃体.TTF')
    txtclip1 = txtclip1.subclip(1, 10).set_position(('left', 'bottom'))
    txtclip2 = TextClip('爱德生妇产医院', fontsize=20, color='white', font='/Volumes/250G存储/四维小视频/素材/华康娃娃体.TTF')
    txtclip2 = txtclip2.subclip(1, 10).set_position(('right', 'bottom'))
    txtend = ImageClip('/Volumes/250G存储/四维小视频/素材/我的宝贝.png')
    txtend = txtend.set_duration(2).set_position('center').set_start(8)
    video = CompositeVideoClip([clip, txtclip1, txtclip2, txtend])
    video = video.volumex(0.3)

    os.chdir('/Volumes/250G存储/四维小视频/十秒')

    video.write_videofile(filename + "vue.mp4")