from flask import Flask, request
import datetime
import requests
from pymongo import MongoClient
from views import views
from pymongo.server_api import ServerApi
from urllib.parse import quote_plus

app = Flask(__name__)
app.register_blueprint(views,url_prefix="/")
def getClient(userName,password):
    userName=quote_plus(userName)
    password = quote_plus(password)
    uri = f'mongodb+srv://{userName}:{password}@cluster0.zz9ubvy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
    client = MongoClient(uri, server_api=ServerApi('1'))
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return MongoClient(f'mongodb+srv://{userName}:{password}@cluster0.zz9ubvy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
    except Exception as e:
        print("dasdas")
        return None

def getCollection(client, dataBaseName='RACPIR', collectionName='IP_Metadata'):
    return client[dataBaseName][collectionName] if client!=None else None

def insertDocuments(collection, documents):
    if collection==None:
        print("No collection where to perform an insertion")
    else:
        collection.insert_many(documents)

def getIPData(IPJson):
    IP = IPJson['ip']
    city = IPJson['city']
    region = IPJson['region']
    country = IPJson['country']
    postal = IPJson['postal']
    loc = IPJson['loc']
    return IP,city,region,country, postal, loc

@app.route('/')
def main():
    approximately_house = ""
    collection = getCollection(getClient("alanaxelcastroresendiz","Alan7776"),'RACPIR','IP_Metadata')

    ip_address = ""
    more = ""
    forwarded_for = request.headers.get('X-Forwarded-For')
    forwarded_for="189.217.111.179"
    if forwarded_for:
        for ip in forwarded_for.split(','):
            ip_address+=ip+" , "
            more += "1"
            approximately_house = requests.get(f'https://ipinfo.io/{ip}?token=9c06a926e98489').json()
            IP,city,region,country, postal, loc = getIPData(approximately_house)
            approximately_house = f'\n IP:{IP}\nCity:{city}\nRegion:{region}\nCountry:{country}\nPostal Code:{postal}\nloc:{loc}'
            insertDocuments(collection,[{"IP":IP,"loc": loc, "country": country, "region": region, "city": city, "postal":postal}])
    return f'{approximately_house}'

if __name__ == '__main__':
    app.run(debug=True)
    
