from email.policy import HTTP
from flask import Flask, jsonify, request, redirect
from flask.helpers import url_for
from flask_pymongo import PyMongo
from pymongo import MongoClient
import json
import ast
# from flask_cors import CORS, cross_origin

app = Flask(__name__)
# app.config["MONGO_URI"] = MongoClient("mongodb://root:pass@localhost:27017/mypydb")
# cors = CORS(app)
app.config['MONGO_URI'] = "mongodb://mongodbshivam:mypwdformongodb@mongodb:27017/mypydb"
# app.config['CORS_Headers'] = 'Content-Type'
mongo = PyMongo(app)
# print(mongo.db.col1.find())

@app.route('/', methods = ['GET'])
def retrieveAll():
    print("reached get method: /get")
    data = {}
    a=0
    for i in mongo.db.col1.find().limit(100):
        data[a] = [str(item) for item in i.items()]
        a=a+1
    
    return {"data":data}, 200


@app.route('/<name>', methods = ['GET'])
def retrieveFromName(name):
    currentCollection = mongo.db.col1
    data = currentCollection.find_one({"city":name})
    data["_id"] = data["_id"] 
    print(data["_id"])
    return {"result":str(data).replace(r"\n","").replace(r'"','')}, 200
    
	

@app.route('/postData', methods = ['POST'])
def postData():
    currentCollection = mongo.db.col1
    data = request.data.decode()
    data = ast.literal_eval(data)
    print(type(data))
    inserted_id = currentCollection.insert_one(data)
    return {"objectID":str(inserted_id)}

@app.route('/deleteData/<name>', methods = ['DELETE'])
def deleteData(name):
    currentCollection = mongo.db.col1
    currentCollection.delete_one({'city' : name})
    return redirect(url_for('retrieveAll'))

@app.route('/update/<name>', methods = ['PUT'])
def updateData(name):
    currentCollection = mongo.db.col1
    updatedName = request.json['name']
    currentCollection.update_one({'name':name}, {"$set" : {'name' : updatedName}})
    return redirect(url_for('retrieveAll'))

if __name__ == '__main__':
    app.run(debug = True, host="0.0.0.0",port=5000)