from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
from src.backend.classifier import Classifier

app = Flask(__name__)
CORS(app)
api = Api(app)

# stub route to make sure requests from the frontend work
@app.route('/predict', methods =['POST'])
def predict():
    response = jsonify({'some': 'data'})

    itemDescription = request.form.get('description')
    imageData = request.form.get('imageData')
    return response

class RalphLaurenFeedPredictions(Resource):
	def get(self):
		# Will eventually make batch predictions
		pass

api.add_resource(RalphLaurenFeedPredictions, '/ralph_lauren_feed_predict')

if __name__ == '__main__':
	app.run()

