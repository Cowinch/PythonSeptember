from flask import render_template,redirect,request
from flask_app import app
from flask_app.models.user_model import User

#home page, displays users
@app.route('/')
def index():
    all_users=User.get_all()
    return render_template("index.html", all_users=all_users)

#view one user
@app.route('/<int:id>/view')
def one_dog(id):
    one_user=User.get_one({'id': id})
    database_zeroes=''
    database_num_length=len(str(id))
    for i in range(0, 8-database_num_length, 1):
        database_zeroes+='0'
    return render_template('one_user.html', one_user=one_user,database_zeroes=database_zeroes)

#create new user FORM
@app.route('/create')
def create_form():
    return render_template('create.html')

#process new user FORM
@app.route('/process', methods=['POST'])
def process_form():
    User.create(request.form)
    return redirect('/')

#display edit for current user
@app.route('/<int:id>/edit')
def edit_user_form(id):
    data={
        'id': id
    }
    this_user=User.get_one(data)
    return render_template("user_edit.html", this_user=this_user)

#update current user on FORM
@app.route('/<int:id>/update', methods=['POST'])
def update_user(id):
    data={
        **request.form, #quick way to copy contents of request.form into dictionary
        'id': id,
    }
    User.update(data)
    return redirect('/')

#delete user from FORM
@app.route('/<int:id>/delete')
def delete_user(id):
    data={
        'id':id
    }
    User.delete(data)
    return redirect('/')



@app.errorhandler(404)
def page_not_found(e): #as far as I can tell this parameter literally exists just to stop a positional argument error.
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404