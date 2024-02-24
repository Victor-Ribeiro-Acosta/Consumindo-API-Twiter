
from pymongo import MongoClient

class coneXaoMongoDB():
    def __init__(self):

    cliente = MongoClient("chave de autenticação")
    db = cliente.Trends_Twiter_Brazil
    colection_tweets = db.tweets
    return colection_tweets