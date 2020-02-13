from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= os.getenv('DB_URL')
db = SQLAlchemy(app)
from os import getenv
app.config['SECRET_KEY']= getenv('MY_SECRET_KEY')
from application import routes
