from src.support.config import Config
from src.database.model.query import Query

class QueryService:

    def __init__(self):
        self.config = Config()

    def get_query(self):

        queries = []

        for query in Query.objects:
            queries.append(query.name)

        return queries

    def add_query(self, query):

        standard_query = self._standardize_query(query)
        new_query = Query()
        new_query.name = standard_query
        new_query.save()

        return

    def delete_query(self, query):

        available_queries = self.get_query()

        standard_query = self._standardize_query(query)

        if standard_query in available_queries:
            Query.objects(name=query).delete()

        return

    def _standardize_query(self, query):

        standard_query = query.replace(" ", "_").lower()

        return standard_query


