from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def nothing_here():
    return "Theres nothing here"

def play():
    return render_template('play.html', number=3, color='aqua')

def playAmount(number):
    return render_template('play.html', number=number, color='aqua')

@app.route('/play')
@app.route('/play/<int:number>')
@app.route('/play/<int:number>/<color>')
def playAmountColor(number=3, color='aqua'):
    return render_template('play.html', number=number, color=color)

if __name__=='__main__':
    app.run(debug=True)