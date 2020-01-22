from flask_restful import Resource, reqparse
from flask_jwt import JWT, jwt_required
import sqlite3

from models.item import ItemModel

parser = reqparse.RequestParser()
parser.add_argument('price', 
    type=float, required=True, help="this field cannot be blank")


class Item(Resource):
    
    def get_data(self):
        return parser.parse_args()

    @jwt_required()
    def get(self, name):
        item = ItemModel.item_by_name(name)
        if item:
            return {'item': item.json()}
        return {'message': 'item not found'}, 404
 
    def post(self, name):
        item = ItemModel.item_by_name(name)
        if item:
            return {"message": "an item with given name '{}' already exists".format(name) }, 400
        
        data = self.get_data()
        print(data)
        try:
            item = ItemModel.save_new_item(name, data)
            json = item.json()
            obj = { 'item': json }
            return obj , 201
        except:
            return {'message': 'problem occurred'}, 503


    def put(self, name):
        data = self.get_data()
        print(data)
        try:
            if ItemModel.item_by_name(name):
                item = ItemModel.update_item(name, data)
                return { 'item', item.json() } , 200
            else:
                item = ItemModel.save_new_item(name, data)
                return { 'item': item.json() }, 201
        except:
            return {'message': 'problem occurred'}, 500
        

    @jwt_required()
    def delete(self, name):
        if ItemModel.delete_item(name):
            return {'message': 'item deleted'}, 204
        else:
            return {'message': 'unable to delete item'}, 500


class ItemList(Resource):
    def get(self):
        items = ItemModel.get_all_items()
        return {'items': [item.json() for item in items] }, 200
