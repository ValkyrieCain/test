from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import Users

class PostRating(FlaskForm):
    title= StringField('Title:',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    genre = StringField('Genre:',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    director = StringField('Director:',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    rating = StringField('Rating:',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    submit = SubmitField('Post!')



class RegistrationForm(FlaskForm):
    email = StringField('Email',
        validators = [
            DataRequired(),
            Email()
        ]
    )
    password = PasswordField('Password',
        validators = [
            DataRequired(),
        ]
    )
    confirm_password = PasswordField('Confirm Password',
        validators = [
            DataRequired(),
            EqualTo('password')
        ]
    )
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('Email already in use')



class LoginForm(FlaskForm):
    email = StringField('Email',
        validators=[
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField('Password',
        validators=[
            DataRequired()
        ]
    )

    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
