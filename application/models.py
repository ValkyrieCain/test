
from application import db

class Movies(db.Model):
        movieid = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(30), nullable=False, unique=True)
        genre = db.Column(db.String(30), nullable=False)
        director = db.Column(db.String(30), nullable=False)
        rating = db.Column(db.String(30), nullable=False)
        def __repr__(self):
            return ''.join(["Title: ", self.title,"\r\n","Genre: ", self.genre,"Director:  ",self.director,"\r\n","Rating: ",self.rating])
