import requests
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from urllib.parse import quote_plus

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