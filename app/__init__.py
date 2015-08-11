import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.github import GitHub
#from flask.ext.openid import OpenID
from config import basedir

GITHUB_CLIENT_ID = os.environ['GITHUB_CLIENT_ID']
GITHUB_CLIENT_SECRET = os.environ['GITHUB_CLIENT_SECRET']

app = Flask(__name__)
app.config.from_object('config')
app.config[GITHUB_CLIENT_ID]
app.config[GITHUB_CLIENT_SECRET]
db = SQLAlchemy(app)
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
github = GitHub(app)
#oid = OpenID(app, os.path.join(basedir, 'tmp'))


from app import views, models
