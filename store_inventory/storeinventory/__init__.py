from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'f4e83b72bf22101657b3cc64c9ccbe68'

from storeinventory import routes
from storeinventory import forms