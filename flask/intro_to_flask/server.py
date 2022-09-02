from flask import Flask, render_template, request, redirect, session
app=Flask(__name__)
app.secret_key = 'no secrets on github'



#everything up here is pertaining to day 1 flask
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




#everything down here is pertaining to day 2 flask
@app.route('/input')
def input():
    return render_template('input.html')
@app.route('/process_form', methods=['POST']) #methos list for specifying methos to listen for
def process_form():
    print(request.form)
    session['dog_name'] = request.form['dog_name']
    session["dog_breed"] = request.form['dog_breed']
    session['form_num'] = request.form['form_num']
    # return render_template('display.html')#typically we WONT render on "ACTION ROUTES"
    return redirect('/show_info')

@app.route('/show_info')
def show_info():
    if 'form_num' in session:
        num=session['form_num']
    name = session['dog_name']
    breed = session['dog_breed']
    return render_template("display.html", name=name,breed=breed, num=num)

@app.route('/clear_session')
def clear_session():
    session.clear()#would remove all keys
    # del session['dog_breed']#would remove one key
    return redirect('/input')

if __name__=='__main__':
    app.run(debug=True)