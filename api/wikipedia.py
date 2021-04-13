import requests

from api import API


class Wikipedia(API):
    url = "https://en.wikipedia.org/w/api.php?action=query&list=search&format=json&srsearch={}"

    def search(self, text):
        r = requests.get(Wikipedia.url.format(text))
        data = r.json()["query"]["search"]

        if len(data) == 0:
            return "Sorry, I couldn't find any result."
        return data[0]["snippet"]
