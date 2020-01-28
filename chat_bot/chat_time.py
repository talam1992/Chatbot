__author__ = 'Timothy Lam'

import datetime
import time
import trans
import config

def chat_time():
    _time = str(datetime.datetime.now()).split()[1].split('.')[0]
    reply = f'The time is {_time}'
    if config.lang_code != 'en':
        reply = trans.translate_sentence_cide(reply, config.lang_code)
        config.lang_code = 'en'
    return reply

def chat_date():
    return time.ctime()
