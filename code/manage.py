import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)

try:
    schema = os.environ['POSTGRES_SCHEMA']
    DATABASE_URL = os.environ['DATABASE_URL']
except:
    schema = 'test'
    DATABASE_URL = 'postgresql+psycopg2://postgres:Postgres2019!@app1postgres:5432/test'

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

from models import user, store, item
manager.run()