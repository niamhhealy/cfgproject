from flask import Flask, render_template, request
import requests

app = Flask("MyApp")

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

@app.route("/")
def hello():
  return render_template("project.html", test=data)



app.run(debug=True)
