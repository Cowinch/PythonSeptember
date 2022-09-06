from flask import Flask, render_template, request, redirect, session, make_response, url_for
from random import randint
import re
app=Flask(__name__)
app.secret_key = 'no secrets on github'

"""
    Three things to ask spencer:
        1: How do I use back end python to remove an HTML element (ie the Moves left: ) (correct answer is to just use a conditional jinja statement to just not even render it)
        2: I am unable to iterate  my for loop backwards as I am unable to use range() as it says the variable is undefined (we now know this was because jinja's syntax wants a |length instead of wrapping the array in len() )
        3: the entire if statement thats responsible for asking what button was pressed and assigning random gold causes an undefined error if I put all of that in an if moves>0 statement. Why? (somehow we fixed this and I didnt quite catch how we did that...)
"""

@app.route('/')
def root():
    #this if statement is because gold only needs to be set to 0 if this is the "first" time the user visits the page
    if 'gold' not in session:
        session['gold']=0
        session['activities']=[]
        session['button']=''#this line of code is used to generate a button when 15 moves have been spent
        session['left']='<p>Moves left: {moves}</p>'
        #the left variable was an attempt at removing the Moves Left after there are no moves left. Sadly, Jinja does not recongize Jinja> though it is possible with an f string, as this point we are doing Jinja's job for Jinja and it makes much more sense to do the math on the HTML page
        session['moves']=15


    gold=session['gold']
    activities=session['activities']
    # activities=reversed(activities)
    #this reversed class, imported from re, flips the index around. This is what allows us to print our activites in order from newest performed.
    
    button=session['button']
    left=session['left']
    moves=session['moves']
    
    if moves==0:
        #we need to be careful not to create an infinite redirect loop here
        return redirect('/game_over')
    
    return render_template(
        'index.html', 
        gold=gold, 
        left=left,
        activities=activities, 
        moves=moves, 
        button=button,
    ) #because this is the page being rendered, values passed to jinja must be passed here

@app.route('/process_money', methods=['POST'])
def process():
    session['building']=request.form['building']
    if session['moves']>0:
        if(session['building']=='farm'):
            random=randint(-5,25)
            session['gold']+=random
            activities=session['activities']
            activities.append(f'<p id="green">Earned {random} gold from the farm!</p>')
        elif(session['building']=='cave'):
            random=randint(3,12)
            session['gold']+=random
            activities=session['activities']
            activities.append(f'<p id="green">Earned {random} gold from the cave!</p>')
        elif(session['building']=='house'):
            session['gold']+=7
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
    else:
        return redirect('/')
    
    #these 3 lines of code is what decrements the moves left display. If this was performed in the root() method then it run everytime the page was refreshed. We don't want that
    moves=session['moves']
    moves-=1
    session['moves']=moves
    print(session)
    return redirect('/')#do not attempt to pass values to jinja in a redirect method

@app.route('/game_over')
def gameOver():
    moves=session['moves']
    moves-=1
    session['moves']=moves
    #we turn the moves value into a string, so it still displays 0 moves left to the user but, it wont run the if moves==0 statement again, saving us from an infinite redirect loop and crashing the page
    session['button']='<div><button name="reset" >reset</button></div>'
    return redirect('/')

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