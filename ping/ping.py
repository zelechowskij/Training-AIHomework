from flask import Flask
from flask_restplus import Api, Resource, reqparse
import requests
import logging

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('url', required=True, help="Url of the page to ping", location='json')

@api.route('/api/v1/ping')
class Ping(Resource):
    @api.expect(parser)
    def post(self):
        url = parser.parse_args().get('url')
        try:
            response_json = requests.get(url).json()
        except Exception as e:
            logging.error(e)
        return response_json
        

@api.route('/health')
class Health(Resource): 
    def get(self):
        return {'status': 'healthy'}

if __name__ == '__main__':
    app.run(debug=True)