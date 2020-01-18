import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

try:
    create_table = "CREATE TABLE users (id INTEGER PRIMARY KEY, username text, password text)"
    cursor.execute(create_table)
except:
    print('users table already exists, its ok')

#user = (1, 'jose', 'asd')
insert_query = "INSERT INTO users values (?,?,?)"
#cursor.execute(insert_query, user)

users = [
    (None, 'jose', 'asd'),
    (None, 'gui', 'asd'),
    (None, 'rose', 'asd')
]

cursor.executemany(insert_query, users)

select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)

connection.commit()
connection.close()