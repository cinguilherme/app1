from security import authenticate, identity

import postgres
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from flask_socketio import SocketIO

import os

from resources.item import Item, ItemList
from resources.user import UserResource
from resources.store import Store, StoreList

SECRET = os.environ['SECRET']

FLASK_APP = os.environ['FLASK_APP']
API_SETTING = os.environ['API_SETTING']

SERVER_HOST = os.environ['SERVER_HOST']
SERVER_PORT = int(os.environ['SERVER_PORT'])

DB_URL = postgres.get_postgres_uri()

app = Flask(__name__)

# POSTGRES mode sqlAlchemy stuff needs to be setup here SQL DB
POSTGRES_PW = os.environ['POSTGRES_PW']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL

# MONGO_DB NO SQL configs
app.config['MONGO_DBNAME'] = 'mongotask'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/mongotask'

# setup secret_key
app.secret_key = SECRET

# Wrap API in the app
api = Api(app)


# be sure all tables exist befire start
# this does not replace a migration strategy
@app.before_first_request
def create_tables():
    db.create_all()
    db.session.commit()


# wrap websocket in the app
socketIO = SocketIO(app)

# actual app resources and endpoints #######

jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(StoreList, '/stores')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserResource, '/register')

print("running app on {} on the port {}".format(SERVER_HOST, SERVER_PORT))

if __name__ == '__main__':
    from db import db
    db.init_app(app)

    from models.user import UserModel
    from models.store import StoreModel
    from models.item import ItemModel
    db.create_all()
    db.session.commit()

    # Theoretcly run the app with socketIO
    # to have it running as Websocket application
    # socketIO.run(app)

    # this option should be used for the rest application flavor
    app.run(host="0.0.0.0", port=5000, debug=True)
