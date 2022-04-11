from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage

import os

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = r'./testimages'
app.config['MAX_CONTENT_PATH'] = 128


@app.route("/")
def hello():
    return render_template("main.html")


@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return 'file uploaded successfully'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5001)