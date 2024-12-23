from flask import Flask, request
import datetime
import requests
from pymongo import MongoClient
from views import views
from pymongo.server_api import ServerApi
from urllib.parse import quote_plus

app = Flask(__name__)
app.register_blueprint(views,url_prefix="/")

if __name__ == '__main__':
    app.run(debug=True)
    
