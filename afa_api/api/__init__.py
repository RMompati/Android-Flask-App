"""
A simple database api for the Android Flask Application(afa).
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = 'f647d7af0e644e0f1dc3ce794a16438c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///api.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


from api import routes