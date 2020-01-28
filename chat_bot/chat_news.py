__author__ = 'Timothy Lam'

import requests
import config
import trans_


def bbc():
    # BBC news api
    main_url = f" https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey={config.news_key}"

    # fetching data in json format
    open_bbc_page = requests.get(main_url).json()

    # getting all articles in a string article
    article = open_bbc_page["articles"]
    if config.lang_code == 'en':
        display = "Top 5 BBC News :"
        say = "Top 5 BBC News :"

        nos = 1
        for ar in article[:5]:
            news = ar["title"]
            url = ar["url"]

            display += f'<br>{nos}. {news} <a href={url} target="_blank">Read</a></br>'

            say += f'\n{nos}. {news}'
            nos += 1
        reply_ = {'display': display, 'say': say}
    else:
        ans = trans_.translate_sentence_code("Top 5 BBC News", config.lang_code)
        display = ans['display'] + ':'
        say = "Top 5 BBC News"
        nos = 1
        for ar in article[:5]:
            news = trans_.translate_sentence_code(ar["title"], config.lang_code)['display']
            url = ar["url"]
            read = trans_.translate_sentence_code("Read", config.lang_code)['display']

            display += f'<br>{nos}. {news} <a href={url} target="_blank">{read}</a></br>'

            say += f'\n{nos}. {news}'
            nos += 1
        say = trans_.translate_sentence_code(say, config.lang_code)['say']
        reply_ = {'display': display, 'say': say}
        config.lang_code = 'en'

    return reply_


