import os
import ffmpeg


ROOT = '/home/ram/anuj/espnet/egs/tamil/asr1'
OUTPUT_DIR = os.path.join(ROOT,'downloads/Synthetic')
TA_ROOT = os.path.join(ROOT,'downloads/ta/ta-in-Test/')
TA_AUDIO_PATH = os.path.join(TA_ROOT,'Audios')
TA_TRANSCRIPT = open(os.path.join(TA_ROOT,'transcription.txt'),'r')

LIBRI_TEXT = open(os.path.join(ROOT,'downloads/libri_test_clean.txt'))

TA_TRANSCRIPT_LIST = TA_TRANSCRIPT.read().split('\n')[:2620]
LIBRI_TRANSCRIPT_LIST = LIBRI_TEXT.read().split('\n')

OUTPUT_TRANSCRIPT = open(os.path.join(OUTPUT_DIR,'transcript.txt'),'w')

length = 100
for i in range(length):

    libri_file_name = LIBRI_TRANSCRIPT_LIST[i].split(',')[0]
    libri_transcript = LIBRI_TRANSCRIPT_LIST[i].split(',')[1]

    ta_file_name = TA_TRANSCRIPT_LIST[i].split('\t')[0]
    ta_transcript = TA_TRANSCRIPT_LIST[i].split('\t')[1]

    libri_file = ffmpeg.input(libri_file_name)
    ta_file = ffmpeg.input(os.path.join(TA_AUDIO_PATH,ta_file_name + '.wav'))
    
    output_file_name = 'code_mixed_' + str(i + 1)
    joint_transcript = ta_transcript + " " + libri_transcript

    OUTPUT_TRANSCRIPT.write(output_file_name + '\t' + joint_transcript + '\n')

    ffmpeg.concat(ta_file,libri_file,v = 0,a = 1).output(os.path.join(OUTPUT_DIR,output_file_name + '.wav')).run()
