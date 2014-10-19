__author__ = 'dominic'

from flask import render_template
from app import app

@app.route('/')
@app.route('/menu')
def index():
    return render_template('menu.html')

@app.route('/restaurants')
def restaurant():
    restaurants = ['Dos Coyotes', 'Mr. Pickles', 'Teabo Cafe', 'Other (Search)']
    links = ["/" + restaurant for restaurant in restaurants[:3]]
    return render_template('restaurants.html', restaurants=restaurants, links=links)

@app.route('/foods')
def foods():
    foods = ['Beef Taco', 'Chicken Burrito', 'Beef Burrito', 'Taco Salad']
    return render_template('foods.html', foods=foods)

@app.route('/stores')
def stores():
    stores = ['Safeway', 'Whole Foods', 'Trader Joe\'s', 'None of These (Search)']
    return render_template('stores.html', stores=stores)

@app.route('/sensitivity')
def sensitivity():
    return render_template('sensitivity.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/nutrients')
def nutrients():
    species = {}
    for f in ('wheatoutput.txt', 'cornoutput.txt', 'soybeanoutput.txt', 'beefoutput.txt', 'riceoutput.txt', 'tomatooutput.txt'):
        file = open(f).readlines()
        nutrients = []
        for line in file:
            line = line.rstrip()
            nutrient = line.split(' ')
            nutrients.append(nutrient)
        name = f.split('output')[0]
        species[name] = nutrients
    return render_template('nutrients.html', species=species)