from flask import Flask
from flask_restful import Resource, Api, reqparse
from src.backend.classifier import Classifier


app = Flask(__name__)
api = Api(app)

class RalphLaurenFeedPredictions(Resource):
	def get(self):
		# Will eventually make batch predictions
		pass


api.add_resource(RalphLaurenFeedPredictions, '/ralph_lauren_feed_predict')

if __name__ == '__main__':
	app.run(host='0.0.0.0')

