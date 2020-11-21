from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired(), Length(min=2,max=10)])
    email = StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired(),Length(min=5, max=10)])
    confirm_password=PasswordField('Confirm Password',validators=[DataRequired(),Length(min=5, max=10), EqualTo('password')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired(),Length(min=5, max=10)])
    remember=BooleanField('Remember Me')
    submit = SubmitField('Login')