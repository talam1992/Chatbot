__author__ = 'Timothy Lam'

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import requests
import wikipedia
import pyttsx3
from selenium import webdriver
from chat_bot import chat_amazon, chat_dict, chat_email, chat_maths as calc, chat_news, chat_one_char, \
     chat_speak, chat_tfl, chat_time
import config
import random as r

bot = ChatBot ('Bot', storage_adapter='chatterbot.storage.SQLStorageAdapter',
               logic_adapters=[
                   {'import_path': 'chatterbot.logic.BestMatch'},
                   {'import_path': 'chatterbot.logic.LowConfidenceAdapter',
                    'threshold': 0.70,
                    'default_response': 'I am sorry, I am not allowed to give you an answer to that question.'
                    }
               ],
               trainer='chatterbot.trainers.ListTrainer')
bot.set_trainer (ListTrainer)

break_words = ["yes", "no", "okay", "yeah", "ok", "nah", "alright", "i see"]
_date = ("what is the date", "what is todays date", "todays date", "current date", "date")
_time = ("what is the time", "time", "what is the current time", "current time")
email = {'msg': '', 'address': '', 'subject': '', 'run': 0 }
run_email = {1: 'which email address do you want yo send to?', 2: 'what is the subject?',
             3: 'what do you wish to send'}

def email_thread(message):
    global email

    if email('run') == 4:
        msg = message
        address = email['address']
        subject = email['subject']
        email = {'msg' : '', 'address': '', 'subject': '', 'run': 0}
        return chat_email.send_email(subject=subject, msg=msg, _send_email=address)

    elif email['run'] == 3:
        email['subject'] = message
        return run_email[3] + email['address']

    elif email['run'] == 1:
        return run_email[1]

    elif email['run'] == 2:
        if chat_email.check(message) == 'valid':
            email['address'] = message
            return run_email[2]
        elif message in chat_email.contact:
            email['address'] = chat_email.contact[message]
            return run_email[2]
        else:
            email['run'] -= 1
            return f"{message} is an invalid email, please give a valid mail"

def chat_voice(speech):
    engine = pyttsx3.init()
    engine.say(speech)
    engine.runAndWait()

def google_search(query):
    try:
        driver = webdriver.Chrome("C:\Program Files\chrome driver\chromedriver.exe")
        google = "https://www.google.com/search?q="
        search = google + query
        driver.get(search)
        return driver
    except Exception as e:
        return "Web Driver Failed"

def play_song(song):
    driver = webdriver.Chrome("C:\Program Files\chrome driver\chromedriver.exe")
    query = "https://www.youtube.com/results?search_query"
    search = query + song
    driver.get(search)
    driver.find_element_by_xpath(xpath='//*[@ide="dismissable"]').click()


def format_string(string):
    d = "!?\|:@'"
    for c in d:
        if c in string:
            string = string.replace(c, '')
    return string

def weather(place):
    try:
        api_address = f'api.openweathermap.org/data/2.5/weather?q={config.weather_id}='
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
        forecast = f"{desc} in {city }. The temperature is {temp_c}° celcius with wind speed of {wind}"
    except:
        forecast = 'Sorry could not find location {}'.format(place)

    return forecast

def stop_words():
    response = ["okay", "ok", "alright", "great", "Thought as much", "Good"]
    return response[r.randrange(len(response))]

def chat(message):
    if (message[:len("dictionary translate")] != "dictionary translate") and (chat_dict.dectec_lang(message) != 'en'):
        config.lang_code = chat_dict.detect_lang(message)
        message = chat_dict.translate_sentence_code(query=message, lang='en')['display']

        # Formatting message input
    if email['run'] == 0:
        if message[:3] == 'tfl':
            message = format_string (message).lower ().strip ()
        elif message[:12] == 'show picture':
            return chat_skype.show_picture (message[13:].strip ())
        elif message[:len ('birthday for')] == 'birthday for':
            return chat_skype.birthday (message[len ('birthday for') + 1:].strip ())
        elif message[:5] == 'skype':
            return chat_skype.skype (message[6:])
        elif message[:len ('amazon')] == 'amazon':
            return chat_amazon.selector (format_string (message).lower ().strip ())
        elif message[:len ('dictionary')] == 'dictionary':
            return chat_dict.selector (message)
        else:
            message = chat_spell.auto_correct (format_string (message).lower ().strip ())
    else:
        message = chat_spell.auto_correct (message.lower ().strip ())

        # Main Decision Thread
    if email['run'] != 0:
        email['run'] += 1
        return email_thread (message)

    elif chat_football.football_key['status'] == 1:
        return chat_football.football_switch (message)

    elif {"send", "email"} - set (message.split ()) == set ():
        email['run'] += 1
        return email_thread (message)

    elif (len (message) == 1) or message.isdigit ():
        return chat_one_char.main (message)

    elif ("twitter" in message) or ("tweet" in message):
        return chat_tweet.twitter (message)

    elif message in break_words:
        reply = stop_words ()
        if config.lang_code != 'en':
            reply = chat_dict.translate_sentence_code (reply, config.lang_code)
            config.lang_code = 'en'
        return reply

    elif message == 'why':
        reply = "Sorry, I cant tell you. Its a secret"
        if config.lang_code != 'en':
            reply = chat_dict.translate_sentence_code (reply, config.lang_code)
            config.lang_code = 'en'
        return reply

    elif message == 'what is your name':
        reply = "My name is Chatbot"
        if config.lang_code != 'en':
            reply = chat_dict.translate_sentence_code (reply, config.lang_code)
            config.lang_code = 'en'
        return reply

    elif message in _date:
        reply = chat_time.chat_date ()
        return reply

    elif message in _time:
        reply = chat_time.chat_time()
        return reply

    elif message[:len ('word cloud')] == 'word cloud':
        return chat_wc.selector (message)

    elif message[0:7] == 'what is':
        try:
            reply = wikipedia.summary (message.strip ()[7:], sentences=1)
            if config.lang_code != 'en':
                reply = chat_dict.translate_sentence_code (reply, config.lang_code)
                config.lang_code = 'en'
            return reply

        except:
            reply = "{}? hmm.. I know what it is but I can not tell you".format (message.strip ()[7:])
            if config.lang_code != 'en':
                reply = chat_dict.translate_sentence_code (reply, config.lang_code)
                config.lang_code = 'en'
            return reply

    elif {"bbc", "news"} - set (message.split ()) == set ():
        reply = chat_news.bbc ()
        return reply

    elif message == 'weather forecast today':
        reply = weather ('london,uk')
        if config.lang_code != 'en':
            reply = chat_dict.translate_sentence_code (reply, config.lang_code)
            config.lang_code = 'en'
        return reply

    elif "facebook" in message:
        return chat_facebook.fb (message)

    elif message[:8] == 'football':
        reply = chat_football.football (message)
        return reply

    elif message[:9] == 'calculate':
        data = message.strip ()[10:]
        reply = calc.calculate (data)
        return reply

    elif message[:6] == 'google':
        search = message.strip ()[7:]
        display = google_search (search)
        reply = "Googling . . ."
        if config.lang_code != 'en':
            reply = chat_dict.translate_sentence_code (reply, config.lang_code)
            config.lang_code = 'en'
        return reply

    elif message[:3] == 'tfl':
        return chat_tfl.tfl (message)

    elif message[0:16] == 'weather forecast':
        reply = weather (message.strip ()[16:].strip ())
        if config.lang_code != 'en':
            reply = chat_dict.translate_sentence_code (reply, config.lang_code)
            config.lang_code = 'en'
        return reply

    elif message[0:4] == 'play':
        critic = ['that is a lovely song', 'that is a terrible song', "don't like that song",
                  "that's my jam", "someone turn the music up", "you have a terrible song taste"]
        # rihanna_voice('Searching for {}'.format(message.strip()[5:]))
        play_song (message.strip ()[5:])
        reply = critic[r.randrange (len (critic))]
        if config.lang_code != 'en':
            reply = chat_dict.translate_sentence_code (reply, config.lang_code)
            config.lang_code = 'en'
        return reply

    elif len ([i for i in calc.opp_code if i in message]) > 0:
        reply = calc.calculate (message)
        return reply

    elif message != 'Bye':
        reply = bot.get_response (message)

        if str (reply)[:3] == '- -':
            reply = str (reply)[3:]
        elif str (reply)[0] == '-':
            reply = str (reply)[1:]
        else:
            pass
        if config.lang_code != 'en':
            reply = chat_dict.translate_sentence_code (reply, config.lang_code)
            config.lang_code = 'en'
        return reply

def get_response(usrText):
    bot = ChatBot('Bot', storage_adapter='chatterbot.storage.SQLStorageAdapter',
                  logic_adapters=[
                      {'import_path': 'chatterbot.logic.BestMatch'},
                      {'import_path': 'chatterbot.logic.LowConfidenceAdapter',
                       'threshold': 0.70,
                       'default_response': 'I am sorry, but I do not understand.'
                       }
                  ],
                  trainer='chatterbot.trainers.ListTrainer')
    bot.set_trainer(ListTrainer)
    while True:
        if  usrText.strip() == 'click':
            text = chat_speak.speech_recog()
            print(f'speech: {text.strip()}')
            if text == 'sorry could not recognize your voice':
                reply = str(text)
                return reply
            else:
                result = chat(text.strip())
                result = f"{text};{result}"
                reply = str(result)
                return reply
        elif usrText.strip()!= 'Bye':
            result = bot.get_response(usrText)
            reply = str(result)
            return(reply)
        elif usrText.strip() == 'Bye':
            return('Bye')



