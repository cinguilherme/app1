import sqlite3
import os

# SQLITE_FILE = os.environ['SQLITE_FILE']
# connection = sqlite3.connect(SQLITE_FILE)

# #from db import db
# #db.session.create_all()tt

# cursor = connection.cursor()

# try:
#     create_table = "CREATE TABLE users (id INTEGER PRIMARY KEY, username text, password text)"
#     cursor.execute(create_table)
#     print('users table created')
# except:
#     print('users table already exists, its ok')

# try:
#     create_table = "CREATE TABLE items (id INTEGER PRIMARY KEY, name text, price float)"
#     cursor.execute(create_table)
#     print('items table created')
# except:
#     print('items table already exists, its ok')

# connection.commit()
# connection.close()