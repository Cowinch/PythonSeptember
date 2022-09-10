from flask import render_template,redirect,request
from flask_app import app
from flask_app.models.email_model import Email
import re

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process_email():
    if not Email.validator(request.form):
        return redirect('/')
    Email.create(request.form)
    return redirect('/display')

@app.route('/display')
def display_emails():
    all_emails=Email.get_all()
    latest_email=Email.get_latest()
    return render_template('display.html', all_emails=all_emails, latest_email=latest_email)

@app.route('/destroy/<int:id>')
def destroy_email(id):
    data = {
        "id": id
    }
    Email.destroy(data)
    return redirect('/display')

@app.errorhandler(404)
def page_not_found(e): #as far as I can tell this parameter literally exists just to stop a positional argument error.
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404