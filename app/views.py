from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Maik'}

    posts = [
    {'author': {'nickname': 'Jon'}, 'body': "No piekny dzionek"},
    {'author': {'nickname': 'Ela'}, 'body': "No malo piekny dzionek"}
    ]

    return render_template('index.html', title='Home', user=user, posts=posts)
