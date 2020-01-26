from db import db
from os import environ

schema = environ['POSTGRES_SCHEMA']


class StoreModel(db.Model):

    __tablename__ = 'stores'
    __table_args__ = {'schema': schema}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    #items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name': self.name,
                'items': [item.json for item in self.items.all()]}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_all_stores(cls):
        return cls.query.all()

    @classmethod
    def create_table(cls):
        db.create_all()
        db.session.commit()
