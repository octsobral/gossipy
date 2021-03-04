from flask_restful import Resource
from flasgger import swag_from
from flask import request
from src.service.query_service import QueryService
from src.support.config import Config
from src.support.utils import str_to_bool


class QueryController(Resource):

    def __init__(self):
        self.query_service = QueryService()
        self.config = Config()

    @swag_from("../swagger/models/query/query-get.yml", endpoint="query")
    def get(self):
        secret = request.headers.get('Authorization', None)

        if secret != self.config.SECRET_KEY:
            raise PermissionError
        else:
            query = self.query_service.get_query()
            return {'query': query}

    @swag_from("../swagger/models/query/query-post.yml", endpoint="query")
    def post(self):
        secret = request.headers.get('Authorization', None)
        query = request.headers.get('Query', None)

        if secret != self.config.SECRET_KEY or query is None:
            raise PermissionError
        else:
            self.query_service.add_query(query)
            return {'msg': 'Query added to queue!'}
