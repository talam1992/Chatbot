__author__ = 'Timothy Lam'

import config
import facebook

graph = facebook.GraphAPI(access_token=config.fb_access_token, version="2.12")


# graph.put_object(parent_object='me', connection_name='feed', message='Hello, world from parrotlet')


def fb(message):
    try:
        if {"facebook", "posts"} - set(message.split()) == set():
            return fb_feed()
        elif {"facebook", "pages", "like"} - set(message.split()) == set():
            return fb_likes()
        elif message == "how many facebook friends do i have":
            return f"You have {friends_num()} friends"
        else:
            return "Please ask me another question"
    except Exception as e:
        return f"Error in facebook"


def fb_likes():
    data = graph.get_object('me', fields=['likes'])
    reply = 'Top 5 facebook pages you like'
    for i in data['likes']['data'][:5]:
        reply += f"\n{i['name']}"
    return reply


def fb_feed():
    data = graph.get_object('me', fields=['feed'])
    reply = '5 Recent Facebook Posts'
    n = 0
    for i in data['feed']['data']:
        if "message" in i:
            reply += f"\nPosted '{i['message']}' on {i['created_time'].split('T')[0]}"
            n += 1
            if n == 5:
                break
    return reply


def friends_num():
    fr = graph.get_object('me', fields=['friends'])
    return fr['friends']['summary']['total_count']

# https://facebook-sdk.readthedocs.io/en/latest/api.html
# https://developers.facebook.com/tools/explorer/
# print(friends_num())
#print(fb("show my facebook posts"))
