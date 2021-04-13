import requests


class Wikipedia:
    url = "https://en.wikipedia.org/w/api.php?action=query&list=search&format=json&srsearch={}"

    def search(self, text):
        r = requests.get(Wikipedia.url.format(text))
        data = r.json()["query"]["search"]

        if len(data) == 0:
            return "Sorry, I couldn't find any result."
        return data[0]["snippet"]
