from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app=Flask(__name__)

# TO GENERATE A RANDOM STRING FOR SECRET KEY
# import secrets
# secrets.token_hex(16)

app.config['SECRET_KEY']="48aba88f189fba176580b35b2a8bd5c8"

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