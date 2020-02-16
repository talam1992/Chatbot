__author__ = 'Timothy Lam'

def selector(query):
    if query in man_dict:
        return man_dict[query]()
    else:
        return "I am sorry. I do not know which man page you want. \nUse 'man help' to view your options"


def man_help():
    reply = ''
    reply += "<table id='t01'>\
                <tr>\
                    <th>Feature</th>\
                    <th>Manual Page</th>\
                </tr>\
                "
    for feature in man_dict:
        reply += f"<tr>\
                        <td><font color='blue'>{feature.replace('man ', '').capitalize()}</font></td>\
                        <td onclick='man_complete("+f'"{feature}"'+f")'>{feature}</td>\
                    </tr>"
    reply += "</table>"
    reply_ = {'display': reply, 'say': 'Please find below the features and manual pages'}
    return reply_


def man_maths():
    display = "<table id='t01'>\
                <tr>\
                    <th>Maths Usage</th>\
                </tr>\
                "
    m = ['+', '*', '-', '/']
    for i in m:
        display += f"<tr>\
                        <td onclick='man_complete("+f'"calculate 5 {i} 2"'+f")'>calculate 5 {i} 2</td>\
                    </tr>"
    display += "</table>"
    say = "Find below How to use the Maths feature"
    reply = {'display': display, 'say': say}
    return reply


def man_twitter():
    display = "<table id='t01'>\
                    <tr>\
                        <th>Twitter Usage</th>\
                    </tr>\
                    "
    func = ["show global trending topics on twitter",
            "show global trending topics on twitter graph",
            "show trending topics on twitter",
            "show my twitter status",
            "show twitter status for <b>user_twitter_id</b>",
            "show my last tweet",
            "show last twitter status for <b>user_twitter_id</b>",
            "tweet <b>message</b>",
            "show twitter hash tags associated with <b>query</b>",
            "search twitter <b>search_query</b>"]
    for i in func:
        j = i.replace('<b>', '[').replace('</b>', ']')
        display += f"<tr>\
                         <td onclick='man_complete(" + f'"{j}"' + f")'>{i}</td>\
                     </tr>"
    display += "</table>"
    say = "Find below How to use the Twitter feature"
    reply = {'display': display, 'say': say}
    return reply


def man_tfl():
    display = "<table id='t01'>\
                        <tr>\
                            <th>TFL Usage</th>\
                        </tr>\
                        "
    func = ["tfl tube service report",
            "tfl journey duration from <b>E6 5JP</b> to <b>E20 1EJ</b>",
            "tfl live arrivals for <b>Bus No.</b> at <b>Bus Stop Road</b>",
            "tfl live arrivals for <b>line</b> at <b>station</b>"]
    for i in func:
        j = i.replace('<b>', '[').replace('</b>', ']')
        display += f"<tr>\
                         <td onclick='man_complete(" + f'"{j}"' + f")'>{i}</td>\
                     </tr>"
    display += "</table>"
    say = "Find below How to use the TFL feature"
    reply = {'display': display, 'say': say}
    return reply


def man_news():
    display = "<table id='t01'>\
                    <tr>\
                        <th>News Usage</th>\
                    </tr>\
                            "
    display += f"<tr>\
                      <td onclick='man_complete("+'"BBC news"'+")'>BBC News</td>\
                </tr>"
    display += "</table>"
    say = "Find below How to use the News feature"
    reply = {'display': display, 'say': say}
    return reply


def man_email():
    display = "<table id='t01'>\
                    <tr>\
                        <th>Email Usage</th>\
                    </tr>\
                            "
    display += f"<tr>\
                      <td onclick='man_complete("+'"send email"'+")'>send email</td>\
                </tr>"
    display += "</table>"
    say = "Find below How to use the Email feature"
    reply = {'display': display, 'say': say}
    return reply


def man_google():
    display = "<table id='t01'>\
                        <tr>\
                            <th>Google Usage</th>\
                        </tr>\
                                "
    display += f"<tr>\
                    <td onclick='man_complete("+'"google [query]"'+")'>google <b>what_to_google</b></td>\
                </tr>"
    display += "</table>"
    say = "Find below How to use the google feature"
    reply = {'display': display, 'say': say}
    return reply


def man_skype():
    display = "<table id='t01'>\
                        <tr>\
                            <th>Skype Usage</th>\
                        </tr>\
                        "
    func = ["skype chat <b>friend_name</b> <b>message</b>",
            "show picture <b>friend_name</b>",
            "birthday for <b>friend_name</b>",
            "skype get last message to <b>friend_name</b>"]
    for i in func:
        j = i.replace('<b>', '[').replace('</b>', ']')
        display += f"<tr>\
                         <td onclick='man_complete(" + f'"{j}"' + f")'>{i}</td>\
                     </tr>"
    display += "</table>"
    say = "Find below How to use the Skype feature"
    reply = {'display': display, 'say': say}
    return reply


def man_wiki():
    display = "<table id='t01'>\
                        <tr>\
                            <th>Wikipedia Usage</th>\
                        </tr>\
                                "
    display += f"<tr>\
                    <td onclick='man_complete("+'"what is [query]"'+")'>what is <b>what_to_look_up></b></td>\
                </tr>"
    display += "</table>"
    say = "Find below How to use the Wikipedia feature"
    reply = {'display': display, 'say': say}
    return reply


def man_facebook():
    display = "<table id='t01'>\
                        <tr>\
                            <th>Facebook Usage</th>\
                        </tr>\
                        "
    func = ["show my facebook posts",
            "show facebook pages i like",
            "how many facebook friends do i have"]
    for i in func:
        display += f"<tr>\
                         <td onclick='man_complete(" + f'"{i}"' + f")'>{i}</td>\
                     </tr>"
    display += "</table>"
    say = "Find below How to use the Facebook feature"
    reply = {'display': display, 'say': say}
    return reply


def man_football():
    display = "<table id='t01'>\
                        <tr>\
                            <th>Football Usage</th>\
                        </tr>\
                        "
    func = ["football match today",
            "football league start",
            "football league status",
            "football top scorers",
            "football top scorers graph",
            "football match schedules for match <b>11</b>",
            ]
    for i in func:
        j = i.replace('<b>', '[').replace('</b>', ']')
        display += f"<tr>\
                         <td onclick='man_complete(" + f'"{j}"' + f")'>{i}</td>\
                     </tr>"
    display += "</table>"
    say = "Find below How to use the Football feature"
    reply = {'display': display, 'say': say}
    return reply


def man_time():
    display = "<table id='t01'>\
                        <tr>\
                            <th>Time Usage</th>\
                        </tr>\
                        "
    func = ("what is the time", "time", "what is the current time", "current time")
    for i in func:
        display += f"<tr>\
                         <td onclick='man_complete(" + f'"{i}"' + f")'>{i}</td>\
                     </tr>"
    display += "</table>"
    say = "Find below How to use the Time feature"
    reply = {'display': display, 'say': say}
    return reply


def man_date():
    display = "<table id='t01'>\
                        <tr>\
                            <th>Date Usage</th>\
                        </tr>\
                        "
    func = ("what is the date", "what is todays date", "todays date", "current date", "date")
    for i in func:
        display += f"<tr>\
                         <td onclick='man_complete(" + f'"{i}"' + f")'>{i}</td>\
                     </tr>"
    display += "</table>"
    say = "Find below How to use the Date feature"
    reply = {'display': display, 'say': say}
    return reply


def man_weather():
    display = "<table id='t01'>\
                        <tr>\
                            <th>Weather Usage</th>\
                        </tr>\
                        "
    func = ("weather forecast today", "weather forecast <b>Ho Chi Minh City, VN</b>")
    for i in func:
        j = i.replace('<b>', '[').replace('</b>', ']')
        display += f"<tr>\
                         <td onclick='man_complete(" + f'"{j}"' + f")'>{i}</td>\
                     </tr>"
    display += "</table>"
    say = "Find below How to use the Weather feature"
    reply = {'display': display, 'say': say}
    return reply


def man_youtube():
    display = "<table id='t01'>\
                        <tr>\
                            <th>Youtube Usage</th>\
                            <th>Description</th>\
                        </tr>\
                                "
    func = {"play <b>video_name</b>": "opens a new window to play video",
            "Youtube <b>video_name</b>": "plays embedded video within chat log",
            "Youtube loop <b>video_name</b>": "plays embedded video within chat log in a loop",
            }
    for i in func:
        j = i.replace('<b>', '[').replace('</b>', ']')
        display += f"<tr>\
                         <td onclick='man_complete(" + f'"{j}"' + f")'>{i}</td>\
                         <td onclick='man_complete(" + f'"{j}"' + f")'>{func[i]}</td>\
                     </tr>"
    display += "</table>"
    say = "Find below How to use the Youtube feature"
    reply = {'display': display, 'say': say}
    return reply


def man_amazon():
    display = "<table id='t01'>\
                        <tr>\
                            <th>Amazon Usage</th>\
                        </tr>\
                        "
    func = ["amazon least price for <b>item_name</b>",
            "amazon max price for <b>item_name</b>",
            "amazon sort price for <b>item</b> at <b>price</b>",
            "amazon sort rating for <b>item</b> at <b>rating</b>"
            ]
    for i in func:
        j = i.replace('<b>', '[').replace('</b>', ']')
        display += f"<tr>\
                         <td onclick='man_complete(" + f'"{j}"' + f")'>{i}</td>\
                     </tr>"
    display += "</table>"
    say = "Find below How to use the Amazon feature"
    reply = {'display': display, 'say': say}
    return reply


def man_dictionary():
    display = "<table id='t01'>\
                        <tr>\
                            <th>Dictionary Usage</th>\
                        </tr>\
                        "
    func = ["dictionary definition <em><b>word</b></em>",
            "dictionary synonym for <em><b>word</b></em>",
            "dictionary antonym for <em><b>word</b></em>",
            "dictionary translate <em><b>sentence</b></em> to <em><b>language</b></em>"
            ]
    for i in func:
        j = i.replace('<b>', '[').replace('</b>', ']').replace('<em>', '').replace('</em>', '')
        display += f"<tr>\
                             <td onclick='man_complete(" + f'"{j}"' + f")'>{i}</td>\
                         </tr>"
    display += "</table>"
    say = "Find below How to use the Dictionary feature"
    reply = {'display': display, 'say': say}
    return reply


def man_word_cloud():
    display = "<table id='t01'>\
                        <tr>\
                            <th>Word Cloud Usage</th>\
                        </tr>\
                        "
    func = ["word cloud <em><b>word</b></em>",
            "word cloud antonyms and synonyms <em><b>word</b></em>",
            "word cloud twitter <em><b>word</b></em>",
            "word cloud twitter user <em><b>word</b></em>"
            ]
    for i in func:
        j = i.replace('<b>', '[').replace('</b>', ']').replace('<em>', '').replace('</em>', '')
        display += f"<tr>\
                         <td onclick='man_complete(" + f'"{j}"' + f")'>{i}</td>\
                     </tr>"
    display += "</table>"
    say = "Find below How to use the Word Cloud feature"
    reply = {'display': display, 'say': say}
    return reply


def man_job_search():
    display = "<table id='t01'>\
                            <tr>\
                                <th>Job Search Usage</th>\
                            </tr>\
                            "
    func = ["job search average salary for <b>job</b> in <b>place</b>",
            "job search min salary for <b>job</b> in <b>place</b>",
            "job search max salary for <b>job</b> in <b>place</b>",
            "job search average salary graph for <b>job</b>"
            ]
    for i in func:
        j = i.replace('<b>', '[').replace('</b>', ']')
        display += f"<tr>\
                            <td onclick='man_complete("+f'"{j}"'+f")'>{i}</td>\
                        </tr>"
    display += "</table>"
    say = "Find below How to use the Job search feature"
    reply = {'display': display, 'say': say}
    return reply

def man_google_image():
    display = "<table id='t01'>\
                            <tr>\
                                <th>Google Image Usage</th>\
                                <th>Description</th>\
                            </tr>\
                            "
    func = ["Google image <b>image_query</b>",
            "Google images <b>image_query</b>",
            ]
    des = ["returns a single image to match search query", "returns at least 10 images to match search query"]
    for i in func:
        j = i.replace('<b>', '[').replace('</b>', ']')
        display += f"<tr>\
                            <td onclick='man_complete("+f'"{j}"'+f")'>{i}</td>\
                            <td onclick='man_complete(" + f'"{j}"' + f")'>{des[func.index(i)]}</td>\
                        </tr>"
    display += "</table>"
    say = "Find below How to use the google image feature"
    reply = {'display': display, 'say': say}
    return reply

man_dict = {'man help': man_help, 'man maths': man_maths, 'man twitter': man_twitter, 'man tfl': man_tfl,
            'man news': man_news, 'man email': man_email, 'man skype': man_skype, 'man facebook': man_facebook,
            'man football': man_football, 'man time': man_time, 'man date': man_date, 'man weather': man_weather,
            'man youtube': man_youtube, 'man google': man_google, 'man wikipedia': man_wiki, 'man wiki': man_wiki,
            'man amazon': man_amazon, 'man dictionary': man_dictionary, 'man word cloud': man_word_cloud,
            'man job search': man_job_search, 'man_google_image': man_google_image}

