#Import statements
import tweepy
import json
from config import consumer_key, consumer_secret, access_token, access_token_secret

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

#Code Execution
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

sentiment_dict = {

}

for post in api.search("Sochi Olympics"):
    data = json.dumps(post._json, sort_keys=True, indent=4, separators=(',', ': '))
    data = json.loads(data)
    print(data['text'])
