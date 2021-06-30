#import flask as Flask
#from flask_restful import Resource, Api, reqparse
#from src.backend.classifier import Classifier


import pathlib
import os
from flask import Flask, render_template, request, redirect, url_for, abort,flash
from werkzeug.utils import secure_filename


#app = Flask(__name__)
#api = API(app)

"""class RalphLaurenFeedPredicitons(Resource):
	def get(self):
		# Will eventually make batch predictions
		pass


#api.add_resource(RalphLaurenFeedPredictions, 'ralph_lauren_feed_predict')

"""





UPLOAD_FOLDER = '/Users/mumtazbano/GLP-Group-1-21/UploadsFolder'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and ALLOWED_EXTENSIONS(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))



if __name__ == '__main__':
	app.run()

