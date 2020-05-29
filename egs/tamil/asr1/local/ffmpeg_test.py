import ffmpeg
import os

ROOT = '/home/ram/anuj/espnet/egs/tamil/asr1/downloads'
EN_DATA_PATH = os.path.join(ROOT,'libri/LibriSpeech/test-clean')
TA_DATA_PATH = os.path.join(ROOT,'ta/ta-in-Test/Audios')
f1 = ffmpeg.input(os.path.join(EN_DATA_PATH,'1089/134686/1089-134686-0000.flac'))
f2 = ffmpeg.input(os.path.join(TA_DATA_PATH, '000520355.wav'))


c2 = ffmpeg.concat(f1,f2,v = 0, a = 1).output('output_2.wav').run()

