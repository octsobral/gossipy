from src.support.config import Config
from src.database.model.news import News
from src.service.search_service.news_api_search_service import NewsAPISearchService

QUERY_DATE_RANGE = ['day', 'week', 'month', 'year']


class NewsService:

    def __init__(self):
        self.config = Config()
        self.search_service = NewsAPISearchService()

    def get_news(self):

        news = []

        for new in News.objects:
            article = []
            article.append(new.title)
            article.append(new.published_at)
            article.append(new.url)
            news.append(article)

        return news

    def add_news(self):

        news = self.search_service.search()

        for article in news:
            if len(News.objects(url=article['url'])) is not 0:
                continue
            else:
                news = News()
                news.query = article['query']
                news.title = article['title']
                news.source = article['source']
                news.url = article['url']
                news.published_at = article['published_at']
                news.hash = article['hash']
                news.save()
        return

