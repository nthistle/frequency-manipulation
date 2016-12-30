from scipy.io import wavfile
import numpy as np

SAMPLE_SIZE = 4096
MOVE_SIZE = 512

notes = [(y[0],float(y[1])) for y in [x.split("\t") for x in open("notefreqs.txt").read().split("\n")]]
