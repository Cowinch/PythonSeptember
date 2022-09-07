from flask import Flask, render_template, request, redirect, session, make_response, url_for
from friend import Friend
app=Flask(__name__)
app.secret_key = 'no secrets on github'

@app.route('/')
def root():
    # call the get all classmethod to get all friends
    friends = Friend.get_all()
    print(friends)
    return render_template('index.html', friends=friends)

@app.route('/create_friend', methods=["POST"])
def create_friend():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "occ" : request.form["occ"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    Friend.save(data)
    # Don't forget to redirect after saving to the database. We always want to redirect on post routes, never render.
    return redirect('/')



@app.errorhandler(404)
def page_not_found(e): #as far as I can tell this parameter literally exists just to stop a positional argument error.
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

if __name__=='__main__':
    app.run(debug=True)