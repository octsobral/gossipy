from flask_restful import Resource
from flasgger import swag_from


class Root(Resource):

    @swag_from("../swagger/models/root/root.yml", endpoint="root")
    def get(self):

        message = {'application_name': 'gossipy-microservice',
                   'version': '0.0.1',
                   'author': '9r09u3',
                   'status': 'working',
                   'available_endpoints': '/, /news, /query'}

        return message