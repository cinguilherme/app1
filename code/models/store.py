from db import db
from os import environ
from sqlalchemy.dialects.postgresql import JSON

from models import item

try:
    schema = environ['POSTGRES_SCHEMA']
except:
    schema = 'test'


class StoreModel(db.Model):

    __tablename__ = 'stores'
    __table_args__ = {'schema': schema}

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(JSON)

    def __init__(self, name):
        self.data = {'name': name}

    def load_items():
        item.ItemModel.get_all_items()

    def json(self):
        return {'data': self.data}

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
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
