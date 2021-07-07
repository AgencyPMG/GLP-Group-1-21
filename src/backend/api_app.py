from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
from src.backend.classifier import Classifier

app = Flask(__name__)
CORS(app)
api = Api(app)
clf = Classifier('src/backend/model')

# stub route to make sure requests from the frontend work
@app.route('/predict', methods=['GET'])
def predict(seq):
    return Jsonify(clf.predict(seq))

@app.rout('/test', methods=['GET'])
def test():
    return Jsonify({'Hello': 'World!'})
