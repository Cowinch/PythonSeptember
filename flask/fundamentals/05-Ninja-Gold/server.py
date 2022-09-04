from flask import Flask, render_template, request, redirect, session, make_response, url_for
from random import randint
app=Flask(__name__)
app.secret_key = 'no secrets on github'

@app.route('/')
def root():
    #this if statement is because gold only needs to be set to 0 
    if 'gold' not in session:
        session['gold']=0
        session['activities']=[]
    gold=session['gold']
    activities=session['activities']
    return render_template('index.html', gold=gold, activities=activities) #because this is the page being rendered, values passed to jinja must be passed here

@app.route('/process_money', methods=['POST'])
def process():
    session['building']=request.form['building']
    if(session['building']=='farm'):
        random=randint(0,20)
        session['gold']+=random
        activities=session['activities']
        activities.append(f'<p id="green">Earned {random} gold from the farm!</p>')
    elif(session['building']=='cave'):
        random=randint(3,10)
        session['gold']+=random
        activities=session['activities']
        activities.append(f'<p id="green">Earned {random} gold from the cave!</p>')
    elif(session['building']=='house'):
        session['gold']+=6
        activities=session['activities']
        activities.append('<p id="green">Earned 6 gold from the house!</p>')
    elif(session['building']=='casino'):
        random=randint(-50,50)
        session['gold']+=random
        activities=session['activities']
        if random>0:
            activities.append(f'<p id="green">Earned {random} gold from the casino!</p>')
        else:
            activities.append(f'<p id="red">Lost {random} gold from the casino!</p>')
    print(session)
    return redirect('/')#do not attempt to pass values to jinja in a redirect method

@app.route('/reset', methods=['POST'])
def restart():
    #self explanatory. this resets our session, and in turn, the game iteslf
    session.clear()
    return redirect('/')



@app.errorhandler(404)
def page_not_found(e): #as far as I can tell this parameter literally exists just to stop a positional argument error.
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

if __name__=='__main__':
    app.run(debug=True)