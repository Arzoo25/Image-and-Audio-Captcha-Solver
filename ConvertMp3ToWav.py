
#for converting mp3 to wav files
import os
from pydub import AudioSegment

os.chdir("C:/Users/Arzoo/Desktop/ScalableProject3/images")

audio_files = os.listdir()

# picking up mp3 audio files in the folder 
for file in audio_files:
    name, ext = os.path.splitext(file)
    if ext == ".mp3":
       mp3_sound = AudioSegment.from_mp3(file)
       #saving the wav files
       mp3_sound.export("{0}.wav".format(name), format="wav")