import tweepy
from SRC.Constants import CONSUMER_KEY, CONSUMER_KEY_SECRET, TOKEN_ACCESS, TOKEN_ACCESS_SECRET, WOE_ID_BRAZIL
from    SRC.conection import conexaoMongoDB


colection_tweets = conexaoMongoDB()

def _buscar_trends(woe_id, api):

  trends_twiter = api.get_place_trends(woe_id)
  return [trend for trend in trends_twiter]


def buscar_trends():
   trends = colection_tweets.find({})
   return list(trends)


def save_trends():
    auth = tweepy.OAuthHandler(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_KEY_SECRET)
    auth.set_access_token(TOKEN_ACCESS, TOKEN_ACCESS_SECRET)

    api = tweepy.API(auth)

    trends = _buscar_trends(WOE_ID_BRAZIL, api)
    colection_tweets.insert_many(trends)
  