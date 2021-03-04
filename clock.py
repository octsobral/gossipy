from apscheduler.schedulers.blocking import BlockingScheduler

from src.service.news_api_search_service import NewsAPISearchService
from src.database import database

scheduler = BlockingScheduler()

@scheduler.scheduled_job('cron', day_of_week='mon-mon', hour=00)
def scheduled_search():

    database.connect()
    news_api_search_service = NewsAPISearchService()
    news_api_search_service.search()


    print('This job is run every weekday at 5pm.')

scheduler.start()
