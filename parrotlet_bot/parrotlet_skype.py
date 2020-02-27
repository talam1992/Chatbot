__author__ = 'Timothy Lam'

from skpy import SkypeAuthException
from skpy import Skype

import trans_
import config as con
import datetime as dt


def selector(message):
    if message.strip()[:4] == 'chat':
        new_msg = message.strip()[5:].split()
        _name = new_msg[0]
        _msg = ' '.join(new_msg[1:])
        return RSkype(name=_name, message=_msg).send_message()
    elif message.strip()[:19] == 'get last message to':
        return RSkype(name=message[20:].strip()).get_last_message()
    elif message[:len('show picture')] == 'show picture':
        return RSkype(name=message[len('show picture') + 1:].strip()).show_picture()
    elif message[:len('birthday for')] == 'birthday for':
        name_ = message[len('birthday for') + 1:].strip()
        return RSkype(name=name_).birthday()
    else:
        return "Thou shall not answer the phrased question"


class RSkype:
    def __init__(self, name, message=None):
        self.name = name
        self.message = message
        sk = Skype(connect=False)
        sk.conn.setTokenFile(".tokens-app")
        try:
            sk.conn.readToken()
        except SkypeAuthException:
            sk.conn.setUserPwd(con.skype_name, con.skype_password)
            sk.conn.getSkypeToken()
        self.contacts = sk.contacts
        self.sk = sk

    def show_picture(self):
        if self.name.lower() in con.friends:
            p_id = con.friends[self.name.lower()]
            picture = f'<img src="https://avatar.skype.com/v1/avatars/{p_id}/public">'
            return picture
        elif self.name == 'me':
            path = "C:/Users/Timothy Lam/Documents/Pycharm Projects/Chatbot/img/me.png"
            # path = r"E:/deadlock files/img/public.png"
            # return f'<img src="{path}" alt="HTML5 Icon" width="128" height="128">'
            display = f'<img src="{path}" alt="Test image" width="65%" height="65%">'
            say = f'find picture of {self.name}'
            reply = {'display': display, 'say': say}
            if con.lang_code != 'en':
                reply['say'] = trans_.translate_sentence_code(reply['say'], con.lang_code)
                con.lang_code = 'en'
            return reply
        else:
            return f"Sorry I do not know {self.name}"

    def birthday(self):
        try:
            if self.name.lower() in con.friends:
                p_id = con.friends[self.name.lower()]
                _birth = self.contacts[p_id].birthday
                now = dt.date.today().year

                return f"{self.name} was born on {str(_birth)}, so {now - _birth.year} years old"
            else:
                return f"Sorry I do not know {self.name}"
        except AttributeError:
            return "Sorry I do not know"

    def send_message(self):
        if self.name.lower() in con.friends:
            chat = self.contacts[con.friends[self.name.lower()]].chat
            self.sk.chats[chat.id].sendMsg(self.message)
            return f"Message sent to {self.name}"
        else:
            try:
                self.group_chat()
                return f"Message sent to {self.name}"
            except KeyError:
                return f"{self.name} is not in your friend list"

    def get_last_message(self):
        if self.name.lower() in con.friends:
            chat = self.contacts[con.friends[self.name.lower()]].chat
            mg = self.sk.chats[chat.id].getMsgs()[0].content
            return f"{mg}"
        else:
            return f"{self.name} is not in your friend list"

    def group_chat(self):
        ski = self.sk.chats.create(members=(self.sk.userId, self.name), admins=(self.sk.userId,))
        ski.sendMsg(self.message)


# docs for skype
# https://github.com/Terrance/SkPy.docs
# https://pypi.org/project/SkPy/
#print(birthday('jess'))

