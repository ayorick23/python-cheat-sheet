import pyodbc

# Configuración de la base de datos
# Asegúrate de que el Driver de ODBC para SQL Server esté instalado en tu sistema.
# Ejemplos de drivers: '{ODBC Driver 17 for SQL Server}' o '{SQL Server}'
# Puedes ver los drivers disponibles en Windows: Administrador de orígenes de datos ODBC
DB_CONFIG = {
    'driver': '{ODBC Driver 17 for SQL Server}', # ¡Cambia esto si tu driver es diferente!
    'server': 'localhost', # O la IP/nombre de tu servidor SQL Server
    'database': 'test_db_sqlserver', # Crea esta base de datos previamente
    'uid': 'your_user',    # Tu usuario de SQL Server
    'pwd': 'your_password' # ¡Cambia esto por tu contraseña!
}

def connect_sqlserver():
    """Establece una conexión a una base de datos SQL Server y realiza operaciones básicas."""
    conn = None
    try:
        # Construir la cadena de conexión
        conn_str = (
            f"DRIVER={DB_CONFIG['driver']};"
            f"SERVER={DB_CONFIG['server']};"
            f"DATABASE={DB_CONFIG['database']};"
            f"UID={DB_CONFIG['uid']};"
            f"PWD={DB_CONFIG['pwd']};"
        )
        
        # 1. Establecer la conexión
        conn = pyodbc.connect(conn_str)
        print(f"Conexión exitosa a SQL Server: {DB_CONFIG['database']}")

        # 2. Crear un cursor
        cursor = conn.cursor()

        # 3. Ejecutar consultas SQL
        # Crear tabla (si no existe)
        # Nota: En SQL Server, se usa TOP para limitar resultados, y IDENTITY para auto-incremento
        cursor.execute("""
            IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='clientes' and xtype='U')
            CREATE TABLE clientes (
                id INT IDENTITY(1,1) PRIMARY KEY,
                nombre NVARCHAR(100) NOT NULL,
                email NVARCHAR(100)
            )
        """)
        print("Tabla 'clientes' creada o ya existe.")

        # Insertar datos
        cursor.execute("INSERT INTO clientes (nombre, email) VALUES (?, ?)", ("David", "david@example.com"))
        cursor.execute("INSERT INTO clientes (nombre, email) VALUES (?, ?)", ("Sara", "sara@example.com"))
        print("Datos insertados.")

        # 4. Confirmar cambios
        conn.commit()

        # 5. Obtener resultados
        print("\n--- Clientes registrados ---")
        cursor.execute("SELECT id, nombre, email FROM clientes")
        rows = cursor.fetchall()
        for row in rows:
            print(f"ID: {row.id}, Nombre: {row.nombre}, Email: {row.email}")

        # Actualizar datos
        cursor.execute("UPDATE clientes SET email = ? WHERE nombre = ?", ("david.nuevo@example.com", "David"))
        conn.commit()
        print("\nCliente 'David' actualizado.")

        # Eliminar datos
        cursor.execute("DELETE FROM clientes WHERE nombre = ?", ("Sara",))
        conn.commit()
        print("Cliente 'Sara' eliminado.")

    except pyodbc.Error as e:
        sqlstate = e.args[0]
        print(f"Error de SQL Server: {e} (SQLSTATE: {sqlstate})")
        if conn:
            conn.rollback() # Deshacer cambios en caso de error
    finally:
        # 6. Cerrar el cursor y la conexión
        if conn:
            cursor.close()
            conn.close()
            print("\nConexión a SQL Server cerrada.")

if __name__ == "__main__":
    connect_sqlserver()
    
# Antes de ejecutar:

# 1. Asegúrate de tener un servidor SQL Server en ejecución.
# 2. Crea una base de datos llamada test_db_sqlserver (o el nombre que elijas) en tu
# servidor SQL Server.
# 3. Instala el Controlador ODBC para SQL Server apropiado para tu sistema operativo.
# 4. Cambia your_user y your_password en DB_CONFIG por tus credenciales de SQL Server.
# 5. Verifica el driver en DB_CONFIG.