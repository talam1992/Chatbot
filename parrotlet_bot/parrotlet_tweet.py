__author__ = 'Timothy Lam'

import twitter
from selenium import webdriver
import time
import ast
import config
import re
import parrotlet
import matplotlib.pyplot as plt
import numpy as np


api = twitter.Api(consumer_key=config.consumer_key,
                  consumer_secret=config.consumer_secret,
                  access_token_key=config.access_token,
                  access_token_secret=config.access_token_secret)


def twitter(message):
    if {"global", "trending", "twitter", "topics", "graph"} - set(message.split()) == set():
        reply = twitter_global_trends_graph()
        return reply
    elif {"global", "trending", "twitter", "topics"} - set(message.split()) == set():
        reply = twitter_global_trends()
        return reply

    elif {"trending", "twitter", "topics"} - set(message.split()) == set():
        reply = twitter_trend()
        return reply

    elif message == 'show my twitter status':
        reply = twitter_status()
        return reply

    elif message[:23] == 'show twitter status for':
        user = message.strip()[24:]
        reply = twitter_status_others(user)
        return reply

    elif message == 'show my last tweet':
        reply = last_tweet()
        return reply

    elif message[:28] == 'show last twitter status for':
        user = message.strip()[29:]
        reply = display_last_tweet(user)
        return reply

    elif message[:5] == 'tweet':
        try:
            tweet = message.strip()[6:]
            reply = post_tweet(tweet)
            display_twitter()
            return reply
        except Exception as e:
            return "Error occurred in twitter"

    elif message[:14] == 'search twitter':
        search = message[15:].strip()
        reply = twitter_search(search)
        return reply

    else:
        display = parrotlet.google_search(message)
        reply = "Googling . . ."
        return reply


def twitter_status_others(user):
    try:
        followers_count = len(api.GetFollowers(screen_name=user))
        friends_count = len(api.GetFriends(screen_name=user))
        return f"{user} have {followers_count} followers and {friends_count} friends following you on twitter"
    except Exception as e:
        return "Due to Twitter Restrictions, You have reached your lookup limit. Try again in 15 minutes"


def twitter_status():
    followers_count = len(api.GetFollowers())
    friends_count = len(api.GetFriends())
    return f"You have {followers_count} followers and {friends_count} friends following you on twitter"


def display_last_tweet(user):
    try:
        status = api.GetUserTimeline(screen_name=user)[0].text
        return status
    except Exception as e:
        return "Due to Twitter Restrictions, You have reached your lookup limit. Try again in 15 minutes"


def last_tweet():
    status = api.GetUserTimeline()[0].text
    return status


def post_tweet(tweet):
    api.PostUpdates(tweet)
    return "Tweet posted"


def display_twitter():
    driver = webdriver.Chrome(executable_path=r"C:\Program Files\chrome driver\chromedriver.exe")
    query = "https://twitter.com/jamesemyking"
    driver.get(query)
    time.sleep(10)


def twitter_trend():
    results = api.GetTrendsWoeid(woeid=23424975)

    reply = "Top UK Trends in Twitter: "

    for _location in results[:5]:
        location = ast.literal_eval(str(_location))
        reply += ("\n " + str(location["name"]))

    return reply


def plot_tweet(tweet_data):     #tweet_data = {tweets: tweet_volume}
    tweets = tweet_data.keys()
    y_pos = np.arange(len(tweets))
    plt.rcdefaults()
    fig, ax = plt.subplots()
    ax.barh(y_pos, tweet_data.values(), align='center', color='b', alpha=0.3)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(tweets, labelpad=70)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Tweet Volume')
    ax.set_title('Global Twitter Trends Plot')
    plt.savefig(r'C:\Users\emyli\PycharmProjects\Chatbot_Project\tweet.png')


def twitter_global_trends_graph():
    try:
        result = api.GetTrendsCurrent()[:5]
        tweet_data = {}

        for trend in result:
            _trend = ast.literal_eval(str(trend))
            name = _trend['name']
            try:
                volume = int(_trend['tweet_volume'])
            except KeyError:
                if len(tweet_data) == 0:
                    volume = 1000
                else:
                    k = min(tweet_data, key=tweet_data.keys())
                    volume = k + 1000
            tweet_data[name] = volume
        plot_tweet(tweet_data)
        picture = f'<img src="tweet.png?{time.time()}" alt="Graph of Top Global Trends in Twitter" width="65%" height="65%">'
        # time.sleep(1)
        reply_ = {'display': picture,
                  'say': f"Find below a graph of Top Global Trends in Twitter"}

        return reply_
    except Exception as e:
        return 'Twitter is currently withholding this information | ' \
               '<a href="https://trends24.in/" target="_blank">view</a>'


def twitter_global_trends():
    try:
        result = api.GetTrendsCurrent()[:5]
        reply = "Top Global Trends in Twitter: "

        for trend in result:
            _trend = ast.literal_eval(str(trend))
            name = _trend['name']
            try:
                volume = _trend['tweet_volume']
            except KeyError:
                volume = "_ number of"
            url = _trend['url']

            reply += f'\n{name} ({volume} Tweets) | <a href={url} target="_blank">view</a>'

        return reply
    except Exception as e:
        return 'Twitter is currently withholding this information | ' \
               '<a href="https://trends24.in/" target="_blank">view</a>'


def twitter_search(query):
    result = str(api.GetSearch(term=query, count=5)).replace('Status', '').replace("'", "")[:-2].split('), (')
    reply = "Top 5 Search Results :"
    for status in result:
        obj = status.split('=')
        tweet = obj[-1]
        links = re.findall(r'(https?://\S+)', tweet)
        if links:
            for i in links:
                link = f'|<a href={i} target="_blank">link</a>'
                #print(i, link)
                tweet = tweet.replace(i, link)
        user = obj[2].split(',')[0]
        reply += f"\n@{user} Tweeted: {tweet}"
    return reply
