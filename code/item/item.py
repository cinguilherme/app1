from flask_restful import Resource, reqparse
from flask_jwt import JWT, jwt_required
import sqlite3

items = []

parser = reqparse.RequestParser()
parser.add_argument('price', 
    type=float, required=True, help="this field cannot be blank")


def lookup(name):
    return next(filter(lambda x: x['name'] == name, items), None)

def item_by_name(name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    query = "select * from items where name=?"
    result = cursor.execute(query, (name,))
    row = result.fetchone()
    connection.close()
    return row

def get_all_items():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    query = "select * from items"
    result = cursor.execute(query)
    row = result.fetchall()
    connection.close()
    return row

def save_new_item(name, data):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    query = "INSERT INTO items values (NULL, ?, ?)"
    cursor.execute(query, (name, data['price']))

    connection.commit()
    connection.close()
    return {'item': {'name':name, 'price':data['price']}}, 201

def update_item(name, data):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    query = "UPDATE items set price=? where name=?"
    cursor.execute(query, (data['price'],name))

    connection.commit()
    connection.close()
    return { 'message': ' to be implemented' }, 200

class Item(Resource):
    
    def get_data(self):
        return parser.parse_args()

    @jwt_required()
    def get(self, name):
        row = item_by_name(name)
        if row:
            return {'item': {'name': row[0], 'price': row[1]}}
        return {'message': 'item not found'}, 404
 
    def post(self, name):
        if item_by_name(name):
            return {"message": "an item with given name '{}' already exists".format(name) }, 400
        
        data = self.get_data()
        try:
            return save_new_item(name, data)
        except:
            return {'message': 'problem occurred'}, 503


    def put(self, name):
        data = self.get_data()
        try:
            if item_by_name(name):
                return update_item(name, data)
            else:
                return save_new_item(name, data)
        except:
            return {'message': 'problem occurred'}, 500
        

    @jwt_required()
    def delete(self, name):

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "DELETE FROM items where name=?"
        result = cursor.execute(query, (name,))
        connection.commit()
        connection.close();
        return {'message': 'item deleted'}, 204

class ItemList(Resource):
    def get(self):
        items = [{ 'name': item[1], 'price': item[2] } for item in get_all_items()]
        return {'items': items }, 200
