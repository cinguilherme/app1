from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
import os

import create_db

from resources.user import UserResource
from resources.item import Item, ItemList

SECRET = os.environ['SECRET']
FLASK_APP = os.environ['FLASK_APP']
API_SETTING = os.environ['API_SETTING']

POSTGRES_PASSWORD = os.environ['POSTGRES_PASSWORD']
SERVER_HOST = os.environ['SERVER_HOST']
SERVER_PORT = int(os.environ['SERVER_PORT'])

#DBs URIs
POSTGRES_URL = os.environ['POSTGRES_URL']
SQLITE_URI = os.environ['SQLITE_URI']

app = Flask(__name__)

#mode sqlAlchemy stuff needs to be setup here
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = SQLITE_URI

app.secret_key = SECRET 
api = Api(app)

jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserResource, '/register')

print("running app on {} on the port {}".format(SERVER_HOST, SERVER_PORT))

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(host="0.0.0.0", port=5000, debug=True)