import mysql.connector

#Conectar a la base de datos
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='test_db'
)
cursor = conn.cursor()

#Creacion de una tabla
cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price FLOAT NOT NULL
)
''')

#Insercion de datos
cursor.execute("INSERT INTO products (name, price) VALUES (%s, %s)", ('Laptop', 1200))
conn.commit()

#Consulta de datos
cursor.execute("SELECT * FROM products")
print(cursor.fetchall())

#Cierre de la conexion
conn.close()