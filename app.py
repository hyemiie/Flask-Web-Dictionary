from flask import Flask, render_template, request, send_from_directory
import json
from difflib import get_close_matches

app = Flask(__name__)

data = json.load(open("data.json"))

@app.route('/')
def home():
    return render_template('layout.html')

@app.route('/static/css/<path:path>')
def send_css(path):
    return send_from_directory('static/css', path)


@app.route('/translate', methods=['GET', 'POST'])
def translate():
    if request.method == 'POST':
        word = request.form['word'].lower()
        if word in data:
            meaning = data[word]
            if meaning:
                return render_template('layout.html', meaning=' '.join(meaning), word=word)
        elif len(get_close_matches(word, data.keys())) > 0:
            suggestion = get_close_matches(word, data.keys())[0]
            return render_template('layout.html', suggestion=suggestion)
        else:
            return render_template('layout.html', error="Oops...this word doesn't exist")
    elif request.method == 'GET':
        word = request.args.get('word')
        if word in data:
            meaning = data[word]
            return render_template('layout.html', meaning=' '.join(meaning), word=word)
        else:
            return render_template('layout.html', error="Oops...this word doesn't exist")

if __name__ == '__main__':
    app.run(debug=True)
