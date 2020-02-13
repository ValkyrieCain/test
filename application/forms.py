from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

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
