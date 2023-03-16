#https://www.analyticsvidhya.com/blog/2022/01/rest-api-with-python-and-flask/

from flask import Flask

from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)

class Helloworld(Resource):

	def __init__(self):

		pass

	def get(self):

		return {

			"Hello": "demo1"

		}

api.add_resource(Helloworld, '/demo1')

if __name__ == '__main__':

	app.run(debug=True)