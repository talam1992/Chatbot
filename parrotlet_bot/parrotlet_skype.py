__author__ = 'Timothy Lam'

from skpy import SkypeAuthException
from skpy import Skype

import trans_
import config as con
import datetime as dt

#sk = Skype(con.skype_name, con.skype_password)
sk = Skype(connect=False)
sk.conn.setTokenFile(".tokens-app")
try:
    sk.conn.readToken()
except SkypeAuthException:
    sk.conn.setUserPwd(con.skype_name, con.skype_password)
    sk.conn.getSkypeToken()
contacts = sk.contacts

'''
for i in c_ids:
    name = contacts.contact(i).name.first
    #print(name)
    if name:
        #print(name)
        friends[name.lower()] = i
'''


def _skype(message):
    if message.strip()[:4] == 'chat':
        new_msg = message.strip()[5:].split()
        _name = new_msg[0]
        _msg = ' '.join(new_msg[1:])
        return send_message(_name, _msg)
    elif message.strip()[:19] == 'get last message to':
        return get_last_message(message[20:].strip())
    else:
        return "Thou shall not answer the phrased question"


def show_picture(name):
    if name.lower() in con.friends:
        p_id = con.friends[name.lower()]
        picture = f'<img src="https://avatar.skype.com/v1/avatars/{p_id}/public">'
        return picture
    elif name == 'me':
        path = r"C:/Users/emyli/PycharmProjects/Chatbot_Project/img/file.png"
        #path = r"E:/deadlock files/img/public.png"
        #return f'<img src="{path}" alt="HTML5 Icon" width="128" height="128">'
        display =  f'<img src="file.png" alt="Test image" width="65%" height="65%">'
        say = f'find picture of {name}'
        reply = {'display': display, 'say': say}
        if con.lang_code != 'en':
            reply['say'] = trans_.translate_sentence_code(reply['say'], con.lang_code)
            con.lang_code = 'en'
        return reply
    else:
        return f"Sorry I do not know {name}"


def birthday(name):
    try:
        if name.lower() in con.friends:
            p_id = con.friends[name.lower()]
            _birth = contacts[p_id].birthday
            now = dt.date.today().year

            return f"{name} was born on {str(_birth)}, so {now - _birth.year} years old"
        else:
            return f"Sorry I do not know {name}"
    except AttributeError:
        return "Sorry I do not know"


def send_message(name, message):
    if name.lower() in con.friends:
        chat = contacts[con.friends[name.lower()]].chat
        sk.chats[chat.id].sendMsg(message)
        return f"Message sent to {name}"
    else:
        try:
            group_chat(name, message)
            return f"Message sent to {name}"
        except KeyError:
            return f"{name} is not in your friend list"


def get_last_message(name):
    if name.lower() in con.friends:
        chat = contacts[con.friends[name.lower()]].chat
        mg = sk.chats[chat.id].getMsgs()[0].content
        return f"{mg}"
    else:
        return f"{name} is not in your friend list"


def group_chat(name, message):
    ski = sk.chats.create(members=(sk.userId, name), admins=(sk.userId,))
    ski.sendMsg(message)

# docs for skype
# https://github.com/Terrance/SkPy.docs
# https://pypi.org/project/SkPy/
#print(birthday('jess'))

