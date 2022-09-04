from flask import Flask, render_template, request, redirect, session, make_response, url_for
app=Flask(__name__)
app.secret_key = 'no secrets on github'

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/process_form', methods=['POST'])
def process():
    #send the form to the redirect method route, then the redirect line directs to our form method with the returning render template line.
    session['username']=request.form['username']
    session['location']=request.form['location']
    session['language']=request.form['language']
    session['comments']=request.form['comments']
    return redirect('/process')

@app.route('/process')
def show_form():
    print(session)
    username=session['username']
    location=session['location']
    language=session['language']
    comments=session['comments']
    return render_template(
        'process.html', 
        username=username, 
        location=location, 
        language=language, 
        comments=comments
    )

@app.errorhandler(404)
def page_not_found(e): #as far as I can tell this parameter literally exists just to stop a positional argument error.
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

if __name__=='__main__':
    app.run(debug=True)