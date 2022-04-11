from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.secret_key = "secret key"
app.config["MONGO_URI"] = "mongodb://mongodbshivam:mypwdformongodb@localhost:27017/mypydb"
mongo = PyMongo(app)