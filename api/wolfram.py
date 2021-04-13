import requests
import base64

from api import API


class Wolfram(API):
    url = "https://api.wolframalpha.com/v1/simple"

    def search(self, text):
        r = requests.get(Wolfram.url, {
            "i": text,
            "appid": "5824LQ-XJ3UGTQ92J",
        })

        return "<img src='{}'/>".format(r.url)
