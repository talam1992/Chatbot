__author__ = 'Timothy Lam'

import requests
from bs4 import BeautifulSoup
import config

url = "https://www.youtube.com/results?search_query="


def selector(message):
    if message[:len('youtube loop')] == "youtube loop":
        message_ = message[len("youtube loop") + 1:]
        return search_youtube_loop(message_)
    elif message[:len('youtube')] == "youtube":
        message_ = message[len("youtube") + 1:]
        return search_youtube(message_)
    else:
        return "Youtube is offline at the moment. refer to man youtube"


def search_youtube(query):
    try:
        req = url + query
        page = requests.get(req, headers=config.header)
        soup = BeautifulSoup(page.content, 'html.parser')
        load= soup.find("div", {"id": "img-preload"})
        li = load.find_all("img")
        vid = li[0].get("src").split('/')[4]
        #link = "https://www.youtube.com/watch?v=" + vid
        display = f'<iframe width="560" height="315"\
                src="https://www.youtube.com/embed/{vid}?autoplay=1" frameborder="0" allowfullscreen>\
                </iframe>'
        say = f"playing {query} video from youtube"
        reply = {'display': display, 'say': say}
        return reply
    except Exception as e:
        return {'display': e, 'say': e}


def search_youtube_loop(query):
    try:
        req = url + query
        page = requests.get(req, headers=config.header)
        soup = BeautifulSoup(page.content, 'html.parser')
        load= soup.find("div", {"id": "img-preload"})
        li = load.find_all("img")
        vid = li[0].get("src").split('/')[4]
        #link = "https://www.youtube.com/watch?v=" + vid
        display = f'<iframe width="560" height="315"\
                src="https://www.youtube.com/embed/{vid}?playlist={vid}&loop=1" frameborder="0" allowfullscreen>\
                </iframe>'
        say = f"playing {query} video from youtube in a loop"
        reply = {'display': display, 'say': say}
        return reply
    except Exception as e:
        return {'display': e, 'say': e}

#https://www.w3schools.com/html/html_youtube.asp