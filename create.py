from application import db
from application.models import Movies

db.drop_all()
db.create_all()
