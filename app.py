import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    print("Test")
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM records').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)


def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM reports WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post


  
@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('report.html', post=post)


@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        username = request.form['username']
        psswrd = request.form['psswrd']

        if not username:
            flash('Username is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO admins (username, psswrd) VALUES (?, ?)',
                         (username, psswrd))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')

app.run(host="localhost", debug=True)
