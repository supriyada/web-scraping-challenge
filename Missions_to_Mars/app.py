from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

@app.route("/")
def scrape_home():

    mars_data = mongo.db.collection.find_one()
    
    return render_template("index.html", mars_info = mars_data)


@app.route("/scrape")
def mars_scrape():
    mars_info_dict = scrape_mars.scrape()

    mongo.db.collection.update({}, mars_info_dict, upsert=True)

    return redirect ("/")


if (__name__ == "__main__"):
    app.run(debug=True)