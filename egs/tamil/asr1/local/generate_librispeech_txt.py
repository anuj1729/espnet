import os

LIBRI_ROOT = '/home/ram/anuj/espnet/egs/tamil/asr1/downloads/libri/LibriSpeech'
PART_NAME = 'test-clean'
OUTPUT_DIR = '/home/ram/anuj/espnet/egs/tamil/asr1/downloads/'
OUTPUT_FILE_NAME = 'libri_test_clean.txt'

OUTPUT_FILE = open(os.path.join(OUTPUT_DIR,OUTPUT_FILE_NAME),'w')

for root,dirs,files in os.walk(os.path.join(LIBRI_ROOT,PART_NAME)):
    for f in files:
        if f.endswith('.txt'):
            transcript_file = open(os.path.join(root,f),'r')
            for x in transcript_file:
                audio_file = x.split(' ',1)[0]
                transcript = x.split(' ',1)[1].lower()
                full_file_path = os.path.join(root,audio_file) + '.flac'
                OUTPUT_FILE.write(full_file_path + ',' + transcript)
