import sys
import os
import librosa
from convert_to_mp3 import jaadu_mp3
from answer import get_answer
from continued_answer import machade

file_name = sys.argv[1]

#CONVERT TO MP3
if not os.path.exists('./data/{0}.mp3'.format(file_name)):
    jaadu_mp3(file_name)

y, sr = librosa.load('./data/{0}.mp3'.format(file_name), sr=44100)

answer = get_answer(y)

machade(file_name, answer)

print('DONE!')

