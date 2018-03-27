# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
import requests

import tweepy

app = Flask(__name__)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/")
def access():
    return render_template("submit.html")

#Example data
data = [
  {
    "lat": 53.800755,
    "lng": -1.549077 ,
    "html": "Leeds"
  },
  {
    "lat": 51.507351,
    "lng": -0.127758,
    "html": "London"
  },
   {
    "lat": 54.978252,
    "lng": -1.617780,
    "html": "Newcastle"
  }
]

#Function to extract location of tweets
def tweet_finder(search):
    # Set auth
    auth = tweepy.OAuthHandler("NhwEslehY264mPa0owS6i4BZU","zzuVEQsOSOovoHXZ965Me4HKlt0VMiH87ruztaTo71cPH9VIYK")
    auth.set_access_token("2282751926-Avzs0JEIg0WIePxJO7y0meUYlQj2gR8uMfrnF6q","ePKPPikAAChk6W5dNnQPLTUOcOxNBzGHknI9DpO9aQXig")

    # Set twitter API
    twitter_api = tweepy.API(auth)

    # Search twitter
    tweets = twitter_api.search  (q = "#{}".format(search),rpp=100, count=200, geocode = "51.5,-0.1,60km")

    #Pull off the location and tweet text for tweets that have a location listed
    d = list()
    t = list()
    for tweet in tweets:
      if tweet.place!= None:
        d.append(tweet.place.bounding_box.coordinates[0][0])
        t.append(tweet.text)

    #Modify the data so it is in the right format to be used in the google maps api
    my_list=list()
    for x in range(0, len(d)):
      my_dict={}
      my_dict["lng"]=d[x][0]
      my_dict["lat"]=d[x][1]
      my_dict["html"]=t[x]
      my_list.append(my_dict)

    return(my_list)



@app.route("/map", methods=["POST"])
def hello():
  form_data = request.form
  search =form_data["text"]
  return render_template("project.html", test=tweet_finder(search))

if __name__ == '__main__':
   app.run(debug=True)
