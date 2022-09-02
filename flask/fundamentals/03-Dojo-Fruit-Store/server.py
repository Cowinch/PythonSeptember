from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'no secrets on github'

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    #session is like backpack carrying the files from one route to another. By doing this, it creates "cookies". Cookies are not quite the same thing as session though. We use redirect so that way if the page refreshes, it wont attempt to submit all the data again, and create duplicates (ie shopping carts back in the 2000s purchasing your order twice). Without session making cookies for us, this page redirected to would have not any of the info we submitted. Thats why session is a backpack.
    session['strawberry']=request.form['strawberry']
    session['apple']=request.form['apple']
    session['raspberry']=request.form['raspberry']
    session['first_name']=request.form['first_name']
    session['last_name']=request.form['last_name']
    session['student_id']=request.form['student_id']
    session['count']=int(session['strawberry']) + int(session['apple']) + int(session['raspberry'])
    # count=int(session['strawberry']) + int(session['apple']) + int(session['raspberry']) #this line of code would work if we rendered the template in this method isntead of redirecting. We do NOT want to do that though.
    
    print(request.form)
    # return render_template('checkout.html') #do not do this. when the page is refreshed the submitted form will be submitted twice.
    return redirect("/checkout")

@app.route('/checkout')
def render_checkout():
    return render_template('checkout.html')

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    