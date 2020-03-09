from flask import Flask, render_template #first call flask to gather resources to build the webapp
import datetime

app= Flask(__name__)#run this when app.py is called independently

@app.route("/") #routing to homepage
def index():# run this when routed to '/' root page of the web app
    return render_template("index.html")

@app.route("/<string:name>") #makeing a scalable api, which takes an argument before processing request
def hello(name): #we gather the argument from the api
    return render_template("index.html", name=name.capitalize()) #then we can print it

@app.route("/newyear")
def newyear():
    now=datetime.datetime.now()
    is_new_year=now.month==1 and now.day==1
    return render_template("newyear.html", is_new_year=is_new_year)