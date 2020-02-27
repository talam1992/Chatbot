__author__ = 'Timothy Lam'

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import requests
import wikipedia
import pyttsx3
from selenium import webdriver
from parrotlet_bot import parrotlet_football, parrotlet_speak, parrotlet_tweet, parrotlet_news, parrotlet_skype, parrotlet_one_char, \
    parrotlet_time, parrotlet_maths as calc, parrotlet_email, parrotlet_tfl, parrotlet_spell, parrotlet_facebook, parrotlet_amazon, \
    parrotlet_dict, parrotlet_wc,parrotlet_man, parrotlet_job, parrotlet_youtube, parrotlet_google_image, parrotlet_windows, parrotlet_nhs
import config
import random as r

bot = ChatBot('Bot', storage_adapter='chatterbot.storage.SQLStorageAdapter',
              logic_adapters=[
                  {'import_path': 'chatterbot.logic.BestMatch'},
                  {'import_path': 'chatterbot.logic.LowConfidenceAdapter',
                   'threshold': 0.50,
                   'default_response': 'I am sorry. I am not allowed to give an answer to that question.'
                   }
              ],
              trainer='chatterbot.trainers.ListTrainer')
bot.set_trainer(ListTrainer)

break_words = ["yes", "no", "okay", "yeah", "ok", "nah", "alright", "i see"]
_date = ("what is the date", "what is todays date", "todays date", "current date", "date")
_time = ("what is the time", "time", "what is the current time", "current time")
email = {'msg': '', 'address': '', 'subject': '', 'run': 0}
run_email = {1: 'which email address do you want to send to?', 2: 'what is the subject?',
             3: 'what do you wish to send to '}


def email_thread(message):
    global email

    if email['run'] == 4:
        msg = message
        address = email['address']
        subject = email['subject']
        email = {'msg': '', 'address': '', 'subject': '', 'run': 0}
        return parrotlet_email.send_email(subject=subject, msg=msg, _send_email=address)

    elif email['run'] == 3:
        email['subject'] = message
        return run_email[3] + email['address']

    elif email['run'] == 1:
        return run_email[1]

    elif email['run'] == 2:
        if parrotlet_email.check(message) == 'valid':
            email['address'] = message
            return run_email[2]
        elif message in parrotlet_email.contact:
            email['address'] = parrotlet_email.contact[message]
            return run_email[2]
        else:
            email['run'] -= 1
            return f"{message} is an invalid email, please give a valid mail"


def parrotlet_voice(word_speech):
    engine = pyttsx3.init()
    engine.say(word_speech)
    engine.runAndWait()


def google_search(query):
    try:
        driver = webdriver.Chrome(executable_path=r"C:\Program Files\chrome driver\chromedriver.exe")
        google = "https://www.google.com/search?q="
        search = google + query
        driver.get(search)
        return driver
    except Exception as e:
        return "Web Driver Failed"


def play_song(song):
    driver = webdriver.Chrome(executable_path=r"C:\Program Files\chrome driver\chromedriver.exe")
    query = "https://www.youtube.com/results?search_query="
    search = query + song
    driver.get(search)
    driver.find_element_by_xpath(xpath='//*[@id="dismissable"]').click()


def format_string(string):
    d = "!?\|:;@'][<>"

    for c in d:
        if c in string:
            string = string.replace(c, '')
    return string


def weather(place):
    try:
        api_address = f'http://api.openweathermap.org/data/2.5/weather?appid={config.weather_id}='
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
        forecast = 'Sorry could not find location {}'.format(place)

    return forecast


def stop_words():
    response = ["okay", "ok", "alright", "great", "Thought as much", "Good"]

    return response[r.randrange(len(response))]


def parrotlet(message):
    if (message[:len("dictionary translate")] != "dictionary translate") and (
            parrotlet_dict.detect_lang(message) != 'en'):
        config.lang_code = parrotlet_dict.detect_lang(message)
        message = parrotlet_dict.translate_sentence_code(query=message, lang='en')['display']

        # print(f'trans: {message} \n l_code: {lang_code}')

        # Formatting message input
    if email['run'] == 0:
        if message.lower()[:3] == 'tfl':
            message = format_string(message).lower().strip()
            return parrotlet_skype.selector (format_string (message[6:]).lower ().strip ())
        elif message.lower()[:len('man')] == 'man':
            return parrotlet_man.selector(format_string(message).lower().strip())
        elif message.lower()[:len('amazon')] == 'amazon':
            return parrotlet_amazon.selector(format_string(message).lower().strip())
        elif message.lower()[:len('youtube')] == 'youtube':
            message_ = message[len("youtube")+1:]
            msg = format_string(message_).lower().strip()
            return parrotlet_youtube.search_youtube(msg)
        elif message.lower()[:len('dictionary')] == 'dictionary':
            return parrotlet_dict.selector(format_string(message).lower().strip())
        elif message.lower()[:len('job search')] == 'job search':
            return parrotlet_job.selector(format_string(message).lower().strip())
        else:
            message = parrotlet_spell.auto_correct(format_string(message).lower().strip())
    else:
        message = parrotlet_spell.auto_correct(message.lower().strip())

    # Main Decision Thread
    if email['run'] != 0:
        email['run'] += 1
        return email_thread(message)

    elif parrotlet_football.football_key['status'] == 1:
        return parrotlet_football.football_switch(message)

    elif {"send", "email"} - set(message.split()) == set():
        email['run'] += 1
        return email_thread(message)

    elif (len(message) == 1) or message.isdigit():
        return parrotlet_one_char.main(message)

    elif message[:len('word cloud')] == 'word cloud':
        return parrotlet_wc.selector(message)

    elif message[:len ('google image')] == 'google image':
        return parrotlet_google_image.selector (message)

    elif ("twitter" in message) or ("tweet" in message):
        return parrotlet_tweet.twitter(message)

    elif message[:len('windows')] == 'windows':
        return parrotlet_windows.selector(message)

    elif message[:len ('nhs')] == 'nhs':
        return parrotlet_nhs.selector (message)

    elif message in break_words:
        reply = stop_words()
        if config.lang_code != 'en':
            reply = parrotlet_dict.translate_sentence_code(reply, config.lang_code)
            config.lang_code = 'en'
        return reply

    elif message == 'why':
        reply = "Sorry, I cant tell you. Its a secret"
        if config.lang_code != 'en':
            reply = parrotlet_dict.translate_sentence_code(reply, config.lang_code)
            config.lang_code = 'en'
        return reply

    elif message == 'what is your name':
        reply = "My name is Parrotlet"
        if config.lang_code != 'en':
            reply = parrotlet_dict.translate_sentence_code(reply, config.lang_code)
            config.lang_code = 'en'
        return reply

    elif message in _date:
        reply = parrotlet_time.parrotlet_date()
        return reply

    elif message in _time:
        reply = parrotlet_time.parrotlet_time()
        return reply

    elif message[0:7] == 'what is':
        try:
            reply = wikipedia.summary(message.strip()[7:], sentences=1)
            if config.lang_code != 'en':
                reply = parrotlet_dict.translate_sentence_code(reply, config.lang_code)
                config.lang_code = 'en'
            return reply

        except:
            reply = "{}? hmm.. I know what it is but I can not tell you".format(message.strip()[7:])
            if config.lang_code != 'en':
                reply = parrotlet_dict.translate_sentence_code(reply, config.lang_code)
                config.lang_code = 'en'
            return reply

    elif {"bbc", "news"} - set(message.split()) == set():
        reply = parrotlet_news.bbc()
        return reply

    elif message == 'weather forecast today':
        reply = weather('london,uk')
        # rihanna_voice(reply)
        if config.lang_code != 'en':
            reply = parrotlet_dict.translate_sentence_code(reply, config.lang_code)
            config.lang_code = 'en'
        return reply

    elif "facebook" in message:
        return parrotlet_facebook.fb(message)

    elif message[:8] == 'football':
        reply = parrotlet_football.football(message)
        return reply

    elif message[:9] == 'calculate':
        data = message.strip()[10:]
        reply = calc.calculate(data)
        return reply

    elif message[:6] == 'google':
        search = message.strip()[7:]
        display = google_search(search)
        reply = "Googling . . ."
        if config.lang_code != 'en':
            reply = parrotlet_dict.translate_sentence_code(reply, config.lang_code)
            config.lang_code = 'en'
        return reply

    elif message[:3] == 'tfl':
        return parrotlet_tfl.tfl(message)

    elif message[0:16] == 'weather forecast':
        reply = weather(message.strip()[16:].strip())
        if config.lang_code != 'en':
            reply = parrotlet_dict.translate_sentence_code(reply, config.lang_code)
            config.lang_code = 'en'
        return reply

    elif message[0:4] == 'play':
        critic = ['that is a lovely song', 'that is a terrible song', "don't like that song",
                  "that's my jam", "someone turn the music up", "you have a terrible song taste"]
        # rihanna_voice('Searching for {}'.format(message.strip()[5:]))
        play_song(message.strip()[5:])
        reply = critic[r.randrange(len(critic))]
        if config.lang_code != 'en':
            reply = parrotlet_dict.translate_sentence_code(reply, config.lang_code)
            config.lang_code = 'en'
        return reply

    elif len([i for i in calc.opp_code if i in message]) > 0:
        reply = calc.calculate(message)
        return reply

    elif message != 'Bye':
        reply = bot.get_response(message)

        if str(reply)[:3] == '- -':
            # rihanna_voice(str(reply)[3:])
            reply = str(reply)[3:]
        elif str(reply)[0] == '-':
            # rihanna_voice(str(reply)[1:])
            reply = str(reply)[1:]
        else:
            # rihanna_voice(reply)
            pass
        if config.lang_code != 'en':
            reply = parrotlet_dict.translate_sentence_code(reply, config.lang_code)
            config.lang_code = 'en'
        return reply


def get_response(usrText):
    bot = ChatBot('Bot',
                  storage_adapter='chatterbot.storage.SQLStorageAdapter',
                  logic_adapters=[
                      {
                          'import_path': 'chatterbot.logic.BestMatch'
                      },
                      {
                          'import_path': 'chatterbot.logic.LowConfidenceAdapter',
                          'threshold': 0.50,
                          'default_response': 'I am sorry. I am not allowed to give an answer to that question.'
                      }
                  ],
                  trainer='chatterbot.trainers.ListTrainer')
    bot.set_trainer(ListTrainer)
    while True:
        if usrText.strip() == 'click':
            text = parrotlet_speak.speech_recog()
            print(f'speech: {text.strip()}')
            if text == 'sorry could not recognize your voice':
                reply = str(text)
                return reply
            else:
                result = parrotlet(text.strip())
                result = f"{text};{result}"
                reply = str(result)
                # return str({'user_sent': text, 'reply': result, 'voice_check': 0, 'say': ''})
                return reply
        elif usrText.strip() != 'Bye':
            result = parrotlet(usrText)
            reply = str(result)
            return reply  # reply should be string else it wont work
        elif usrText.strip() == 'Bye':
            return 'Bye'
