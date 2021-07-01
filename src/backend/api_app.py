
import pathlib
import os
from flask import Flask, render_template, request, redirect, url_for, abort,flash
from werkzeug.utils import secure_filename


app = Flask(__name__)



UPLOAD_FOLDER = 'static/uploads/'
app.secret_key = "secret key"

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/uploader', methods = ['POST'])
def upload_file():
    file = request.files["file"]
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return "File Successfully Uploaded"

