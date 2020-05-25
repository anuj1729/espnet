import torch
import argparse
import os
import numpy as np
parser = argparse.ArgumentParser()
parser.add_argument('--path',dest = 'path')

args = parser.parse_args()

# model = os.path.join(args.path,'snapshot.ep.1')

snapshot = torch.load(args.path,map_location = "cpu")

print(sum([np.prod(p.size()) for p in snapshot.values()]))


