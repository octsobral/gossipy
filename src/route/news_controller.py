from flask_restful import Resource
from flasgger import swag_from
from flask import request
from src.service.query_service import QueryService
from src.service.news_service import NewsService
from src.support.config import Config
from src.support.utils import str_to_bool


class NewsController(Resource):

    def __init__(self):
        self.config = Config()
        self.news_service = NewsService()

    def get(self):
        secret = request.args.get('Authorization', None)
        query = request.args.get('Query', None)

        if secret != self.config.SECRET_KEY:
            raise PermissionError
        else:
            news = self.news_service.get_news()
            return {'news': news}

    def post(self):
        secret = request.headers.get('Authorization', None)
        query = request.headers.get('Query', None)

        if secret != self.config.SECRET_KEY or query is None:
            raise PermissionError
        else:
            self.query_service.add_query(query)
            return {'msg': 'Query added to queue!'}