import tweepy
import requests

auth = tweepy.OAuthHandler("NhwEslehY264mPa0owS6i4BZU","zzuVEQsOSOovoHXZ965Me4HKlt0VMiH87ruztaTo71cPH9VIYK")
auth.set_access_token("2282751926-Avzs0JEIg0WIePxJO7y0meUYlQj2gR8uMfrnF6q","ePKPPikAAChk6W5dNnQPLTUOcOxNBzGHknI9DpO9aQXig")

twitter_api = tweepy.API(auth)

cfg_tweets = twitter_api.search ( q  = "CodeFirstGirls")

for tweet in cfg_tweets:

    print tweet.user.name
