from flask_login import LoginManager
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_bcrypt import Bcrypt
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= os.getenv('DB_URL')
db = SQLAlchemy(app)
from os import getenv
app.config['SECRET_KEY']= getenv('MY_SECRET_KEY')
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
from application import routes
