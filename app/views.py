from flask import render_template
from app import app

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
