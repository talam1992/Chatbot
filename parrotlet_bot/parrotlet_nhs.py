__author__ = "Timothy Lam"

# This script is using Python3
import urllib.request
import urllib.parse
import config
import json


def selector(message):
    if message[:len('nhs review on')] == 'nhs review on':
        msg = message[len('nhs review on') + 1:].strip()
        return HealthData(search=msg, branch="conditions").display_all()
    elif message[:len('nhs prevention for')] == 'nhs prevention for':
        msg = message[len('nhs prevention for') + 1:].strip()
        return HealthData(search=msg, branch="conditions", name="prevention").content_attrs()
    elif message[:len('nhs overview for')] == 'nhs overview for':
        msg = message[len('nhs overview for') + 1:].strip()
        return HealthData(search=msg, branch="conditions", name="overview").content_attrs()
    elif message[:len('nhs symptoms for')] == 'nhs symptoms for':
        msg = message[len('nhs symptoms for') + 1:].strip()
        return HealthData(search=msg, branch="conditions", name="symptoms").content_attrs()
    elif message[:len('nhs treatments overview for')] == 'nhs treatments overview for':
        msg = message[len('nhs treatments overview for') + 1:].strip()
        return HealthData(search=msg, branch="conditions", name="treatments_overview").content_attrs()
    elif message[:len('nhs self care advice for')] == 'nhs self care advice for':
        msg = message[len('nhs self care advice for') + 1:].strip()
        return HealthData(search=msg, branch="conditions", name="self_care").content_attrs()
    elif message[:len('nhs other treatments for')] == 'nhs other treatments for':
        msg = message[len('nhs other treatments for') + 1:].strip()
        return HealthData(search=msg, branch="conditions", name="other_treatments").content_attrs()
    elif message[:len('nhs causes for')] == 'nhs causes for':
        msg = message[len('nhs causes for') + 1:].strip()
        return HealthData(search=msg, branch="conditions", name="causes").content_attrs()
    elif message[:] == 'nhs health news':
        return HealthData(branch="conditions").display_news_all()
    elif message[:len('nhs medicine information on')] == 'nhs medicine information on':
        msg = message[len('nhs medicine information on') + 1:].strip()
        return HealthData(search=msg, branch='medicines').nhs_medicine()
    elif message[:len ('nhs search')] == 'nhs search':
        msg = message[len ('nhs search') + 1:].strip ()
        return HealthData (search=msg, branch="search").nhs_search ()
    else:
        return "NHS server cannot process that request at the moment"


class HealthData:
    def __init__(self, branch, search=None, name=None):
        self.request_headers = {
            "subscription-key": config.nhs_Key,
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
        }
        self.search = search
        self.branch = branch
        self.baseUrl = f"https://api.nhs.uk/{branch}/"
        self.name = name

    def display_all(self):
        if self.search == 'coronavirus':
            self.search = 'coronavirus-covid-19'
        pageURL = f"{self.baseUrl}/{self.search}"
        try:
            request = urllib.request.Request(pageURL, headers=self.request_headers)
            contents = json.loads(urllib.request.urlopen(request).read())
            reply = f"<h1><font color='blue'>NHS REVIEW ON {self.search.upper()}</font></h1>"
            for data_dict in contents["hasPart"]:
                reply += f"<h3>{data_dict['name'].capitalize().replace('_', ' ')}</h3>"
                text = data_dict["text"]
                if text == "":
                    text = data_dict["description"]
                reply += f"{text.replace(';', '').replace('api', 'www')}"
                reply += f'<a href="{data_dict["url"].replace("api", "www")}" target="_blank">Read More</a>'
            reply_ = {'display': reply,
                      'say': f'Find displayed a review on {self.search}. this information is provided by NHS'}
            return reply_

        except Exception:
            return f"cannot find result for {self.search}"

    def _get_parts(self, name):
        try:
            if self.search == 'coronavirus':
                self.search = 'coronavirus-covid-19'
            pageURL = f"{self.baseUrl}/{self.search}"
            request = urllib.request.Request(pageURL, headers=self.request_headers)
            contents = json.loads(urllib.request.urlopen(request).read())
            data_attrs = {}
            for data_dict in contents['hasPart']:
                text = data_dict["text"]
                if text == "":
                    text = data_dict["description"]
                data_attrs[data_dict["name"]] = text
            if name in data_attrs:
                return data_attrs[name]
            else:
                return 0
        except Exception:
            return 0

    def content_attrs(self):
        data = self._get_parts(self.name)
        if data != 0:
            reply = f"<h2><font color='blue'>{self.name.capitalize().replace('_', ' ')} of {self.search.upper()}</font></h2>"
            reply += f"{data.replace(';', '')}"
            reply += f'<a href="{self.baseUrl}/{self.search}/#{self.name}" target="_blank">Read More</a>'
            reply_ = {'display': reply,
                      'say': f'Find displayed {self.name.capitalize().replace("_", " ")} of {self.search}. '
                             f'this information is provided by NHS'}
            return reply_
        else:
            return f"cannot find result for {self.search}"

    def display_news_all(self):
        pageURL = f"{self.baseUrl}/?page=65"  # /?endDate=2020-01-09"
        request = urllib.request.Request(pageURL, headers=self.request_headers)
        contents = json.loads(urllib.request.urlopen(request).read())
        data = contents['significantLink'][:]
        display = ''
        for element_dict in data:
            display += f"<h3><font color='blue'>{element_dict['name']}</font></h3>"
            display += f"{element_dict['description']}"
            display += f"<a href={element_dict['url']} target='_blank'>Read More</a>"
            date = element_dict['mainEntityOfPage']['datePublished'].split('T')
            display += f"<font color='grey' size='2'><p>Published on {date[1].split('+')[0]}, {date[0]}</p></font>"

        reply = {'display': display,
                 'say': 'Find the displayed recent Health News. This information is brought to you by NHS'}
        # print(reply)
        return reply

    def nhs_medicine(self):
        pageURL = f"{self.baseUrl}/{self.search}"
        request = urllib.request.Request(pageURL, headers=self.request_headers)
        contents = json.loads(urllib.request.urlopen(request).read())
        heading9 = [f"About {self.search}", f"Key facts on {self.search}",
                    f"Who can and can't take {self.search}", f"How and when to take {self.search}",
                    f"Side effects of {self.search}", f"How to cope with side effects of {self.search}",
                    f"Pregnancy and breastfeeding",
                    f"Cautions with other medicines", f"Common questions"]
        heading10 = [f"About {self.search}", f"Key facts on {self.search}",
                     f"Who can and can't take {self.search}", f"How and when to take {self.search}",
                     f"Taking {self.search} with other painkillers",
                     f"Side effects of {self.search}", f"How to cope with side effects of {self.search}",
                     f"Pregnancy and breastfeeding",
                     f"Cautions with other medicines", f"Common questions"]
        display = f"<h2><font color='blue'> NHS MEDICINE PAGE FOR {self.search.upper()}</font></h2>"
        if len(contents['mainEntityOfPage']) > 9:
            for data_dict in contents['mainEntityOfPage']:
                ind = data_dict['position']
                if ind <= 9:
                    display += f"<h4>{heading10[ind]}</h4>"
                    display += f"{data_dict['mainEntityOfPage'][0]['text']}"
                else:
                    break
        else:
            for data_dict in contents['mainEntityOfPage']:
                ind = data_dict['position']
                display += f"<h4>{heading9[ind]}</h4>"
                display += f"{data_dict['mainEntityOfPage'][0]['text']}"

        reply = {'display': display.replace(';', ''),
                 'say': f'Find the displayed information on {self.search}. This information is brought to you by NHS'}
        # print(reply)
        return reply

    def nhs_search(self):
        pageURL = f"{self.baseUrl}/?query={self.search}"
        request = urllib.request.Request(pageURL, headers=self.request_headers)
        contents = json.loads(urllib.request.urlopen(request).read())
        #print(contents)
        title = f"NHS Search Results For {self.search.capitalize()}"
        display = f"<h2><font color='blue'>{title}</font></h2>"
        for result in contents['results']:
            if (result['id'] != '1') and (self.search in f"{result['title']} {result['summary']}"):
                display += f"<h4><a href={result['url']} target='_blank'>{result['title']}</a></h4>"
                display += f"{result['summary'].replace(';', '')}"
                #print(result['id'])
        reply = {'display': display, 'say': title}
        return reply