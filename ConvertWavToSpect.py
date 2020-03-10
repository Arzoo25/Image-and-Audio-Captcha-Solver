import os
import numpy as np
import matplotlib.pylab as plt
from os import listdir
from os.path import isfile,join
#for loading and visualizing audio files
import librosa
import librosa.display

path="C:/Users/Arzoo/Desktop/ScalableProject3/wav"
dest = "C:/Users/Arzoo/Desktop/ScalableProject3/specto"
files = [f for f in listdir(path) if isfile(join(path,f))]

# for converting the wav file to spectrograms
for audio in files:
    x, sr = librosa.load(os.path.join(path, audio))
    plt.figure(figsize=(1.28, .64), dpi=100)
    plt.axis('off')
    plt.axes([0., 0., 1., 1., ], frameon=False, xticks=[], yticks=[])
    #creating spectrogram
    S = librosa.feature.melspectrogram(y=x, sr=sr)
    librosa.display.specshow(librosa.power_to_db(S, ref=np.max))
    #saving the spectrograms as png images
    plt.savefig(os.path.join(dest, os.path.splitext(audio)[0]+'.png'), bbox_inches=None, pad_inches=0)
    plt.close()