from flask import render_template,redirect,request
from flask_app import app
from flask_app.models.dojo_model import Dojo
from flask_app.models.ninja_model import Ninja

#reroute blank to home page
@app.route('/')
def index():
    return redirect('/dojos')

#display home page
@app.route('/dojos')
def homepage():
    all_dojos=Dojo.get_all()
    print(all_dojos)
    return render_template('index.html', all_dojos=all_dojos)

#process new dojo, redirect to homepage
@app.route('/dojos/new', methods=['POST'])
def create_new_dojo():
    Dojo.create(request.form)
    return redirect('/dojos')

#display Dojo and Ninjas of that Dojo
@app.route('/dojos/<int:id>')
def display_dojo(id):
    one_dojo=Dojo.get_one({'id':id})
    return render_template('dojo_show.html', one_dojo=one_dojo)



@app.errorhandler(404)
def page_not_found(e): #as far as I can tell this parameter literally exists just to stop a positional argument error.
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404