from flask import Flask, render_template
app=Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/success')
def success():
    return "success"

@app.route('/say/<word>/<int:number>/')
#path variables go in <>
#by default path variables are strings
def say_word(word, number):
    #remember to bring your path variables in as paramters
    return render_template("say.html",word=word,number=number)

@app.route("/iterate")
def iterate():
    cats =[
        {
            'name': 'Garfield',
            'color': 'orange'
        },
        {
            'name': 'Scar',
            'color': 'dark brown'
        },
        {
            'name': 'Felix',
            'color': 'old'
        }
    ]
    return render_template('cats.html', cats=cats, h=100, w=100)

@app.route('/template')
def template():
    new_variable='This is a test tsring'
    return render_template("index.html", new_variable_html=new_variable)
    #the variable on the left is what we call it on html, the value on the right must match the variable defined above

if __name__=='__main__':
    app.run(debug=True)