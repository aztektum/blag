import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID

lm = LoginManager()
lm.init_app(app)
oid = OpenID(app, os.path.join(basedir, 'tmp'))
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app) # what is this? why do we still import app and not db

from app import views, models
