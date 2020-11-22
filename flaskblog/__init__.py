from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app=Flask(__name__)

# TO GENERATE A RANDOM STRING FOR SECRET KEY
# import secrets
# secrets.token_hex(16)

app.config['SECRET_KEY']="48aba88f189fba176580b35b2a8bd5c8"
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///site.db"

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskblog import routes