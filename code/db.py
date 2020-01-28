import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

# the values of those depend on your setup
local_bd = 'postgresql+psycopg2://postgres:Postgres2019!@app1postgres:5432/test'
try:
    DB_URL = os.environ['DATABASE_URL']
except:
    DB_URL = local_bd

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


