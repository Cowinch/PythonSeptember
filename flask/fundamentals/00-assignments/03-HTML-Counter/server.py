from flask import Flask, render_template, request, redirect, session, make_response, url_for
app=Flask(__name__)
app.secret_key = 'no secrets on github'

#if we want to view the values stored in the cookies, we can open a python shell (thats gunna be a terminal with >>>, just type python into cmder). Then well type import base64 and then base64.urlsafe_b64decode('') insert the first part of the cookies value (everything before the first . ) followed by === all inside of the ''

@app.route('/')
def root():
    #this if statement is responsible for generating the counter in session. We dont want session being set to 0 each time the site is loaded, so we use an if statement to check if it exists or not.
    if 'counter' not in session:
        session['counter']=0
    session['counter']+=1
    return render_template('index.html')

@app.route('/addition')
def count():
    #this, combined with the same line already running in the default root method, will increase the counter by 2
    session['counter']+=1
    return redirect('/')

@app.route('/reset')
def reset():
    #session.clear() is used to clear our backpack, AKA session
    session.clear()
    return redirect('/')

@app.errorhandler(404)
def page_not_found(e): #as far as I can tell this parameter literally exists just to stop a positional argument error.
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

if __name__=='__main__':
    app.run(debug=True)