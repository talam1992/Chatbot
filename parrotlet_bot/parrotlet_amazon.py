__author__ = 'Timothy Lam'

import requests
from bs4 import BeautifulSoup
import config

url = "https://www.amazon.co.uk/s?k="
out = 0


def find_nearest(l, h, _array, x):
    global out

    if abs(l - h) == 1:
        if abs(_array[l] - x) > abs(_array[h] - x):
            out = h
        else:
            out = l
        return 0
    else:
        m = int((l + h) / 2)
        if _array[m] == x:
            out = m
            return 0
        elif _array[m] < x:
            find_nearest(m, h, _array, x)
        elif _array[m] > x:
            find_nearest(l, m, _array, x)


def get_number(word):
    newstr = ''.join((ch if ch in '0123456789.-e' else ' ') for ch in word)
    listOfNumbers = [float(i) for i in newstr.split()]
    return listOfNumbers[0]


def selector(msg):
    if msg[:len("amazon least price for")] == "amazon least price for":
        msg = msg[len("amazon least price for") + 1:].strip()
        return product_min_price(msg)
    elif msg[:len("amazon max price for")] == "amazon max price for":
        msg = msg[len("amazon max price for") + 1:].strip()
        return product_max_price(msg)
    elif msg[:len("amazon sort price for")] == "amazon sort price for":  # e.g amazon sort price for speakers at 11
        sub_msg = msg[len("amazon sort price for") + 1:].strip()
        msg, price_raw = sub_msg.split(' at ')
        price = get_number(price_raw)
        return sort_products(msg, [price, 0])
    elif msg[:len("amazon sort rating for")] == "amazon sort rating for":  # e.g amazon sort rating for speakers at 4.5
        sub_msg = msg[len("amazon sort rating for") + 1:].strip()
        msg, rate_raw = sub_msg.split(' at ')
        rate = get_number(rate_raw)
        return sort_products(msg, [0, rate])
    else:
        return "We apologise on behalf of our brothers and sister in amazon.co.uk"


def search_amazon(query):
    req = url + query
    page = requests.get(req, headers=config.header)
    soup = BeautifulSoup(page.content, 'html.parser')
    items = soup.find_all("div", {"class": "s-include-content-margin s-border-bottom"})
    item_dict = {}
    item_link = {}  # item_link = {item: [item_link, image_link, rating]}
    for i in items:
        try:
            _name = i.find("span", {"class": "a-size-medium a-color-base a-text-normal"}).get_text()
            raw_pice = i.find("span", {"class": "a-offscreen"}).get_text()[1:]
            _price = float(raw_pice.replace(',', '') if ',' in raw_pice else raw_pice)
            _link = i.find("a", {"class": "a-link-normal a-text-normal"}).get('href')
            _img = i.find("img", {"class": "s-image"}).get('src')
            _rate = i.find("span", {"class": "a-icon-alt"}).get_text()
            item_dict[_name] = _price
            item_link[_name] = [_link, _img, _rate]
        except AttributeError:
            continue
    return item_dict, item_link


def product_min_price(query):
    try:
        item_dict, item_link = search_amazon(query)
        if len(item_dict) == 0:
            item_dict, item_link = search_amazon(query.split()[0])
        if len(item_dict) == 0:
            return "I am not in the mood to search for that query"
        min_price = min(item_dict, key=item_dict.get)
        reply = "<table id='t01'>\
                      <tr>\
                        <th>Image</th>\
                        <th>Product Name</th>\
                        <th>Price</th>\
                        <th>Rating</th>\
                      </tr>\
                    "
        reply += f"<tr>\
                            <td><img src='{item_link[min_price][1]}' alt='{query} image' width='40%' height='40%'></td>\
                            <td><a href='https://www.amazon.co.uk{item_link[min_price][0]}' target='_blank'>{min_price}</a></td>\
                            <td>£{item_dict[min_price]}</td>\
                            <td>{item_link[min_price][2]}</td>\
                          </tr>"
        return reply
    except Exception as e:
        return f'Error in product_min_price: {e}'


def product_max_price(query):
    try:
        item_dict, item_link = search_amazon(query)
        if len(item_dict) == 0:
            item_dict, item_link = search_amazon(query.split()[0])
        if len(item_dict) == 0:
            return "I am not in the mood to search for that query"
        max_price = max(item_dict, key=item_dict.get)
        reply = "<table id='t01'>\
                          <tr>\
                            <th>Image</th>\
                            <th>Product Name</th>\
                            <th>Price</th>\
                            <th>Rating</th>\
                          </tr>\
                        "
        reply += f"<tr>\
                                <td><img src='{item_link[max_price][1]}' alt='{query} image' width='40%' height='40%'></td>\
                                <td><a href='https://www.amazon.co.uk{item_link[max_price][0]}' target='_blank'>{max_price}</a></td>\
                                <td>£{item_dict[max_price]}</td>\
                                <td>{item_link[max_price][2]}</td>\
                              </tr>"
        return reply
    except Exception as e:
        return f'Error in product_max_price: {e}'


def search_amazon_sort(query):
    req = url + query
    page = requests.get(req, headers=config.header)
    soup = BeautifulSoup(page.content, 'html.parser')
    items = soup.find_all("div", {"class": "s-include-content-margin s-border-bottom"})
    item_dict = {}
    item_link = {}  # item_link = {item: [item_link, image_link, rating]}
    item_rate = {}
    for i in items:
        try:
            _name = i.find("span", {"class": "a-size-medium a-color-base a-text-normal"}).get_text()
            raw_pice = i.find("span", {"class": "a-offscreen"}).get_text()[1:]
            _price = float(raw_pice.replace(',', '') if ',' in raw_pice else raw_pice)
            _link = i.find("a", {"class": "a-link-normal a-text-normal"}).get('href')
            _img = i.find("img", {"class": "s-image"}).get('src')
            _rate = float(i.find("span", {"class": "a-icon-alt"}).get_text().split()[0])
            item_dict[_name] = _price
            item_link[_name] = [_link, _img]
            item_rate[_name] = _rate
        except AttributeError:
            continue

    return item_dict, item_link, item_rate


def sort_products(query, _sort=(), no=5):  # _sort = [1,1]    [price, rate]
    try:
        reply = ''
        if len(_sort) == 0:
            item_dict, item_link, item_rate = search_amazon_sort(query)
            if len(item_dict) == 0:
                item_dict, item_link, item_rate = search_amazon_sort(query.split()[0])
            if len(item_dict) == 0:
                return "I am not in the mood to search for that query, ehhhhh."

            reply = "<table id='t01'>\
                      <tr>\
                        <th>Image</th>\
                        <th>Product Name</th>\
                        <th>Price</th>\
                        <th>Rating</th>\
                      </tr>\
                    "
            for i in list(item_dict.keys())[:no]:
                reply += f"<tr>\
                              <td><img src='{item_link[i][1]}' alt='{query} image' width='40%' height='40%'></td>\
                              <td><a href='https://www.amazon.co.uk{item_link[i][0]}' target='_blank'>{i}</a></td>\
                              <td>£{item_dict[i]}</td>\
                              <td>{item_rate[i]}</td>\
                            </tr>"
        elif _sort[0] != 0:
            item_dict, item_link, item_rate = search_amazon_sort(query)
            if len(item_dict) == 0:
                item_dict, item_link, item_rate = search_amazon_sort(query.split()[0])
            if len(item_dict) == 0:
                return "I am not in the mood to search for that query, ehhhhh."
            sorted_price = {k: v for k, v in sorted(item_dict.items(), key=lambda item: item[1])}
            '''
            start = 0
            j = 0

            for i in sorted_price.values():
                if i >= _sort[0]:
                    start = list(sorted_price.values()).index(i)
                    j = 1
                    break
            if (start == 0) and (j == 1):
                start = len(sorted_price)//2
                reply = "Could Not Find the requested price"
            '''
            find_nearest(0, h=len(sorted_price) - 1, _array=list(sorted_price.values()), x=_sort[0])
            start = out

            reply += "<table id='t01'>\
                      <tr>\
                        <th>Image</th>\
                        <th>Product Name</th>\
                        <th>Price</th>\
                        <th>Rating</th>\
                      </tr>\
                    "
            if len(sorted_price) > (start + no):
                for i in list(sorted_price.keys())[start:start + no]:
                    reply += f"<tr>\
                                <td><img src='{item_link[i][1]}' alt='{query} image' width='40%' height='40%'></td>\
                                <td><a href='https://www.amazon.co.uk{item_link[i][0]}' target='_blank'>{i}</a></td>\
                                <td>£{item_dict[i]}</td>\
                                <td>{item_rate[i]} / 5</td>\
                              </tr>"
            else:
                for i in list(sorted_price.keys())[-no:]:
                    reply += f"<tr>\
                                <td><img src='{item_link[i][1]}' alt='{query} image' width='40%' height='40%'></td>\
                                <td><a href='https://www.amazon.co.uk{item_link[i][0]}' target='_blank'>{i}</a></td>\
                                <td>£{item_dict[i]}</td>\
                                <td>{item_rate[i]} / 5</td>\
                              </tr>"

        elif _sort[1] != 0:
            item_dict, item_link, item_rate = search_amazon_sort(query)
            if len(item_dict) == 0:
                item_dict, item_link, item_rate = search_amazon_sort(query.split()[0])
            if len(item_dict) == 0:
                return "I am not in the mood to search for that query, ehhhhh."
            sorted_rate = {k: v for k, v in sorted(item_rate.items(), key=lambda item: item[1])}
            '''
            start = 0
            for i in sorted_rate.values():
                if i >= _sort[1]:
                    start = list(sorted_rate.values()).index(i)
                    break
                else:
                    start = len(sorted_rate)//2
                    reply = "No product with such rating at the moment"
            '''
            find_nearest(0, h=len(sorted_rate) - 1, _array=list(sorted_rate.values()), x=_sort[1])
            start = out

            reply += "<table id='t01'>\
                      <tr>\
                        <th>Image</th>\
                        <th>Product Name</th>\
                        <th>Price</th>\
                        <th>Rating</th>\
                      </tr>\
                    "
            if len(sorted_rate) > (start + no):
                for i in list(sorted_rate.keys())[start:start + no]:
                    reply += f"<tr>\
                                <td><img src='{item_link[i][1]}' alt='{query} image' width='40%' height='40%'></td>\
                                <td><a href='https://www.amazon.co.uk{item_link[i][0]}' target='_blank'>{i}</a></td>\
                                <td>£{item_dict[i]}</td>\
                                <td>{item_rate[i]} / 5</td>\
                              </tr>"
            else:
                for i in list(sorted_rate.keys())[-no:]:
                    reply += f"<tr>\
                                <td><img src='{item_link[i][1]}' alt='{query} image' width='40%' height='40%'></td>\
                                <td><a href='https://www.amazon.co.uk{item_link[i][0]}' target='_blank'>{i}</a></td>\
                                <td>£{item_dict[i]}</td>\
                                <td>{item_rate[i]} / 5</td>\
                              </tr>"
        reply += '~'
        return reply

    except Exception as e:
        return f'Error in amazon sort_product: {e}'
