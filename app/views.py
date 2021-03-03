from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    News = 'Welcome to Pizza World'
    comment ='Where you get the best from Us'
    return render_template('index.html',News= News,comment = comment)

@app.route('/pizza/<int:pizza_id>')
def pizza(pizza_id):

    '''
    View pizza page function that returns the pizza details page and its data
    '''
    return render_template('pizza.html',id = pizza_id)
