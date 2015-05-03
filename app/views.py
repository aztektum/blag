from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index(name=None):
    user = {'nickname': 'Michael'} # this luser is so fake
    return render_template('index.html',
                            title='Home',
                            user=user)

@app.route('/about')
def about(name=None):
    return render_template('about.html',
                            title='About')
