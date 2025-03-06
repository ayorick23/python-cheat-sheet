import pyodbc

#Contectar a la base de datos
conn = pyodbc.connect(
    'DRIVER={SQL Server};' #o usa "SQL Server Native Client 11.0"
    'SERVER=localhost;'
    'DATABASE=test_db;'
    'UID=sa;' #usuario con permisos
    'PWD=password'
)
cursor = conn.cursor()

#Creacion de una tabla
cursor.execute('''
CREATE TABLE IF NOT EXISTS customers (
    id INT IDENTITY PRIMARY KEY,
    name NVARCHAR(100) NOT NULL,
    email NVARCHAR(100) NOT NULL
)
''')
conn.commit()

#Insercion de datos
cursor.execute("INSERT INTO customers (name, email) VALUES (?, ?)", ('Dereck', 'mayorickhenry@gmail.com'))
conn.commit()

#Consulta de datos
cursor.execute("SELECT * FROM customers")
print(cursor.fetchall())

#Cierre de la conexion
conn.close()