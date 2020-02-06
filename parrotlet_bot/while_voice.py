__author__ = 'Timothy Lam'

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import requests
import speech_recognition as sr
import wikipedia
import pyttsx3
from selenium import webdriver
import re

# bot = ChatBot('Bot')
# bot.set_trainer(ListTrainer)


bot = ChatBot('Bot', storage_adapter='chatterbot.storage.SQLStorageAdapter',
              logic_adapters=[
                  {'import_path': 'chatterbot.logic.BestMatch'},
                  {'import_path': 'chatterbot.logic.LowConfidenceAdapter',
                   'threshold': 0.20,
                   'default_response': 'I am sorry, but I do not understand.'
                   }
              ],
              trainer='chatterbot.trainers.ListTrainer')
bot.set_trainer(ListTrainer)


def parrotlet_voice(word_speech):
    engine = pyttsx3.init()
    engine.say(word_speech)
    engine.runAndWait()


def play_song(song):
    # chromedriver = "C:\Program Files\chrome driver"
    # driver = webdriver.Chrome(chromedriver)
    driver = webdriver.Chrome(executable_path=r"C:\Program Files\chrome driver\chromedriver.exe")
    query = "https://www.youtube.com/results?search_query="
    search = query + song
    driver.get(search)


def speech_recog():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            audio = r.listen(source)

            try:
                text = r.recognize_google(audio)
                if text.lower() == "wake up":
                    print('How can I help?...')
                    parrotlet_voice('how can i help..')
                    audio_query = r.listen(source)
                    try:
                        query = r.recognize_google(audio_query)
                        break
                    except:
                        print('sorry could not recognize your voice')
            except:
                pass
    return query


def weather(place):
    try:
        api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=73f448c069df192842fc72a34f8ea837='
        word = place.split(' ')
        if len(word) == 1:
            city = word[0]
        else:
            city = word[0] + ',' + word[1]

        url = api_address + city

        json_data = requests.get(url).json()
        desc = json_data['weather'][0]['description']
        temp_f = json_data['main']['temp']
        wind = json_data['wind']['speed']

        temp_c = round(temp_f - 273)

        forecast = f"{desc} in {city}. The temperature is {temp_c}° celcius with wind speed of {wind}"

    except:
        forecast = 'Sorry could not find {}'.format(place)

    return forecast


def rihanna_speak():
    while True:
        message = speech_recog()
        if message.strip()[0:7] == 'what is':
            try:
                reply = wikipedia.summary(message.strip()[7:], sentences=1)
                print('Parrotlet :', reply)
                parrotlet_voice(reply)
            except:
                print('Parrotlet :', '{}? hmm.. I know what it is but I can not tell you'.format(message.strip()[7:]))
                parrotlet_voice("{}? hmm.. I know what it is but I can not tell you".format(message.strip()[7:]))
        elif message.strip() == 'goodbye Rihanna':
            print('Parrotlet : Bye {}'.format(name))
            parrotlet_voice('Bye {}'.format(name))
            break

        elif message.strip() == 'weather forecast today':
            reply = weather('london,uk')
            print('Rihanna :', reply)
            rihanna_voice(reply)
        elif message.strip()[0:16] == 'weather forecast':
            reply = weather(message.strip()[16:].strip())
            print('Rihanna :', reply)
            rihanna_voice(reply)
        elif message.strip()[0:4] == 'play':
            print('Rihanna :', 'Search for {}'.format(message.strip()[5:]))
            rihanna_voice('Search for {}'.format(message.strip()[5:]))
            play_song(message.strip()[5:])

        elif message.strip() != 'Bye':
            reply = bot.get_response(message)
            print('Rihanna :', reply)
            if str(reply)[:3] == '- -':
                rihanna_voice(str(reply)[3:])
            elif str(reply)[0] == '-':
                rihanna_voice(str(reply)[1:])
            else:
                rihanna_voice(reply)


def rihanna():
    while True:
        message = input('{} : '.format(name.capitalize()))
        if message.strip()[0:7] == 'what is':
            try:
                reply = wikipedia.summary(message.strip()[7:], sentences=1)
                print('Rihanna :', reply)
                rihanna_voice(reply)
            except:
                print('Rihanna :', '{}? hmm.. I know what it is but I can not tell you'.format(message.strip()[7:]))
                rihanna_voice("{}? hmm.. I know what it is but I can not tell you".format(message.strip()[7:]))
        elif message.strip() == 'goodbye Rihanna':
            print('Rihanna : Bye {}'.format(name))
            rihanna_voice('Bye {}'.format(name))
            break

        elif message.strip() == 'weather forecast today':
            reply = weather('london,uk')
            print('Rihanna :', reply)
            rihanna_voice(reply)
        elif message.strip()[0:16] == 'weather forecast':
            reply = weather(message.strip()[16:].strip())
            print('Rihanna :', reply)
            rihanna_voice(reply)

        elif message.strip()[0:4] == 'play':
            print('Rihanna :', 'Searching for {}'.format(message.strip()[5:]))
            rihanna_voice('Searching for {}'.format(message.strip()[5:]))
            play_song(message.strip()[5:])

        elif message.strip() != 'Bye':
            reply = bot.get_response(message)
            print('Rihanna :', reply)
            if str(reply)[:3] == '- -':
                rihanna_voice(str(reply)[3:])
            elif str(reply)[0] == '-':
                rihanna_voice(str(reply)[1:])
            else:
                rihanna_voice(reply)


def main():
    global name

    name = 'Emeka'
    '''
    print('Rihanna : What is your name?')
    rihanna_voice("What is your name?")
    while True:
        name = input('You : ')
        p = "Valid" if re.match("^[a-zA-Z]*$", name) else "Invalid"
        if p == "Valid":
            break
        else:
            print('Rihanna : Only Alphabetical characters you menace!')
            rihanna_voice('Only Alphabetical characters you menace!')
    print('Rihanna : Hello {}!'.format(name))
    rihanna_voice("Hello {}!".format(name))
    '''
    print('say \'hello\' to start')
    rihanna_speak()


if __name__ == "__main__":
    main()
