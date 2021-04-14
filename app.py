from flask import Flask
from flask import render_template
from flask import request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('menu.html')

@app.route('/metronome-data', methods=['GET', 'POST'])
def metronome_data():

    if request.method == 'POST':
        TEMPO = request.form['tempo']
        BEATS = request.form['beats']
        return redirect(url_for('metronome_play', data1=TEMPO, data2=BEATS))

    else:
        return render_template('metronome_data.html')

@app.route('/metronome-play/<data1>/<data2>')
def metronome_play(data1, data2):

    return render_template('metronome_play.html', tempo=data1, beats=data2)

if __name__ == '__main__':
    app.run()
