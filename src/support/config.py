from os import getenv

from src.support import load_config


class Config:

    def __init__(self, load_config_from_file=True):
        if load_config_from_file:
            load_config.load()

        self.NAME = 'GOSSIPY'
        self.VERSION = '0.0.1'

        self.NEWS_API_KEY = getenv('NEWS_API_KEY')
        self.SEARCH_TERMS = list(getenv("SEARCH_TERMS").split(","))
        self.FREQUENCY = getenv('FREQUENCY') if getenv('OSTRACIZE_LIST') else ""
        self.OSTRACIZE_LIST = getenv('OSTRACIZE_LIST') if getenv('OSTRACIZE_LIST') else ""
        self.RESULT = int(getenv('RESULT')) if getenv('RESULT') else ""
