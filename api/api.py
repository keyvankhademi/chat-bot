

class API:
    """
    Abstract API class
    """
    url = None

    def search(self, text):
        raise NotImplementedError()