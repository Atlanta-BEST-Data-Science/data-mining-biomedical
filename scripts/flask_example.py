#Import statements
from pymongo import MongoClient
from flask import Flask

#Define the app
app = Flask(__name__)

#Create our sequence method
@app.route('/sequences')
def sequences():
    pass

#run the app locally
if __name__ == "__main__":
    app.run()
