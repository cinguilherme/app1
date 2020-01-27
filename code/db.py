import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

# the values of those depend on your setup

DB_URL = os.environ['DATABASE_URL']

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


