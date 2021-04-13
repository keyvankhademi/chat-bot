from es import ElasticSearch
from nlp.cleaner import Cleaner
from api import Wikipedia

DEFAULT = [
    "Sorry, I don't get what you're saying, can you try again?",
    "I don't quite follow, could you try repeating that in a different way?",
    "I'm not sure if I remember that happening in the Fast & Furious movies...",
    "Are you describing a specific scene? Which characters were involved?",
    "You're interesting...Out of curiosity, what is your favourite Fast & Furious movie?",
    "I don't understand, but I'm interested, what do you think Dom would say if you said that to him?",
    "Well...I'm not sure how to respond. Let's change the topic - What do you think about Tyrese?",
    "I don't know how to follow that up haha. To change the topic - What do you think about Dom?",
    "Intriguing, but let's get back on topic - What do you think about Paul Walker?"
]


class Bot:
    """
    The main bot class
    """

    def __init__(self):
        self.cleaner = Cleaner
        self.es = ElasticSearch
        self.wikipedia = Wikipedia()

    def ask(self, raw_input_string: str):
        """
        :param raw_input_string: Users question as raw string
        :return: Bots response as string
        """

        if raw_input_string.startswith("Wikipedia:"):
            text = raw_input_string.replace("Wikipedia:", "")
            return self.wikipedia.search(text)

        query = self.cleaner.clean(raw_input_string)
        results = self.es.search(query)

        if len(results) > 0:
            return results[0]["_source"]['response']

        from random import randint

        return DEFAULT[randint(0, len(DEFAULT) - 1)]
