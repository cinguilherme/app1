import sqlite3

from db import db
import os
SQLITE_URI = os.environ['SQLITE_URI']
SQLITE_FILE = os.environ['SQLITE_FILE']

def get_connection():
    return sqlite3.connect(SQLITE_FILE)

class ItemModel(db.Model):

    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def json(self):
        return { 'name': self.name, 'price': self.price }

    @classmethod
    def item_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def get_all_items(cls):
        
        connection = get_connection()
        cursor = connection.cursor()
        query = "select * from items"
        result = cursor.execute(query)
        row = result.fetchall()
        connection.close()
        items = [ItemModel(n[1], n[2]).json() for n in row]
        return items

    @classmethod
    def save_new_item(csl, name, data):
        connection = get_connection()
        cursor = connection.cursor()

        query = "INSERT INTO items values (NULL, ?, ?)"
        cursor.execute(query, (name, data['price']))

        connection.commit()
        connection.close()
        return {'item': {'name':name, 'price':data['price']} }, 201

    @classmethod
    def update_item(cls, name, data):
        connection = get_connection()
        cursor = connection.cursor()

        query = "UPDATE items set price=? where name=?"
        cursor.execute(query, (data['price'],name))

        connection.commit()
        connection.close()
        return { 'item': data }, 200

    @classmethod
    def delete_item(cls, name):
        connection = get_connection()
        cursor = connection.cursor()

        query = "DELETE FROM items where name=?"
        result = cursor.execute(query, (name,))
        connection.commit()
        connection.close()
        return True

