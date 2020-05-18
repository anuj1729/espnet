import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--source",dest="source")
parser.add_argument("--destination",dest="destination")

args = parser.parse_args()

source = args.source
destination = args.destination

transcript_path = os.path.join(source,'transcription.txt')

transcript_file = open(transcript_path,'r')
text_file = open(os.path.join(destination,'text'),'w+')
wav_scp = open(os.path.join(destination,'wav.scp'),'w+')
utt2spk = open(os.path.join(destination,'utt2spk'),'w+')
spk2utt = open(os.path.join(destination,'spk2utt'),'w+')
for x in transcript_file:
    utterance = x.split("\t")[0]
    text = x.split("\t")[1]
    speaker = utterance
    utterance_id = utterance
    text_file.write(utterance_id + " " + text)
    utt2spk.write(utterance + " " + speaker + "\n")
    spk2utt.write(speaker + " " + utterance + "\n")
    wav_scp.write(utterance_id + " sox " + os.path.join(source + "/Audios",utterance + '.wav') + " -t wav -r 16000 -b 16 - |\n")
