__author__ = 'Timothy Lam'

import requests
from bs4 import BeautifulSoup
import config


def selector(message):
    if message[:len("google images")] == "google images":
        msg = message[len("google images")+1:]
        return search_google_image_lot(msg)
    elif message[:len("google image")] == "google image":
        msg = message[len("google image")+1:]
        return search_google_image(msg)

    else:
        return "parrotlet cannot help with your query, use man help to navigate"


def search_google_image(query):
    url_ = "https://www.google.com/search?q="
    tail = "&sxsrf=ACYBGNRUxRetR93scVEO2O_eaShP8p7tfA:1581015953816&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiNx76yz73nAhVASxUIHUXUDdEQ_AUoAXoECBMQAw&biw=1536&bih=722"
    req = url_ + query + tail
    page = requests.get(req, headers=config.header)
    soup = BeautifulSoup(page.content, 'html.parser')
    load = soup.find("img", {"class": "rg_i Q4LuWd tx8vtf"}).get('data-iurl')
    reply = {'display': f'<img src="{load}" alt="google image" width="60%" height="60%">',
             'say': f'find google image for {query}'}
    return reply


def search_google_image_lot(query):
    url_ = "https://www.google.com/search?q="
    tail = "&sxsrf=ACYBGNRUxRetR93scVEO2O_eaShP8p7tfA:1581015953816&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiNx76yz73nAhVASxUIHUXUDdEQ_AUoAXoECBMQAw&biw=1536&bih=722"
    req = url_ + query + tail
    page = requests.get(req, headers=config.header)
    soup = BeautifulSoup(page.content, 'html.parser')
    load = soup.find_all("img", {"class": "rg_i Q4LuWd tx8vtf"})
    display = ""
    for i in load:
        display += f'<img src="{i.get("data-iurl")}" alt="google images" width="30%" height="30%">'
    reply = {'display': f'{display}',
             'say': f'find google images for all {query}'}
    return reply