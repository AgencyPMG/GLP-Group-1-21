import flask as Flask
from flask_restful import Resource, Api, reqparse
from src.backend.classifier import Classifier


app = Flask(__name__)
api = API(app)

class RalphLaurenFeedPredicitons(Resource):
	def get(self):
		# Will eventually make batch predictions
		pass


api.add_resource(RalphLaurenFeedPredictions, 'ralph_lauren_feed_predict')

if __name__ == '__main__':
	app.run()

