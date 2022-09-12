from flask import Flask, render_template, request, redirect, session, make_response, url_for
app=Flask(__name__)
app.secret_key = 'no secrets on github'

@app.route('/')
def root():
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)