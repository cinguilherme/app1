from os import environ

from db import db

from sqlalchemy.dialects.postgresql import JSON

schema = environ['POSTGRES_SCHEMA']


class ItemModel(db.Model):

    __tablename__ = 'items'
    __table_args__ = {'schema': schema}

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(JSON)

    def __init__(self, name, price, store_id):
        self.data = {'name': name, 'price': price, 'store_id': store_id}

    def json(self):
        return {'data': self.data}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def item_by_name(cls, name):
        return cls.query.all()
        filter(ItemModel.data['name'].astext == name).first()

    @classmethod
    def get_all_items(cls):
        return cls.query.all()

    @classmethod
    def save_new_item(csl, name, data):
        item = ItemModel(name, **data)
        item.save_to_db()
        return item

    @classmethod
    def update_item(cls, name, data):
        item = cls.item_by_name(name)
        if item:
            item.price = data['price']
        else:
            item = ItemModel(name, data['price'])
        item.save_to_db()
        return item

    @classmethod
    def delete_item(cls, name):
        item = ItemModel.item_by_name(name)
        if item:
            item.delete_from_db()
            return True
        return False
