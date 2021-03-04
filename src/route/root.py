from flask_restful import Resource


class Root(Resource):

    def get(self):

        message = {'application_name': 'gossipy-microservice',
                   'version': '0.0.1',
                   'author': '9r09u3',
                   'status': 'working',
                   'available_endpoints': '/, /news, /query'}

        return message