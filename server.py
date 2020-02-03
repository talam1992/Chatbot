__author__ = 'Timothy Lam'

from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
from parrotlet import get_response
from parrotlet import parrotlet_voice
from threading import Thread
import ast


class ChatServer (WebSocket):

    def handleMessage(self):
        # echo message back to client
        message = self.data
        response = get_response (message)
        # self.sendMessage(response)
        if ";" in response:
            result = response.split (';')
            response = result[1]
            reply = result[0] + ';'

            '''
            '''
            if response[0] == '{':
                response = ast.literal_eval (response)
                answer = reply + response['display']
                h1 = Thread (target=self.sendMessage, args=(answer,))
                h2 = Thread (target=parrotlet_voice, args=(response['say'],))
                h1.start ()
                h2.start ()
            elif (response[0] == '<') and ('~' in response):
                say = 'find reply below'
                display_response = response
                answer = reply + display_response
                h1 = Thread (target=self.sendMessage, args=(answer,))
                h2 = Thread (target=parrotlet_voice, args=(say,))
                h1.start ()
                h2.start ()
            elif response[0] == '<':
                say = 'find reply below'
                display_response = response
                answer = reply + display_response
                h1 = Thread (target=self.sendMessage, args=(answer,))
                h2 = Thread (target=parrotlet_voice, args=(say,))
                h1.start ()
                h2.start ()
            elif '~' in response:
                say = 'find reply below'
                display_response = response
                answer = reply + display_response
                h1 = Thread (target=self.sendMessage, args=(answer,))
                h2 = Thread (target=parrotlet_voice, args=(say,))
                h1.start ()
                h2.start ()
            elif ("\n" and "|") in response:
                say = ""
                for i in response.split ('\n'):
                    if '|' in i:
                        say += "\n" + i.split ('|')[0]
                    else:
                        say += i
                display_response = response.replace ("\n", "<br>").replace ("|", "")
                answer = reply + display_response
                h1 = Thread (target=self.sendMessage, args=(answer,))
                h2 = Thread (target=parrotlet_voice, args=(say,))
                h1.start ()
                h2.start ()
            elif "\n" in response:
                display_response = response.replace ("\n", "<br>")
                answer = reply + display_response
                h1 = Thread (target=self.sendMessage, args=(answer,))
                h2 = Thread (target=parrotlet_voice, args=(response,))
                h1.start ()
                h2.start ()
            elif "|" in response:
                say = response.split ('|')[0] + "\n Link provided"
                _reply_ = response.replace ("|", "")
                answer = reply + _reply_
                h1 = Thread (target=self.sendMessage, args=(answer,))
                h2 = Thread (target=parrotlet_voice, args=(say,))
                h1.start ()
                h2.start ()
            else:
                answer = reply + response
                h1 = Thread (target=self.sendMessage, args=(answer,))
                h2 = Thread (target=parrotlet_voice, args=(response,))
                h1.start ()
                h2.start ()
        elif response[0] == '{':
            response = ast.literal_eval (response)
            h1 = Thread (target=self.sendMessage, args=(response['display'],))
            h2 = Thread (target=chat_voice, args=(response['say'],))
            h1.start ()
            h2.start ()

        elif (response[0] == '<') and ('~' in response):
            say = 'find reply below'
            display_response = response
            h1 = Thread (target=self.sendMessage, args=(display_response,))
            h2 = Thread (target=parrotlet_voice, args=(say,))
            h1.start ()
            h2.start ()

        elif response[0] == '<':
            say = 'find reply below'
            display_response = response
            h1 = Thread (target=self.sendMessage, args=(display_response,))
            h2 = Thread (target=parrotlet_voice, args=(say,))
            h1.start ()
            h2.start ()
        elif '~' in response:
            say = 'find reply below'
            display_response = response
            h1 = Thread (target=self.sendMessage, args=(display_response,))
            h2 = Thread (target=parrotlet_voice, args=(say,))
            h1.start ()
            h2.start ()
        elif ("\n" and "|") in response:
            say = ""
            for i in response.split ('\n'):
                if '|' in i:
                    say += "\n" + i.split ('|')[0]
                else:
                    say += i
            display_response = response.replace ("\n", "<br>").replace ("|", "")
            h1 = Thread (target=self.sendMessage, args=(display_response,))
            h2 = Thread (target=parrotlet_voice, args=(say,))
            h1.start ()
            h2.start ()
        elif "\n" in response:
            display_response = response.replace ("\n", "<br>")
            h1 = Thread (target=self.sendMessage, args=(display_response,))
            h2 = Thread (target=parrotlet_voice, args=(response,))
            h1.start ()
            h2.start ()
        elif "|" in response:
            say = response.split ('|')[0] + "\n Link provided"
            reply = response.replace ("|", "")
            h1 = Thread (target=self.sendMessage, args=(reply,))
            h2 = Thread (target=parrotlet_voice, args=(say,))
            h1.start ()
            h2.start ()
        else:
            h1 = Thread (target=self.sendMessage, args=(response,))
            h2 = Thread (target=parrotlet_voice, args=(response,))
            h1.start ()
            h2.start ()

    def handleConnected(self):
        print (self.address, 'connected')

    def handleClose(self):
        print (self.address, 'closed')


server = SimpleWebSocketServer ('', 8000, ChatServer)
server.serveforever ()
