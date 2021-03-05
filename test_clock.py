from src.service.news_service import NewsService
from src.database import database

def test_scheduled_search():

    database.connect()
    news_service = NewsService()
    news_service.add_news()

test_scheduled_search()