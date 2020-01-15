from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)

items = []

class Item(Resource):
    def get(self, name):
        by_name = lambda item: item['name'] == name
        found = list(filter(by_name, items))
        if(len(found) > 0):
            return found.pop(), 200
        return { "item" : None }, 404
    
    def post(self, name):
        data = request.get_json(silent=True)
        item = {"name": name, "price": data['price']}
        items.append(item)
        return item, 201

    def put(self, name):
        pass
    
    def delete(self, name):
        pass

class ItemList(Resource):
    def get(self):
        return { 'items': items }

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)