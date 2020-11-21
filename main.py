from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from datetime import datetime

app=Flask(__name__)

# TO GENERATE A RANDOM STRING FOR SECRET KEY
# import secrets
# secrets.token_hex(16)

app.config['SECRET_KEY']="48aba88f189fba176580b35b2a8bd5c8"
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///site.db"

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"User('{self.title}','{self.date_posted}')"

posts=[
    {
        "title":"Post 1",
        "author":"Divyansh Singh",
        "date_posted":"17/11/2020",
        "content":"Hello post 1"
    },
    {
        "title":"Post 2",
        "author":"Shivansh Singh",
        "date_posted":"18/11/2020",
        "content":"Hello post 2"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/register",methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html',title="Register", form=form)

@app.route("/login",methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        if form.email.data=='a@a.a' and form.password.data=='password':
            flash(f'Login Successful !','success')
            return redirect(url_for('home'))
        else:
            flash(f'Login Unsuccessful !','danger') 
    return render_template('login.html',title="Login", form=form)

if __name__=="__main__":
    app.run(debug=True)