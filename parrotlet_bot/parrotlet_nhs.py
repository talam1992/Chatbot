__author__ = "Timothy Lam"

# This script is using Python3
import urllib.request
import urllib.parse
import config
import json


def selector(message):
    if message[:len('nhs review on')] == 'nhs review on':
        msg = message[len('nhs review on')+1:].strip()
        return HealthData(msg).display_all()
    else:
        return


class HealthData:
    def __init__(self, search):
        request_headers = {
            "subscription-key": config.nhs_Key,
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
        }
        pageURL = f"https://api.nhs.uk/conditions/{search}"
        try:
            request = urllib.request.Request(pageURL, headers=request_headers)
            self.search = search
            self.contents = json.loads(urllib.request.urlopen(request).read())
            self.check = 1
        except Exception:
            self.search = search
            self.check = 0

    def display_all(self):
        if self.check == 1:
            reply = f"<h1><font color='blue'>NHS REVIEW ON {self.search.upper()}</font></h1>"
            for data_dict in self.contents["hasPart"]:
                reply += f"<h3>{data_dict['name'].capitalize().replace('_', ' ')}</h3>"
                text = data_dict["text"]
                if text == "":
                    text = data_dict["description"]
                reply += f"{text.replace(';', '').replace('api', 'www')}"
                reply += f'<a href="{data_dict["url"].replace("api", "www")}" target="_blank">Read More</a>'
            reply_ = {'display': reply,
                      'say': f'Find displayed a review on {self.search}. this information is provided by NHS'}
            return reply_
        else:
            return f"cannot find result for {self.search}"