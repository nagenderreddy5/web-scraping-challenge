#Dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/craigslist_app"
mongo = PyMongo(app)


@app.route("/")
def index():
    mars_db = mongo.db.mars_db.find_one()
    return render_template("index.html", mars_db = 'mars_db')


@app.route("/scrape_mars")
def scrape():
   #mars_data = scrape_mars.scrape()
   mongo.db.collection.update({}, mars_data, upsert=True)
   
   return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)