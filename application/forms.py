from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,PasswordField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError,InputRequired
from application.models import Users, Movies
from flask_login import current_user


class addMovie(FlaskForm):
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
        validators=[
            InputRequired(message='A-D'),
           Length(min=1,max=1)
        ]
    )

    submit = SubmitField('Post!')

    def validate_title(self, title):
        movie = Movies.query.filter_by(title=title.data).first()

        if movie:
           raise ValidationError('Duplicate Movie')

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


class EmailChange(FlaskForm):
    email = StringField('Email',
        validators=[
            DataRequired(),
            Email()
        ])
    submit = SubmitField('Update')

    def validate_email(self,email):
        if email.data != current_user.email:
            user = Users.query.filter_by(email=email.data).first()
            if user:
              raise ValidationError('Email already in use')




class updateMovie(FlaskForm):
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
        validators=[
            InputRequired(message='A-D'),
           Length(min=1,max=1)
        ]
    )

    submit = SubmitField('Post!')

    def validate_title(self, title):
        movie = Movies.query.filter_by(title=title.data).first()

        if not movie:
           raise ValidationError('Movie Does Not Exist')



class delete_Movie(FlaskForm):
    title= StringField('Title:',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )

    submit = SubmitField('Delete!')

    def validate_title(self, title):
        movie = Movies.query.filter_by(title=title.data).first()

        if not movie:
           raise ValidationError('Movie Does Not Exist')
