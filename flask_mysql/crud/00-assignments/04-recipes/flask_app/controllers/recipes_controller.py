from flask_app import app
from flask import render_template, redirect, request, flash, session
from flask_app.models.user_model import User
from flask_app.models.recipe_model import Recipe
from flask_app import DATABASE

#route for NEW RECIPE
@app.route('/recipes/new')
def new_recipe_form():
    if 'user_id' not in session:
        return redirect('/')
    logged_user = User.get_by_id({'id': session['user_id']})
    return render_template('recipes_new.html', logged_user=logged_user)

#process form for NEW RECIPE
@app.route('/recipes/create', methods=['POST'])
def process_recipe():
    if 'user_id' not in session:
        return redirect('/')
    if not Recipe.validator(request.form):
        return redirect('/recipes/new')
    data = {
        **request.form,
        'user_id':  session['user_id']
    }
    id=Recipe.create(data)
    return redirect('/welcome')
    # return redirect(f'/recipes/{id}') for later use

#process route for deleting recipe
@app.route('/recipes/<int:id>/delete')
def del_party(id):
    if 'user_id' not in session:
        return redirect('/')
    recipe = Recipe.get_by_id({'id': id})
    if not int(session['user_id']) == recipe.user_id:
        flash("Whoa there, that's not yours, hands off!")
        return redirect('/welcome')
    Recipe.delete({'id': id})
    return redirect('/welcome')

#route for EDIT RECIPE
@app.route('/recipes/<int:id>/edit')
def edit_recipe_form(id):
    if 'user_id' not in session:
        return redirect('/')
    recipe = Recipe.get_by_id({'id': id})
    if not int(session['user_id']) == recipe.user_id:
        flash("Whoa there, that's not yours, hands off!")
        return redirect('/welcome')
    recipe = Recipe.get_by_id({'id': id})
    return render_template('recipes_edit.html', recipe=recipe)

#process form for EDIT RECIPE
@app.route('/recipes/<int:id>/update', methods=['POST'])
def update_recipe(id):
    if 'user_id' not in session:
        return redirect('/')
    recipe = Recipe.get_by_id({'id': id})
    if not int(session['user_id']) == recipe.user_id:
        flash("Whoa there, that's not yours, hands off!")
        return redirect('/welcome')
    if not Recipe.validator(request.form):
        return redirect(f'/recipes/{id}/edit')
    data = {
        **request.form,
        'id': id
    }
    Recipe.update(data)
    return redirect('/welcome')

#route for SHOW ONE RECIPE
@app.route('/recipes/<int:id>')
def show_recipe(id):
    recipe = Recipe.get_by_id({'id': id})
    logged_user = User.get_by_id({'id': session['user_id']})
    return render_template('recipes_one.html', recipe=recipe, logged_user=logged_user)