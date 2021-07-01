import os
from flask import request
from werkzeug.utils import secure_filename

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


#Code to ruploaded file and store it in a folder


UPLOAD_FOLDER = 'static/uploads/'
app.secret_key = "secret key"

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# Allowed file type extensions

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):

    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@app.route('/uploader', methods = ['POST'])
def upload_file():
    
    file = request.files["file"]


    if file.filename == '':
        print('No image selected for uploading')
    
    if file and allowed_file(file.filename):

        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return "File Uploaded Successfully"
    
    else:
        print('Allowed file types are - png, jpg, jpeg, gif')
        



if __name__ == '__main__':
	app.run()
