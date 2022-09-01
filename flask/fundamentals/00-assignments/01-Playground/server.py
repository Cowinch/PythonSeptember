from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def nothing_here():
    return "Theres nothing here"

@app.route('/play')
def play():
    return render_template('play.html', number=3, color='aqua')

@app.route('/play/<int:number>')
def playAmount(number):
    return render_template('play.html', number=number, color='aqua')

@app.route('/play/<int:number>/<color>')
def playAmountColor(number, color):
    return render_template('play.html', number=number, color=color)

if __name__=='__main__':
    app.run(debug=True)