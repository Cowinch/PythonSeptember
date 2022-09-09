from flask_app import app
from flask_app.controllers import dojos_controller
from flask_app.controllers import ninjas_controller
from flask import render_template

@app.errorhandler(404)
def page_not_found(e): #as far as I can tell this parameter literally exists just to stop a positional argument error.
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

if __name__=='__main__':
    app.run(debug=True)