from flask import render_template, request, redirect, url_for, abort
from . import main
from ..models import User, Order
from .forms import OrderForm
from flask_login import login_required, current_user
from .. import db

@main.route('/')
# @login_required
def index():
    """
    View root page function that returns the index page and its data
    """
    title = 'PIZZA WORLD'
    # size_order = Order.query.filter_by( = 'size order').all()
    # toppings = Order.query.filter_by(category = 'topping').all()
    # interview_pitch = Pitch.query.filter_by(category = 'Interview Pitch').all()
    # promotion_pitch = Pitch.query.filter_by(category = 'Promotion Pitch').all()

    return render_template('index.html',title = title)

# @main.route('/order', methods =['GET', 'POST'])
# def order():
#     form = OrderForm()

#     title = 'Ordering form'
#     return render_template('order.html', form = form, title = title)


@main.route('/order/new_order', methods = ['GET','POST'])
# @login_required
def new_order():
    order_form = OrderForm() 
    pizza = Order.query.all()
   

    if order_form.validate_on_submit():
        order = Order(email= order_form.email.data, flavor = order_form.flavor.data, crust = order_form.crust.data, size = order_form.size.data, no_of_pizzas = order_form.no_of_pizzas.data, toppings = order_form.toppings.data, delivery = order_form.delivery.data,)

        db.session.add(order)
        db.session.commit() 
        
        # return redirect(url_for('main.index'))
    
    return render_template('order.html', order_form = order_form, pizza = pizza)   


