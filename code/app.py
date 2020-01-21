from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from flask_sqlalchemy import SQLAlchemy

import os

import create_db

def get_env_variable(name):
    try:
        return os.environ[name]
    except KeyError:
        message = "Expected environment variable '{}' not set.".format(name)
        raise Exception(message)

SECRET = os.environ['SECRET']
FLASK_APP = os.environ['FLASK_APP']
API_SETTING = os.environ['API_SETTING']
POSTGRES_PW = os.environ['POSTGRES_PW']
SERVER_HOST = os.environ['SERVER_HOST']
SERVER_PORT = int(os.environ['SERVER_PORT'])

# the values of those depend on your setup
POSTGRES_URL = get_env_variable("POSTGRES_URL")
POSTGRES_USER = get_env_variable("POSTGRES_USER")
POSTGRES_PW = get_env_variable("POSTGRES_PW")
POSTGRES_DB = get_env_variable("POSTGRES_DB")
DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)

#DBs URIs
POSTGRES_URL = os.environ['POSTGRES_URL']
SQLITE_URI = os.environ['SQLITE_URI']

app = Flask(__name__)

#mode sqlAlchemy stuff needs to be setup here
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# SQLITE or POSTGRES
#app.config['SQLALCHEMY_DATABASE_URI'] = SQLITE_URI
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL

app.secret_key = SECRET 
api = Api(app)

import db
db.create_db(app)


######### actual app #######
from resources.user import UserResource
from resources.item import Item, ItemList
from security import authenticate, identity

jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserResource, '/register')

# Command to clear DB
@app.cli.command('resetdb')
def resetdb_command():
    """Destroys and creates the database + tables."""

    from sqlalchemy_utils import database_exists, create_database, drop_database
    if database_exists(DB_URL):
        print('Deleting database.')
        drop_database(DB_URL)
    if not database_exists(DB_URL):
        print('Creating database.')
        create_database(DB_URL)

    print('Creating tables.')
    db.create_all()
    print('Shiny!')


print("running app on {} on the port {}".format(SERVER_HOST, SERVER_PORT))

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(host="0.0.0.0", port=5000, debug=True)