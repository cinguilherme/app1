from flask import Flask, request
from flask_restful import Resource, Api
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

class Item(Resource):
    @jwt_required()
    def get(self, name):
        found = next(filter(lambda x: x['name'] == name, items), None)
        return {"item" : found}, 200 if found else 404
 
    def post(self, name):
        found = next(filter(lambda x: x['name'] == name, items), None)
        if(found):
            return {"message": "an item with given name '{}' already exists".format(name) }, 400

        data = request.get_json(silent=True)
        item = {"name": name, "price": data['price']}
        items.append(item)
        return item, 201

    def put(self, name):
        global items
        data = request.get_json(silent=True)
        found = next(filter(lambda x: x['name'] == name, items), None)
        
        if(found == None):
            item = {"name": name, "price": data['price']}
            items.append(item)
            return item, 201

        
        update = lambda x: data if x['name'] == name else x 
        items = list(map(update ,items))
        return { 'item': data }, 200

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