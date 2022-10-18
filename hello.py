from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/test')
def test():
    return render_template('index2.html')


app.run(host="localhost", debug=True)
