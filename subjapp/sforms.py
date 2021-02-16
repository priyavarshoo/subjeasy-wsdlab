from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, NumberRange, ValidationError
from subjapp.smodels import User
from subjapp import autoIncrement

class RegForm(FlaskForm):
    #id = autoIncrement()
    
    name = StringField('Name',
                           validators=[DataRequired(), Length(min=1, max=30)])
    username = StringField('Roll Number', 
                           validators=[DataRequired(), Length(min=9, max=9)])
    year = IntegerField('Year of Study',
                           validators=[DataRequired()])
    degree = StringField('Degree',
                           validators=[DataRequired(),Length(min=1, max=30)])
    department = StringField('Department',
                           validators=[DataRequired(),Length(min=1, max=50)])
    hall = StringField('Hall',
                        validators=[DataRequired()])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                        validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                        validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
    
    def validate_username(self, username):
    
        user = User.query.filter_by(username = self.username.data).first()
    
        if user:
            raise ValidationError('That username is already in use. Please choose a different one.')

    def validate_email(self, email):
    
        user = User.query.filter_by(email = self.email.data).first()
    
        if user:
            raise ValidationError('That email is already in use. Please choose a different one.')


class LoginForm(FlaskForm):
    #id = autoIncrement()
    username = StringField('Roll Number',
                        validators=[DataRequired()])
    password = PasswordField('Password',
                        validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
    
 
