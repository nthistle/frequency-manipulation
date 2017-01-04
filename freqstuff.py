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


freqs = []

rate, sound = wavfile.read("../song.wav")


#test for extracting which frequencies / notes played at which time

for i in range(1+((len(sound)-SAMPLE_SIZE)//MOVE_SIZE)):
    sample = sound[MOVE_SIZE*i:MOVE_SIZE*i+SAMPLE_SIZE]
    freqs.append(freqbreakdown(sample))


thresh = 500000
multthresh = 2.0

for i in range(1,len(freqs)):
    for j in range(len(freqs[i])):
        if freqs[i][j] > thresh and freqs[i][j] > multthresh * freqs[i-1][j]:
            print("Frequency",int(1000*(j*rate/SAMPLE_SIZE))/1000.0,"played at time",int(1000*i*MOVE_SIZE/rate)/1000.0)
