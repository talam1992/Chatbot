__author__ = 'Timothy Lam'

'''
for this module to  work you will need speechregonition and pyaudio
install speechrecognition directly from pip
for pyaudio first install pip install pipwin
then pipwin install pyaudio
'''

import speech_recognition as sr
import pyttsx3
import config

def chat_voice(speech):
    engine = pyttsx3.init()
    engine.say(speech)
    engine.runAndWait()

def speech_recog():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        chat_voice("listening")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            return text
        except Exception as e:
            return 'sorry, could not recognize your voice'