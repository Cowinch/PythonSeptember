from flask_app import app
from flask import render_template, redirect, request, flash, session
from flask_app.models.recipe_model import Recipe
from flask_app.models.user_model import User
from flask_app import DATABASE
from flask_bcrypt import Bcrypt
bcrypt=Bcrypt(app)

# ADD RECIPES, EDIT RECIPES, and DISPLAY RECIPE routes are all in the recipes_controller file.

#this is a reroute to home page
@app.route('/')
def index():
    return redirect('/login')

#this is just so when we're logging in the URL reflects the stage we're at
@app.route('/login')
def home():
    return render_template('index.html')

#this is the route for NEW USERS
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

#this is the login route for ACTIVE USERS
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

#this is the dashboard
@app.route('/welcome')
def welcome():
    if 'user_id' not in session:
        return redirect('/')
    all_recipes=Recipe.get_all()
    user_data={
        'id':session['user_id']
    }
    logged_user=User.get_by_id(user_data)
    return render_template('dashboard.html', logged_user=logged_user, all_recipes=all_recipes)

#this is the logout route
@app.route('/users/logout')
def logout():
    del session['user_id']
    return redirect('/')