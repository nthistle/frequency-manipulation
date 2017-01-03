from scipy.io import wavfile
import numpy as np

SAMPLE_SIZE = 4096
MOVE_SIZE = 512

notes = [(y[0],float(y[1])) for y in [x.split("\t") for x in open("notefreqs.txt").read().split("\n")]]

# ((bin_id) * freq / 2) / (N/2) where freq is sample freq

## returns the closest match note to a frequency
def findnote(freq):
    bestnote = notes[0][0]
    bestdist = abs(notes[0][1]-freq)
    for i in range(1,len(notes)):
        if(abs(notes[i][1]-freq)<bestdist):
            bestdist = abs(notes[i][1]-freq)
            bestnote = notes[i][0]
    return bestnote

## returns magnitudes of each frequency
def freqbreakdown(snd):
    f = np.fft.fft(snd)
    return [abs(x) for x in f[0:len(f)//2]]


rate, sound = wavfile.read("song.wav")

for i in range(1+((len(sound)-SAMPLE_SIZE)//MOVE_SIZE)):
    sample = sound[MOVE_SIZE*i:MOVE_SIZE*i+SAMPLE_SIZE]
