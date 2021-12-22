import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

create_table = "CREATE TABLE table_games (id INTEGER PRIMARY KEY, name text, type text)"
cursor.execute(create_table)

connection.commit()
connection.close()