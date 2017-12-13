from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_openid import OpenID
from config import basedir
from flask_login import LoginManager
import os


app = Flask(__name__) #create application object
app.config.from_object('config')
db = SQLAlchemy(app)

# lm = LoginManager()
# lm.init_app(app)
# oid = OpenID(app, os.path.join(basedir, 'tmp'))
# lm.login_view = 'login'

from app import views, models