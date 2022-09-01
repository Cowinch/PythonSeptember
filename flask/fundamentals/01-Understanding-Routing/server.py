from flask import Flask
app=Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def sayDojo():
    return 'Dojo!'

@app.route('/say/<string:name>')
def say_hello(name):
    print(name)
    return 'Hello ' + name + '!'

@app.route('/repeat/<int:num>/<string:word>')
def repeat(num, word):
    return word * num


if __name__=='__main__':
    app.run(debug=True)