from flask import render_template,redirect,request, session
from flask_app import app
from flask_app.models.email_model import Email
import re

#I have 4 route statements that are IDENTICAL how do I put functions and parameters to work here?
#CSS just stops working once there are too many '/' in a URL. whats going on here?

@app.route('/')
def index():
    if 'switch' not in session:
        session['switch']='date'
        session['order']='order'
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process_email():
    if not Email.validator(request.form):
        return redirect('/')
    Email.create(request.form)
    return redirect('/display')

@app.route('/display/date/reverse')
def display_emails_latest():
    all_emails=Email.get_all('id')
    latest_email=Email.get_latest()
    switch=session['switch']
    order=session['order']
    carrot='and'
    return render_template(
        'display.html', 
        all_emails=all_emails, 
        latest_email=latest_email, 
        switch=switch,
        carrot=carrot,
        order=order
    )

@app.route('/display/date/order')
def display_emails():
    all_emails=Email.get_all('id desc')
    latest_email=Email.get_latest()
    switch=session['switch']
    carrot='or'
    order=session['order']
    return render_template(
        'display.html', 
        all_emails=all_emails, 
        latest_email=latest_email, 
        switch=switch, 
        carrot=carrot,
        order=order
    )

@app.route('/display/alphabet/order')
def display_emails_alphabetically():
    all_emails=Email.get_all('name')
    latest_email=Email.get_latest()
    switch=session['switch']
    carrot='or'
    order=session['order']
    return render_template(
        'display.html', 
        all_emails=all_emails, 
        latest_email=latest_email, 
        switch = switch, 
        carrot=carrot,
        order=order
    )

@app.route('/display/alphabet/reverse')
def display_emails_alphabetically_reversed():
    all_emails=Email.get_all('name desc')
    latest_email=Email.get_latest()
    switch=session['switch']
    carrot='and'
    order=session['order']
    return render_template(
        'display.html', 
        all_emails=all_emails, 
        latest_email=latest_email, 
        switch = switch, 
        carrot=carrot,
        order=order
    )

@app.route('/display')
def reroute():
    return redirect(f'/display/{session["switch"]}/{session["order"]}')
    # if session['switch']=='date':
    #     return redirect('/display/date')
    # elif session['switch']=='alphabet':
    #     return redirect('/display/alphabet')
    # elif session['switch']=='latest':
    #     return redirect('/display/latest')
    # elif session['switch']=='alphabetreverse':
    #     return redirect('display/alphabetreverse')
    #who needs a giant if statement when you can just use an f string and PUT the dictionary to work!

@app.route('/display/alphabet/switch')
def switch_to_id():
    session['switch']='date'
    return redirect(f'/display/date/{session["order"]}')

@app.route('/display/date/switch')
def switch_to_alphabet():
    session['switch']='alphabet'
    return redirect(f'/display/alphabet/{session["order"]}')

@app.route('/display/date/flip')
@app.route('/display/alphabet/flip')
def flip_the_id():
    if session['order']=='order':
        session['order']='reverse'
    
    elif session['order']=='reverse':
        session['order']='order'
    
    return redirect(f'/display/{session["switch"]}/{session["order"]}')

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