from flask_app import app
from flask import render_template, redirect, request, flash, session
from flask_app.models.item_model import Item
from flask_app.models.user_model import User
from flask_app.models.order_model import Order
from flask_app import DATABASE
from flask_bcrypt import Bcrypt
bcrypt=Bcrypt(app)

#route for NEW ORDER
@app.route('/orders/new')
def new_orders_form():
    if 'user_id' not in session:
        return redirect('/')
    logged_user = User.get_by_id({'id': session['user_id']})
    return render_template('orders_new.html', logged_user=logged_user)

#process form for NEW ORDER
@app.route('/orders/create')
def process_order():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'user_id':  session['user_id']
    }
    Order.create(data)
    return redirect('/welcome')
    # return redirect(f'/recipes/{id}') for later use

@app.route('/orders/<int:id>/delete')
def del_order(id):
    if 'user_id' not in session:
        return redirect('/')
    order = Order.get_by_id({'id': id})
    if not int(session['user_id']) == order.user_id:
        flash("Whoa there, that's not yours, hands off!")
        return redirect('/welcome')
    Order.delete({'id': id})
    return redirect('/welcome')
