from flask_app import app
from flask import render_template, redirect, request, flash, session
from flask_app.models.item_model import Item
from flask_app.models.user_model import User
from flask_app.models.order_model import Order
from flask_app import DATABASE
from flask_bcrypt import Bcrypt
bcrypt=Bcrypt(app)

#this is a reroute to home page
@app.route('/')
def index():
    return redirect('/login')

#this is just so when we're logging in the URL reflects the stage we're at
@app.route('/login')
def home():
    return render_template('index.html')

#process form route for NEW USERS
@app.route('/users/register', methods=['POST'])
def register():
    if not User.validate(request.form):
        return redirect('/')
    hashed_pass=bcrypt.generate_password_hash(request.form['password'])
    data={
        **request.form,
        'password': hashed_pass
    }
    id=User.create(data)
    session['user_id']=id
    return redirect('/welcome')

#process form route for ACTIVE USERS
@app.route('/users/login', methods=['POST'])
def login():
    data={'email': request.form['email']}
    user_in_db=User.get_by_email(data)
    if not user_in_db:
        flash('Invalid login info','log')
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash('Invalid login info','log')
        return redirect('/')
    session['user_id']=user_in_db.id
    return redirect('/welcome')

#DASHBOARD
@app.route('/welcome')
def welcome():
    if 'user_id' not in session:
        return redirect('/')
    all_orders=Order.get_all()
    user_data={
        'id':session['user_id']
    }
    logged_user=User.get_by_id(user_data)
    return render_template('dashboard.html', logged_user=logged_user, all_orders=all_orders)

#process route to LOG OUT
@app.route('/users/logout')
def logout():
    del session['user_id']
    return redirect('/')