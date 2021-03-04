from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flasgger import Swagger
import json_logging

from src.route.query_controller import QueryController
from src.database import database
from src.support.config import Config


app = Flask('gossipy-microservice')

app.config['SWAGGER'] = {
    'title': "Gossipy Microservice",
    'uiversion': 1,
    'description': "Gossipy Microservice Endpoints"
}

api = Api(app)

swagger = Swagger(app, template_file='src/swagger/template.yml')

CORS(app)


#json_logging.ENABLE_JSON_LOGGING = True
#json_logging.init_flask()
#json_logging.init_request_instrument(app)


def configure_database():
    database.connect()


def configure_api():
    api.add_resource(QueryController, '/query', endpoint='query')


def create_app():
    app.config['ERROR_404_HELP'] = False

    configure_api()

    configure_database()

    return app