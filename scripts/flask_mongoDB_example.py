#Import statements
from pymongo import MongoClient
from flask import Flask
from flask import jsonify

#Connect to the database
mongo_uri = 'mongodb://test_user:Emory18!@ds023455.mlab.com:23455/heroku_kn66qwrg'
client = MongoClient(mongo_uri)
database = client["heroku_kn66qwrg"]

#Define the app
app = Flask(__name__)

#Create our sequence method
@app.route('/sequences')
def sequences():
    data = []
    #Get all of the records in your collection
    your_name = "Doug"
    results = database[your_name + "_sequences"].find({})
    #Print out the information
    for result in results:
        del result["_id"]
        data.append(result)
    return jsonify(data), 200

#run the app locally
if __name__ == "__main__":
    app.run()
