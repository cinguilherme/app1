from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity
import os

app = Flask(__name__)
secret = os.environ['SECRET']
secret = secret #this is not tobe here! get from env

app.secret_key = secret 
api = Api(app)

jwt = JWT(app, authenticate, identity) # /auth

items = []

parser = reqparse.RequestParser()
parser.add_argument('price', 
    type=float, required=True, help="this field cannot be blank")


def lookup(name):
    return next(filter(lambda x: x['name'] == name, items), None)

class Item(Resource):
    
    def get_data(self):
        return parser.parse_args()

    @jwt_required()
    def get(self, name):
        found = next(filter(lambda x: x['name'] == name, items), None)
        return {"item" : found}, 200 if found else 404
 
    def post(self, name):
        data = self.get_data()

        found = lookup(name)
        if(found):
            return {"message": "an item with given name '{}' already exists".format(name) }, 400

        item = {"name": name, "price": data['price']}
        items.append(item)
        return item, 201

    def put(self, name):
        data = self.get_data()
        
        global items
        
        found = lookup(name)
        
        if(found == None):
            item = {"name": name, "price": data['price']}
            items.append(item)
            return { 'item': item }, 201

        found.update(data)
        return { 'item': found }, 200

    @jwt_required()
    def delete(self, name):
        global items
        found = next(filter(lambda x: x['name'] == name, items), None)
        
        if(found == None):
            return {"message": "an item with given name '{}' does not exists".format(name) }, 404
        
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'item deleted'}, 204
        


class ItemList(Resource):
    def get(self):
        return { 'items': items }

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

#LINUX machine use 0.0.0.0 mac use 127.0.0.1
host="0.0.0.0" 

app.run(host=host,port=5000, debug=True)