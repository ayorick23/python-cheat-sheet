import sqlite3

#Conexion a la base de datos (o creacion si no existe)
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

#Creacion de una tabla
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
''')

#Insercion de datos
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Dereck', 25))
conn.commit()

#Consulta de datos
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

#Cierre de la conexion
conn.close()