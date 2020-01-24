from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from models.item import ItemModel

parser = reqparse.RequestParser()
parser.add_argument('price',
                    type=float, required=True,
                    help="this field cannot be blank")


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
            return {"message": "an item with given name '{}'" +
                    " already exists".format(name)}, 400

        data = self.get_data()

        try:
            item = ItemModel.save_new_item(name, data)
            json = item.json()
            obj = {'item': json}
            return obj, 201
        except Exception:
            return {'message': 'problem occurred'}, 503

    def put(self, name):
        data = self.get_data()
        item = ItemModel.item_by_name(name)
        try:
            if item:
                item.price = data['price']
                item.save_to_db()
                return {'item': item.json()}, 200
            else:
                item = ItemModel.save_new_item(name, data)
                return {'item': item.json()}, 201
        except Exception as error:
            return {'message': 'problem occurred {}'.format(error)}, 500

    @jwt_required()
    def delete(self, name):
        if ItemModel.delete_item(name):
            return {'message': 'item deleted'}, 204
        else:
            return {'message': 'unable to delete item'}, 500


class ItemList(Resource):
    def get(self):
        items = [item.json() for item in ItemModel.get_all_items()]
        return {'items': items}, 200
