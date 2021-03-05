from apscheduler.schedulers.blocking import BlockingScheduler

from src.service.news_service import NewsService
from src.database import database

scheduler = BlockingScheduler()

@scheduler.scheduled_job('cron', day_of_week='mon-mon', hour=00)
def scheduled_search():

    database.connect()
    news_service = NewsService()
    news_service.add_news()

scheduler.start()
