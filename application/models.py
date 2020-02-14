
from application import db, login_manager
from flask_login import UserMixin



@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(500), nullable=False, unique=True)
    password = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return ''.join(["UserID: ", str(self.id), "\r\n", "Email: ", self.email])





class Movies(db.Model):
        movieid = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(30), nullable=False, unique=True)
        genre = db.Column(db.String(30), nullable=False)
        director = db.Column(db.String(30), nullable=False)
        rating = db.Column(db.String(30), nullable=False)
        def __repr__(self):
            return ''.join(["Title: ", self.title,"\r\n","Genre: ", self.genre,"Director:  ",self.director,"\r\n","Rating: ",self.rating])



