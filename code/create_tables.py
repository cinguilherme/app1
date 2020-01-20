import sqlite3
import os
SQLITE_URI = os.environ['SQLITE_URI']

connection = sqlite3.connect(SQLITE_URI)

cursor = connection.cursor()

try:
    create_table = "CREATE TABLE users (id INTEGER PRIMARY KEY, username text, password text)"
    cursor.execute(create_table)
except:
    print('users table already exists, its ok')


connection.commit()
connection.close()