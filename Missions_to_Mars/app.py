from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

#Connecting to Mongo DB and creating a database mars_app
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

#Landing/home page
@app.route("/")
def scrape_home():

    mars_data = mongo.db.collection.find_one()
    
    return render_template("index.html", mars_info = mars_data)

#Invokes the function to scrape the html pages for new data
@app.route("/scrape")
def mars_scrape():
    mars_info_dict = scrape_mars.scrape()

    #Insert/updates one record in the mongodb
    mongo.db.collection.replace_one({}, mars_info_dict, True)

    return redirect ("/")


if (__name__ == "__main__"):
    app.run(debug=True)