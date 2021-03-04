import datetime
import requests

from src.database.model.news import News
from src.database.model.query import Query
from src.support.config import Config

SEARCH_ENDPOINT = 'http://newsapi.org/v2/everything?'

QUERY_DATE_RANGE = ['day', 'week', 'month', 'year']


class NewsAPISearchService:

    def __init__(self):
        self.config = Config()

    def search(self, query, query_date_range):

        session = requests.Session()

        urls = self._create_search_url(self)

        response = []

        for query, url in urls:
            request = session.get(url)
            json_request = request.json()
            for article in json_request['articles']:
                result = {}
                result['query'] = query
                result['title'] = article['title']
                result['source'] = article['source']['name']
                result['url'] = article['url']
                result['published_at'] = article['publishedAt']
                result['hash'] = hash(result['url'])
                response.append(result)

        return response

    @staticmethod
    def _create_search_url(self):

        today = datetime.date.today()
        yesterday = today - datetime.timedelta(days=1)

        list_of_search_items = []

        for query in self.config.SEARCH_TERMS:
            standard_query = query.replace(" ", "-")
            url = SEARCH_ENDPOINT + 'q=' + query + '&from=' + str(yesterday) + '&apiKey=' + self.config.NEWS_API_KEY
            list_of_search_items.append((standard_query, url))

        return list_of_search_items


