from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS

app = Flask(__name__, static_url_path='', static_folder='client-side/build')
CORS(app)
api = Api(app)

# stub route to make sure requests from the frontend work
@app.route('/predict', methods =['POST'])
def predict():
    
    itemDescription = request.form.get('description')
    gender = request.form.get('gender')
    age = request.form.get('age')
    size = request.form.get('size')
    image_url = request.form.get('image-url')

    response = jsonify({'description': itemDescription,'gender':gender,'age':age,'size':size,'image-url':image_url})
    return response

class RalphLaurenFeedPredictions(Resource):
	def get(self):
		# Will eventually make batch predictions
		pass

api.add_resource(RalphLaurenFeedPredictions, '/ralph_lauren_feed_predict')

if __name__ == '__main__':
	app.run()

