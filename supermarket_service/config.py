from os import environ

from dotenv import load_dotenv

load_dotenv()


class GlobalConfig:
    def __init__(self):
        pass

    # Database URL:
    database_url: str = environ['DATABASE_URL']


settings = GlobalConfig()