from os import environ

from db import db

schema = environ['POSTGRES_SCHEMA']


class UserModel(db.Model):

    __tablename__ = 'users'
    __table_args__ = {'schema': schema}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __repr__(self):
        return '<User %r>' % self.username

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def json(self):
        return {'username': self.username}

    @classmethod
    def find_by_username(cls, username):
        return UserModel.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return UserModel.query.filter_by(id=_id).first()

    @classmethod
    def create_new_user(cls, data):
        user = UserModel(username=data['username'],
                         password=data['password'])
        db.session.add(user)
        db.session.commit()
        return user

    @classmethod
    def create_table(cls):
        db.create_all()
        db.session.commit()
