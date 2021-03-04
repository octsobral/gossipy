from flask_restful import Resource


class Root(Resource):

    def get(self):

        message = {'aplication_name': 'gossipy-microservice',
                   'author': '9r09u3',
                   'status': 'working',
                   'available_endpoints': '/, /news, /query'}

        return message