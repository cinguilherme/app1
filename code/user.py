import sqlite3


def return_user_from_row(row):
    row = result.fetchone()
    if row:
        user = User(*row)
    else:
        user = None
    connection.close()
    return user

def get_connection_cursor():
    connection = sqlite3.connect('data.db')
    cursos = connection.cursor()

class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        cursos = get_connection_cursor()

        query = "select * from users where username=?"
         
        # this is crap python.. shame on you.
        result = cursos.execute(query, (username,))
        row = result.fetchone()
        return_user_from_row(row)

    @classmethod
    def find_by_id(cls, _id):
        cursos = get_connection_cursor()

        query = "select * from users where id=?"
         
        # this is crap python.. shame on you.
        result = cursos.execute(query, (_id,))
        row = result.fetchone()
        return_user_from_row(row)