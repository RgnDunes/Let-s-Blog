from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)

# TO GENERATE A RANDOM STRING FOR SECRET KEY
# import secrets
# secrets.token_hex(16)

app.config['SECRET_KEY']="48aba88f189fba176580b35b2a8bd5c8"
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///site.db"

db = SQLAlchemy(app)

from flaskblog import routes