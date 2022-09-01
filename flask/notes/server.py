from flask import Flask, render_template
app=Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/success')
def success():
    return "success"

@app.route('/say/<word>')
#path variables go in <>
#by default path variables are strings
def say_word(word):
    #remember to bring your path variables in as paramters
    return f"The word you gave me is: {word}"

@app.route('/template')
def template():
    return render_template("index.html")

if __name__=='__main__':
    app.run(debug=True)