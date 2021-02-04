from src.service.news_api_search_service import NewsAPISearchService
from service.google_search_service import SearchService


class Gossipy:
    def __init__(self):
        self.news_api_search_service = NewsAPISearchService()

    def run(self):
        search_result = self.news_api_search_service.search()
        for news in search_result:
            print(news)


if __name__ == '__main__':
    GOSSIPY = Gossipy()
    GOSSIPY.run()
