import sqlite3
import os
from db import db

SQLITE_URI = os.environ['SQLITE_URI']
SQLITE_FILE = os.environ['SQLITE_FILE']

def get_connection():
    return sqlite3.connect(SQLITE_FILE)

def get_connection_cursor():
    connection = get_connection()
    return connection.cursor(), connection

def return_user_from_row(row):
    if row:
        user = UserModel(*row)
    else:
        user = None
    return user

class UserModel(db.Model):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    def json(self):
        return { 'username': self.username }

    @classmethod
    def find_by_username(cls, username):
        return UserModel.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return UserModel.query.filter_by(id=_id).first()

    @classmethod
    def create_new_user(cls, data):
        
        user = UserModel(_id=1,username=data['username'], password=data['password'])
        db.session.add(user)
        db.session.commit()

        return user