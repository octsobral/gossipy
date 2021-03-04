import mongoengine

from src.support.config import Config

client = None

def connect():

    global client

    configs = Config()

    if not client:
        client = mongoengine.connect(
            host=configs.DATABASE_URI,
            connect=False
        )
