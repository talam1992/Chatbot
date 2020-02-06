__author__ = 'Timothy Lam'

import speech_recognition as sr
import pyttsx3
import config


def rihanna_voice(word_speech):
    engine = pyttsx3.init()
    engine.say(word_speech)
    engine.runAndWait()


def speech_recog():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #print('speak')
        rihanna_voice("listening")
        #r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            #text = r.recognize_ibm(audio_data=audio, username=config.ibm['username'], password=config.ibm['password'])

            return text
        except Exception as e:
            #print('sorry could not recognize your voice')
            return 'sorry, could not recognize your voice'


"""
for this module to work you need speechreognition and pyaudio
install speechreognition directly from pip
for pyaudio first pip install pipwin
then pipwin install pyaudio
"""
#print(speech_recog())
#rihanna_voice('buen día')
