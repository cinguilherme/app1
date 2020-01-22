from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from flask_sqlalchemy import SQLAlchemy

import os

SECRET = os.environ['SECRET']
FLASK_APP = os.environ['FLASK_APP']
API_SETTING = os.environ['API_SETTING']
POSTGRES_PW = os.environ['POSTGRES_PW']
SERVER_HOST = os.environ['SERVER_HOST']
SERVER_PORT = int(os.environ['SERVER_PORT'])

import postgres
DB_URL = postgres.get_postgres_uri()

app = Flask(__name__)

#mode sqlAlchemy stuff needs to be setup here
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL

#setup secret_key
app.secret_key = SECRET 
api = Api(app)

######### actual app resources and endpoints #######
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
    
    from models.user import UserModel
    from models.item import ItemModel
    UserModel.create_table()
    ItemModel.create_table()

    app.run(host="0.0.0.0", port=5000, debug=True)
    