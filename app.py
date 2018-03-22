from flask import Flask, render_template, request
import requests
import twitter as twitter

app = Flask("MyApp")

@app.route("/home")
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

@app.route("/map",methods=["POST"])
def hello():
  return render_template("project.html", test=data)

app.run(debug=True)
