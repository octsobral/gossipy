import datetime
import requests

from src.service.query_service import QueryService
from src.support.config import Config

SEARCH_ENDPOINT = 'http://newsapi.org/v2/everything?'


class NewsAPISearchService:

    def __init__(self):
        self.config = Config()
        self.query_service = QueryService()

    def search(self):

        session = requests.Session()

        queries = self.query_service.get_query()

        urls = self._create_search_url(queries)

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
                result['hash'] = str(hash(result['url']))
                response.append(result)

        return response

    def _create_search_url(self, queries):

        today = datetime.date.today()
        yesterday = today - datetime.timedelta(days=1)

        list_of_search_items = []

        for query in queries:
            url = SEARCH_ENDPOINT + 'q=' + query + '&from=' + str(yesterday) + '&apiKey=' + self.config.NEWS_API_KEY
            list_of_search_items.append((query, url))

        return list_of_search_items


