__author__ = 'Timothy Lam'

#Parrotlet world cloud
import sys
from os import path
import numpy as np
from PIL import Image
import wikipedia
from wordcloud import WordCloud, STOPWORDS
from parrotlet_bot import parrotlet_dict, parrotlet_tweet
import time
import os
import requests
from bs4 import BeautifulSoup
import config
import random as r

url2 = "https://www.google.com/search?q="

# get path to script's directory
currdir = path.dirname(__file__)


def scrap(query):
    req = url2 + query
    page = requests.get(req, headers=config.header)
    soup = BeautifulSoup(page.content, 'lxml')

    reply = ''
    for i in soup.find_all('p'):
        reply += i.text
    return reply


def selector(msg):

    if msg[:len('word cloud antonyms and synonyms')] == 'word cloud antonyms and synonyms':
        query = msg[len('word cloud antonyms and synonyms')+1:]
        return word_cloud_syn_ant(query)
    elif msg[:len('word cloud')] == 'word cloud':
        query = msg[len('word cloud')+1:]
        return word_cloud(query)
    elif msg[:len('word cloud twitter')] == 'word cloud twitter':
        query = msg[len('word cloud twitter')+1:]
        return word_cloud_twitter(query)
    elif msg[:len('word cloud twitter user')] == 'word cloud twitter user':
        query = msg[len('word cloud twitter user')+1:]
        return word_cloud_twitter(query, user=1)
    else:
        return "Rihanna is not in the mood for Word cloud at the moment"


def get_wiki(query):
    # get best matching title for given query
    title = wikipedia.search(query)[0]

    # get wikipedia page for selected title
    page = wikipedia.page(title)
    return page.content


def create_wordcloud(text):
    # create numpy araay for wordcloud mask image
    #img_list = ['cloud', 'pic', 'heart', 'house', 'dv']
    img_list = ['cloud', 'house', 'heart']
    an = r.randrange(len(img_list))
    img = img_list[an]
    mask = np.array(Image.open(path.join(currdir, f"{img}.png")))

    # create set of stopwords
    stopwords = set(STOPWORDS)

    # create wordcloud object
    wc = WordCloud(background_color="white",
                   max_words=200,
                   mask=mask,
                   stopwords=stopwords)

    # generate wordcloud
    wc.generate(text)

    # save wordcloud
    wc.to_file(path.join(currdir, r"C:\Users\Timothy Lam\Documents\Pycharm Projects\Chatbot\wc.png"))


def word_cloud_syn_ant(query):
    path = rf'C:\Users\Timothy Lam\Documents\Pycharm Projects\Chatbot\wc.png'
    try:
        os.remove(path)
    except Exception as e:
        pass
    text = parrotlet_dict.ant_syn(query)
    # generate wordcloud
    create_wordcloud(text)

    reply = {'display': f'<img src="wc.png?{time.time()}" alt="Test image" width="65%" height="65%">',
             'say': f'find word cloud for {query}'}

    return reply


def word_cloud(query):
    path = rf'C:\Users\emyli\PycharmProjects\Chatbot_Project\wc.png'
    try:
        os.remove(path)
    except Exception as e:
        pass
    # get text for given query
    try:
        text = get_wiki(query)
    except Exception as e:
        text = scrap(query)
    # generate wordcloud
    create_wordcloud(text)

    reply = {'display': f'<img src="wc.png?{time.time()}" alt="Test image" width="65%" height="65%">',
             'say': f'find word cloud for {query}'}

    return reply


def word_cloud_twitter(query, user=0):
    path = rf'C:\Users\Timothy Lam\Documents\Pycharm Projects\Chatbot\wc.png'
    try:
        os.remove(path)
    except Exception as e:
        pass
    if user == 1:
        # makes a word cloud of the twitter profiles of users that are taking about a given topic
        text = parrotlet_tweet.twitter_search_cloud_user(query)
    else:
        text = parrotlet_tweet.twitter_search_cloud(query)
    create_wordcloud(text)

    reply = {'display': f'<img src="wc.png?{time.time()}" alt="Test image" width="60%" height="60%">',
             'say': f'find word cloud from twitter for {query}'}

    return reply



#print(word_cloud('hello'))
