import os

from flask import Flask, jsonify
from flask_restplus import Api, Resource
from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(app, version='1.0', doc='/apidocs/', title='Agile Tutorial', description='Python API')
my_list = list()

ns = api.namespace('basic', description='List manipulation')


@api.route('/basic/print')
@api.doc(description='Print current list.')
class PrintList(Resource):
    def get(self):
        return jsonify(list=my_list)


port = os.getenv('PORT', '5000')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port))
