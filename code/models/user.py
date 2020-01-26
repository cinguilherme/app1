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

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

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
        user.save_to_db()
        return user