from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
#from src.backend.classifier import Classifier

app = Flask(__name__)
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

