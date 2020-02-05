from db import db
from security import authenticate, identity

import postgres
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from flask_migrate import Migrate

import os

from resources.item import Item, ItemList
from resources.user import UserResource
from resources.store import Store, StoreList

from extensions import mongo

try:
    SECRET = os.environ['SECRET']
except:
    SECRET = 'seecret_local'

try:
    API_SETTING = os.environ['API_SETTING']
except:
    API_SETTING = 'development'

app = Flask(__name__)

DB_URL = postgres.get_postgres_uri()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config["MONGO_URI"] = os.environ['MONGO_URL']


# setup secret_key
app.secret_key = SECRET

# Wrap API in the app
api = Api(app)
mongo.init_app(app)

# be sure all tables exist befire start
# this does not replace a migration strategy
@app.before_first_request
def create_tables():
    db.create_all()
    db.session.commit()

# actual app resources and endpoints #######


#########

jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(StoreList, '/stores')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserResource, '/register')

#########


db.init_app(app)
migrate = Migrate(app, db)

if __name__ == '__main__':

    from models.user import UserModel
    from models.store import StoreModel
    from models.item import ItemModel
    db.create_all()

    # this option should be used for the rest application flavor
    app.run(host="0.0.0.0", port=5000, debug=True)
