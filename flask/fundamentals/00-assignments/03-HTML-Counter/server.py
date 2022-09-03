from flask import Flask, render_template, request, redirect, session
app=Flask(__name__)
app.secret_key = 'no secrets on github'

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

if __name__=='__main__':
    app.run(debug=True)