from gtts import gTTS
import os
from playsound import playsound

text='hello'
'''with open('new.txt') as file:
    for line in file:
        text+=line'''

tts = gTTS(text)
tts.save('audio.mp3')
playsound('audio.mp3')
os.remove('audio.mp3')