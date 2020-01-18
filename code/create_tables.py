import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

try:
    create_table = "CREATE TABLE users (id INTEGER PRIMARY KEY, username text, password text)"
    cursor.execute(create_table)
except:
    print('users table already exists, its ok')


connection.commit()
connection.close()