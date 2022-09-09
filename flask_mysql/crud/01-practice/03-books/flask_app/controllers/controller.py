from flask import render_template,redirect,request
from flask_app import app

@app.route('/')
def index():
    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(e): #as far as I can tell this parameter literally exists just to stop a positional argument error.
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404