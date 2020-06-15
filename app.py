import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'data_centric'
app.config["MONGO_URI"] = 'MONGO_URI'


mongo = PyMongo(app)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/recipes')
def recipes():
    return render_template('recipes.html', recipes=mongo.db.recipes.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT')), debug=True)
