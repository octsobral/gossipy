from flask_restful import Resource
from flasgger import swag_from
from flask import request
from src.service.query_service import QueryService
from src.support.config import Config


class QueryController(Resource):

    def __init__(self):
        self.query_service = QueryService()
        self.config = Config()

    @swag_from("../swagger/models/query/query-get.yml", endpoint="query")
    def get(self):
        secret = request.args.get('Authorization', None)

        if secret != self.config.SECRET_KEY:
            raise PermissionError
        else:
            query = self.query_service.get_query()
            return {'query': query}

    @swag_from("../swagger/models/query/query-post.yml", endpoint="query")
    def post(self):
        secret = request.args.get('Authorization', None)
        query = request.args.get('Query', None)

        if secret != self.config.SECRET_KEY or query is None:
            raise PermissionError
        else:
            self.query_service.add_query(query)
            return {'msg': 'Query added to queue!'}

    @swag_from("../swagger/models/query/query-delete.yml", endpoint="query")
    def delete(self):
        secret = request.args.get('Authorization', None)
        query = request.args.get('Query', None)

        if secret != self.config.SECRET_KEY or query is None:
            raise PermissionError
        else:
            self.query_service.delete_query(query)
            return {'msg': 'Query deleted from queue!'}
