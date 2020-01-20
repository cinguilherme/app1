from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
import os

import test

from resources.user import UserResource
from resources.item import Item, ItemList


SECRET = os.environ['SECRET']
FLASK_APP = os.environ['FLASK_APP']
API_SETTING = os.environ['API_SETTING']
DATABASE_URL = os.environ['DATABASE_URL']
POSTGRES_PASSWORD = os.environ['POSTGRES_PASSWORD']
SERVER_HOST = os.environ['SERVER_HOST']
SERVER_PORT = int(os.environ['SERVER_PORT'])

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = SECRET 
api = Api(app)

jwt = JWT(app, authenticate, identity) # /auth

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserResource, '/register')

print("running app on {} on the port {}".format(SERVER_HOST, SERVER_PORT))

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(host="0.0.0.0", port=5000, debug=True)