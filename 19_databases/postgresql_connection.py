import psycopg2

#Conectar a la base de datos
conn = psycopg2.connect(
    dbname='test_db',
    user='postgres',
    password='password',
    host='localhost'
)
cursor = conn.cursor()

#Creacion de una tabla
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    salary NUMERIC(10, 2)
)
''')

#Insercion de datos
cursor.execute("INSERT INTO employees (name, salary) VALUES (%s, %s)", ('Dereck', 2500))
conn.commit()

#Consulta de datos
cursor.execute("SELECT * FROM employees")
print(cursor.fetchall())

#Cierre de la conexion
conn.close()