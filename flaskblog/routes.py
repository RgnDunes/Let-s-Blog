from flask import render_template, url_for, flash, redirect
from flaskblog.models import User, Post
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog import app

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
