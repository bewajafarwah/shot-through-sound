import os
import sys

def jaadu_mp3(file):
    os.system('ffmpeg -i ./data/{0}.mp4 -b:a 192k -vn ./data/{0}.mp3'.format(file))