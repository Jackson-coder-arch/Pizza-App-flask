# from flask import render_template,url_for
# from app import app

# # Views
# @app.route('/')
# def index():

#     '''
#     View root page function that returns the index page and its data
#     '''
#     News = 'Welcome to Pizza World'
#     title = 'PIZZA WORLD'
#     comment ='Where you get the best from Us'
#     happy ='Am always glad to have a slice at Pizza World it always refreshs my day'

#     return render_template('index.html',News= News,comment = comment,title =title)

# @app.route('/pizza')
# def pizza(pizza_id):

#     '''
#     View pizza page function that returns the pizza details page and its data
#     '''

#     return render_template('pizza.html',id = pizza_id)


# @app.route('/order')
# def order():


#     return render_template('order.html')


# @app.route('/login')
# def login():
    

#     return render_template('login.html')



