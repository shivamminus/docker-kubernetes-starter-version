from pymongo import MongoClient
import pymongo
import json
from flask import Flask, jsonify, request, redirect, render_template
import ast
# instantiate flask object
app = Flask(__name__)


def get_database(database):
    # Provide the mongodb DATABASE NAME
    global client = MongoClient(f"mongodb://root:pass@localhost:27017/{database}")

    # Create the database for our example
    return client

def insert_record(data):
    mydatabase = client["mypydb"]
    mycollection = mydatabase["col1"]
    db_response = mycollection.insert_one(data)
    print(mycollection)# Collection(Database(MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True), 'mypydb'), 'col1')
    return db_response.inserted_id

@app.route("/")
def redirect_page():
    return redirect(location="/fill-details")


@app.route("/fill-details", methods=["GET", "POST"])
def details_page():
    inserted_id = None
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        data1 = request.form.to_dict()
        print(type(data1))
        try:
            inserted_id = insert_record(data1)
            print("RECORD INSERTED!!")
            print(f"ID:\t{inserted_id}")
        except Exception as e:
            print("DATABASE INSERTION ERROR \n\n\n\n ",e)
            
        
    return render_template("index.html")



if __name__ == "__main__":
    rec={
    "title": 'MongoDB and Python',
    "description": 'MongoDB is no SQL database',
    "tags": ['mongodb', 'database', 'NoSQL'],
    "viewers": 104 
    }
    print("CONNECTING TO DB...")
    client = get_database(database="mypydb")
    
    print("DB CONNECTION SUCCESSFUL..")
    print("ATTEMPTING TO RUN SERVER")
    app.run(host="0.0.0.0", debug=True, port=5000)

