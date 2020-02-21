
from application import db, login_manager
from flask_login import UserMixin
from datetime import datetime

#Test change for jenkins

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(500), nullable=False, unique=True)
    password = db.Column(db.String(500), nullable=False)
    movies = db.relationship("Movies", backref="author", lazy=True)

    def __repr__(self):
        return ''.join(["UserID: ", str(self.id), "\r\n", "Email: ", self.email])
    @login_manager.user_loader
    def load_user(id):
        return Users.query.get(int(id))


class Movies(db.Model):
        movieid = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(30), nullable=False, unique=True)
        genre = db.Column(db.String(30), nullable=False)
        director = db.Column(db.String(30), nullable=False)
        rating = db.Column(db.String(1), nullable=False)
        date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
        user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

        def __repr__(self):
            return ''.join(["User ID: ",self.user_id,"\r\n,""Title: ", self.title,"\r\n","Genre: ", self.genre,"Director:  ",self.director,"\r\n","Rating: ",self.rating])



