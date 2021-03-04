from os import getenv

from src.support import load_config
from src.support.utils import str_to_bool


class Config:

    def __init__(self, load_config_from_file=True):
        if load_config_from_file:
            load_config.load()

        self.NAME = 'GOSSIPY'
        self.VERSION = '0.0.1'
        self.HOST = getenv('HOST')
        self.PORT = getenv('PORT')
        self.DEBUG = str_to_bool(getenv('DEBUG'))

        self.NEWS_API_KEY = getenv('NEWS_API_KEY')
        self.DATABASE_URI = getenv('DATABASE_URI')
        self.SECRET_KEY = getenv('SECRET_KEY')

        #self.SEARCH_TERMS = list(getenv("SEARCH_TERMS").split(","))
        #self.SAVE_OPTION = getenv('SAVE_OPTION') if getenv('SAVE_OPTION') else ""
