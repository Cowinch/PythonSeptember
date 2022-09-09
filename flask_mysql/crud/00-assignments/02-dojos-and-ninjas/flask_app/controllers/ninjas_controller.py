from flask_app import app
from flask import render_template,request, session, redirect
from flask_app.models.dojo_model import Dojo
from flask_app.models.ninja_model import Ninja

@app.route('/dojos/ninja')
def new_ninja():
    all_dojos=Dojo.get_all()
    return render_template('ninja_create.html', all_dojos=all_dojos)

@app.route('/dojos/ninja/process', methods=['POST'])
def process_ninja():
    Ninja.create(request.form)
    id=request.form['dojo_id']
    return redirect(f'/dojos/{id}')