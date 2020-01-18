import sqlite3


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