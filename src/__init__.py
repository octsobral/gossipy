from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flasgger import Swagger
import json_logging

from src.route.query_controller import QueryController
from src.route.news_controller import NewsController
from src.route.root import Root
from src.database import database
from src.support.config import Config


app = Flask('gossipy-microservice')

app.config['SWAGGER'] = {
    'title': "Gossipy Microservice",
    'description': "Gossipy Microservice Endpoints"
}

api = Api(app)

swagger = Swagger(app, template_file="src/swagger/template.yml")

CORS(app)


#json_logging.ENABLE_JSON_LOGGING = True
#json_logging.init_flask()
#json_logging.init_request_instrument(app)


def configure_database():
    database.connect()


def configure_api():
    api.add_resource(QueryController, '/query', endpoint='query')
    api.add_resource(Root, '/', endpoint='root')
    api.add_resource(NewsController, '/news', endpoint='news')

def create_app():
    app.config.from_object(Config)
    app.config['ERROR_404_HELP'] = False

    configure_api()

    configure_database()

    return app