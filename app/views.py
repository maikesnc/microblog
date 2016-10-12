from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Maik'}

    posts = [
    {'author': {'nickname': 'Jon'}, 'body': "No piekny dzionek"},
    {'author': {'nickname': 'Ela'}, 'body': "No malo piekny dzionek"}
    ]

    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        flash('Login request for OpenID="%s", remember_me=%s' %
        (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', title="Sign In", form=form,
                            providers=app.config['OPENID_PROVIDERS'])
