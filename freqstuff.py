from scipy.io import wavfile
import numpy as np

SAMPLE_SIZE = 4096
MOVE_SIZE = 512

notes = [(y[0],float(y[1])) for y in [x.split("\t") for x in open("notefreqs.txt").read().split("\n")]]


# returns magnitudes of each frequency
def freqbreakdown(snd):
    f = np.fft.fft(snd)
    return [abs(x) for x in f[0:len(f)//2]]

rate, sound = wavfile.read("song.wav")

for i in range(1+((len(sound)-SAMPLE_SIZE)//MOVE_SIZE)):
    sample = sound[MOVE_SIZE*i:MOVE_SIZE*i+SAMPLE_SIZE]
