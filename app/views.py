from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index(name=None):
    user = {'nickname': 'Michael'} # this luser is so fake
    posts = [ # fake posts or a bunch of dicts
        {
            'author': {'nickname': 'Dude'},
            'body': 'Brevity thing'
        },
        {
            'author': {'nickname': 'Donnie'},
            'body': 'Good burgers!'
        },
        {
            'author': {'nickname': 'Walter'},
            'body': 'Elements, dude. You\'re out of it.'
        }
    ]
    return render_template('index.html',
                            title='Welcome to blag!',
                            user=user,
                            posts=posts)

@app.route('/about')
def about(name=None):
    return render_template('about.html',
                            title='About')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me%s' %
                (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                            title='Sign In',
                            form=form,
                            providers=app.config['OPENID_PROVIDERS'])
