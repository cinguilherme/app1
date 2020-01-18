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
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO items values (NULL, ?, ?)"
        cursor.execute(query, (name, data['price']))

        connection.commit()
        connection.close()
        return {'item': {'name':name, 'price':data['price']}}, 201

    def put(self, name):
        global items
        data = self.get_data()
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
        items = [{ 'name': item[1], 'price': item[2] } for item in get_all_items()]
        return {'items': items }, 200
