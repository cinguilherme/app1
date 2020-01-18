import sqlite3
from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()
parser.add_argument('username', 
    type=str, required=True, help="this field cannot be blank")
parser.add_argument('password', 
    type=str, required=True, help="this field cannot be blank")


def return_user_from_row(row):
    if row:
        user = User(*row)
    else:
        user = None
    return user

def get_connection_cursor():
    connection = sqlite3.connect('data.db')
    return connection.cursor(), connection

class User:
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

class UserResource(Resource):

    def get_data(self):
        return parser.parse_args()

    @classmethod
    def check_user_exist(cls, username, cursor):
        query = "SELECT username from users where username=?"
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        if(row):
            return True
        return False

    @classmethod
    def break_if_already_exists(cls, connection, data):
        cursor = connection.cursor()
        exists = UserResource.check_user_exist(data['username'], cursor)
        if(exists):
            connection.close()
            return { 'message': 'username already exists' }, 400
        return False

    @classmethod
    def create_new_user(cls, connection ,data):
        cursor = connection.cursor()
        query = "INSERT INTO users values (NULL, ?, ?)"
        cursor.execute(query, (data['username'], data['password']))

        connection.commit()
        connection.close()
        return {'message': 'user created successfuly'}, 201

    def post(self):
        data = self.get_data()
        
        connection = sqlite3.connect('data.db')
        exist = UserResource.break_if_already_exists(connection, data)
        if(exist == False):
            return UserResource.create_new_user(connection, data)
        else:
            return exist

