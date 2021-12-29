from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskCode.models import User


class RegistrationForm(FlaskForm):
  username = StringField('Username', 
                         validators=[DataRequired(), Length(min=6, max=10)])
  
  email = StringField('Email',
                      validators=[DataRequired(), Email()])
  
  password = PasswordField('Password', validators=[DataRequired()])
  
  confirm_password = PasswordField('Cofirm Password', validators=[DataRequired(), EqualTo('password')])
  
  submit = SubmitField('Sign Up')
  
  def validate_username(self, username):
    user = User.query.filter_by(username=username.data).first()
    if user:
      raise ValidationError('Username Already Taken')
  
  def validate_email(self, email):
    user = User.query.filter_by(email=email.data).first()
    if user:
      raise ValidationError('Email Already Taken')
  
  
class LoginForm(FlaskForm): 
  email = StringField('Email',
                      validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])
  remember = BooleanField('Remember Me')
  submit = SubmitField('Login')