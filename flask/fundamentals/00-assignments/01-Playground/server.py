from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def nothing_here():
    return "Theres nothing here"
if __name__=='__main__':
    app.run(debug=True)