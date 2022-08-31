import tweepy
import dotenv as dotenv
import os as os
import time

dotenv.load_dotenv()

TW_API_KEY = os.environ["TWITTER_API_KEY"]
TW_API_SECRET = os.environ["TWITTER_SECRET_KEY"]
TW_ACCESS_TOKEN = os.environ["TWITTER_ACCESS_TOKEN"]
TW_ACCESS_SECRET = os.environ["TWITTER_ACCESS_SECRET"]

auth = tweepy.OAuthHandler(TW_API_KEY, TW_API_SECRET)
auth.set_access_token(TW_ACCESS_TOKEN, TW_ACCESS_SECRET)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

respuesta = "Acabas de nombrar la palabra M3t4m4sk, muchos bot van a contestarte con el objetivo de estafarte. Las cuentas oficiales son @metamask y @metamasksupport"
TIME_DELAY = 30

