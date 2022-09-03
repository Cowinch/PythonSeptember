from flask import Flask, render_template, request, redirect, session, make_response, url_for
app=Flask(__name__)
app.secret_key = 'no secrets on github'

@app.route('/')
def root():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e): #as far as I can tell this parameter literally exists just to stop a positional argument error.
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

if __name__=='__main__':
    app.run(debug=True)