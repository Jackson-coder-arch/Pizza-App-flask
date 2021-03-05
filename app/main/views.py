from flask import render_template, request, redirect, url_for, abort
from . import main
from ..models import User, Order
from .forms import OrderForm
from flask_login import login_required, current_user
from .. import db

@main.route('/')
@login_required
def index():
    """
    View root page function that returns the index page and its data
    """
    title = 'Orders'
    size_order = Order.query.filter_by(category = 'size order').all()
    toppings = Order.query.filter_by(category = 'topping').all()
    interview_pitch = Pitch.query.filter_by(category = 'Interview Pitch').all()
    promotion_pitch = Pitch.query.filter_by(category = 'Promotion Pitch').all()

    return render_template('index.html', title = title)

@main.route('/order', methods =['GET', 'POST'])
def order():
    form = OrderForm()

    title = 'Ordering form'
    return render_template('order.html', form =  form, title = title)


@main.route('/order/new_order', methods = ['GET','POST'])
@login_required
def new_order():
    order_form = OrderForm()    

    if order_form.validate_on_submit():
        order = Order(email= order_form.title.data, flavor = order_form.category.data, crust = order_form.order_content.data, size= order_form.category.data, no_of_pizza = order_form.category.data, toppings = order_form.category.data, delivery = order_form.category.data,)

        db.session.add(order)
        db.session.commit() 
        
        return redirect(url_for('main.index'))
    
    return render_template('order.html', order_form = order_form)   


