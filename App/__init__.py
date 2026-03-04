import os
import configparser
from flask import Flask

config = configparser.ConfigParser()
config.read('config.ini')

app = Flask(__name__)
# app.config['SECRET_KEY'] = config.get('APP', 'SECRET_TOKEN')
# app.config['SQLALCHEMY_DATABASE_URI'] = config.get('APP', 'DATABASE_URL')

# db = SQLAlchemy(app)
# bcrypt = Bcrypt(app)

app.app_context().push()

# from dashlink import routes
from App.routes import root
