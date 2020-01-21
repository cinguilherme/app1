from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from flask_sqlalchemy import SQLAlchemy

import os

def migrate_db(app):
    try:
        from models.user import UserModel
        from models.item import ItemModel
        ItemModel.create_table(app)
        UserModel.create_table(app)
    except Exception as inst: 
        print("cannot migrate db, {}".format(inst))

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

app = Flask(__name__)

#mode sqlAlchemy stuff needs to be setup here
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL

#setup secret_key
app.secret_key = SECRET 
api = Api(app)

######### actual app #######
from resources.user import UserResource
from resources.item import Item, ItemList
from security import authenticate, identity

jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserResource, '/register')

print("running app on {} on the port {}".format(SERVER_HOST, SERVER_PORT))

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    migrate_db(app)
    app.run(host="0.0.0.0", port=5000, debug=True)
    