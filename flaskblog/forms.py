from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField , SubmitField , BooleanField
from wtforms.validators import DataRequired, Length , Email ,EqualTo ,ValidationError
from flaskblog.models import Student

class Search(FlaskForm):
    
    
    sbd = StringField('Số Báo Danh',
                        validators=[DataRequired()] )
  
    submit = SubmitField('Tra cứu')

        


class LoginForm(FlaskForm):
    
    username = StringField('Username' ,
                           validators=[DataRequired(),Length(min=2, max=20)])
    
    email = StringField('Email',
                        validators=[DataRequired(),Email()] )

    password = PasswordField('Password' ,
                                  validators=[DataRequired()])
    
    remember = BooleanField('Remember Me')

    submit = SubmitField('Login')


