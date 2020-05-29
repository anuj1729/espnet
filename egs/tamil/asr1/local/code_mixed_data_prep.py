import os

DATA_DIR = '/home/ram/anuj/espnet/egs/tamil/asr1/data/code_mixed_synthetic_2'
CM_DATA_DIR = '/home/ram/anuj/espnet/egs/tamil/asr1/downloads/Synthetic2'

transcript_file = open(os.path.join(CM_DATA_DIR,'transcript.txt'),'r')

text = open(os.path.join(DATA_DIR,'text'),'w+')
utt2spk = open(os.path.join(DATA_DIR,'utt2spk'),'w+')
spk2utt = open(os.path.join(DATA_DIR,'spk2utt'),'w+')
wav_scp = open(os.path.join(DATA_DIR,'wav.scp'),'w+')

for x in transcript_file:

    utterance_id = x.split('\t')[0]
    transcript = x.split('\t')[1]
    speaker_id = utterance_id
    text.write(utterance_id + " " + transcript)
    utt2spk.write(utterance_id + " " + speaker_id +"\n")
    spk2utt.write(speaker_id + " " + utterance_id + "\n")
    wav_scp.write(utterance_id + " sox " + os.path.join(CM_DATA_DIR,utterance_id + '.wav')  + " -t wav -r 16000 -b 16 - |\n")

    # wav_scp.write(utterance_id + " sox " + os.path.join(source + "/Audios",utterance + '.wav') + " -t wav -r 16000 -b 16 - |\n")i
