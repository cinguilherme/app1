from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
app.secret = "jose" #this is not tobe here!
api = Api(app)

items = []

class Item(Resource):
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
        pass

    def delete(self, name):
        pass

class ItemList(Resource):
    def get(self):
        return { 'items': items }

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)