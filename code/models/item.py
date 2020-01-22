from flask_sqlalchemy import SQLAlchemy

from db import db

class ItemModel(db.Model):

    __tablename__ = 'items'
    __table_args__ = {'schema': 'test'}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def json(self):
        return { 'name': self.name, 'price': self.price }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def item_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def get_all_items(cls):
        return cls.query.all()

    @classmethod
    def save_new_item(csl, name, data):
        item = ItemModel(name=name, price=data['price'])
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

    @classmethod
    def create_table(cls):
        db.create_all()
        db.session.commit()