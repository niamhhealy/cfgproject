import tweepy
import requests

auth = tweepy.OAuthHandler("NhwEslehY264mPa0owS6i4BZU","zzuVEQsOSOovoHXZ965Me4HKlt0VMiH87ruztaTo71cPH9VIYK")
auth.set_access_token("2282751926-Avzs0JEIg0WIePxJO7y0meUYlQj2gR8uMfrnF6q","ePKPPikAAChk6W5dNnQPLTUOcOxNBzGHknI9DpO9aQXig")

twitter_api = tweepy.API(auth, parser = tweepy.parsers.JSONParser())



lat = 51.5
lon = 0

cfg_tweets = twitter_api.search  (geocode(lat = lat, lon = lon), count = 5)

print cfg_tweets['username']

# for tweet in cfg_tweets:

#    print tweet.user.name
