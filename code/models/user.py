import sqlite3

from db import db

def get_connection_cursor():
    connection = sqlite3.connect('data.db')
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

    @classmethod
    def find_by_username(cls, username):
        
        cursos, connection = get_connection_cursor()

        query = "select * from users where username=?"
        
        # this is crap python.. shame on you.
        result = cursos.execute(query, (username,))
        row = result.fetchone()
        
        user = return_user_from_row(row)
        connection.close()
        
        return user

    @classmethod
    def find_by_id(cls, _id):
        cursos, connection = get_connection_cursor()

        query = "select * from users where id=?"
         
        # this is crap python.. shame on you.
        result = cursos.execute(query, (_id,))
        row = result.fetchone()
        user = return_user_from_row(row)
        connection.close()
        return user

    @classmethod
    def create_new_user(cls, data):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "INSERT INTO users values (NULL, ?, ?)"
        cursor.execute(query, (data['username'], data['password']))

        connection.commit()
        connection.close()
        return True