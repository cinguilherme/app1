import sqlite3

class ItemModel:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def json(self):
        return { 'name': self.name, 'price': self.price }

    @classmethod
    def item_by_name(csl, name):
        try:
            connection = sqlite3.connect('data.db')
            cursor = connection.cursor()
            query = "select * from items where name=?"
            result = cursor.execute(query, (name,))
            row = result.fetchone()
            connection.close()
            return ItemModel(row[1], row[2])
        except:
            return None

    @classmethod
    def get_all_items(cls):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "select * from items"
        result = cursor.execute(query)
        row = result.fetchall()
        connection.close()
        items = [ItemModel(n[1], n[2]).json() for n in row]
        return items

    @classmethod
    def save_new_item(csl, name, data):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO items values (NULL, ?, ?)"
        cursor.execute(query, (name, data['price']))

        connection.commit()
        connection.close()
        return {'item': {'name':name, 'price':data['price']} }, 201

    @classmethod
    def update_item(cls, name, data):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "UPDATE items set price=? where name=?"
        cursor.execute(query, (data['price'],name))

        connection.commit()
        connection.close()
        return { 'item': data }, 200

    @classmethod
    def delete_item(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "DELETE FROM items where name=?"
        result = cursor.execute(query, (name,))
        connection.commit()
        connection.close();
        return True

