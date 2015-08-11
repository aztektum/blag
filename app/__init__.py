import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from config import basedir

app = Flask(__name__)
app.config.from_object('config')
app.config('GITHUB_CLIENT_ID')
app.config('GITHUB_CLIENT_SECRET')
db = SQLAlchemy(app)
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
github = GitHub(app)
oid = OpenID(app, os.path.join(basedir, 'tmp'))


from app import views, models
