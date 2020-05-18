import pandas as pd
import argparse
import os
parser = argparse.ArgumentParser()
parser.add_argument('--source',dest='source')

args = parser.parse_args()
source = args.source
utt2dur = open(os.path.join(source,'utt2dur'),'r')

s = 0
for line in utt2dur:
    dur = line.split(" ")[1]
    dur = (float)dur
    s += dur

print(s)

