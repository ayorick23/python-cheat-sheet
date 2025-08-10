import pymysql.cursors

# Configuración de la base de datos
DB_CONFIG = {
    'host': '127.0.0.1', # O la IP de tu servidor MySQL
    'user': 'root',      # Tu usuario de MySQL
    'password': 'your_password', # ¡Cambia esto por tu contraseña!
    'database': 'test_db', # Crea esta base de datos previamente
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor # Para obtener resultados como diccionarios
}

def connect_mysql():
    """Establece una conexión a una base de datos MySQL y realiza operaciones básicas."""
    conn = None
    try:
        # 1. Establecer la conexión
        conn = pymysql.connect(**DB_CONFIG)
        print(f"Conexión exitosa a MySQL: {DB_CONFIG['database']}")

        # 2. Crear un cursor
        cursor = conn.cursor()

        # 3. Ejecutar consultas SQL
        # Crear tabla (si no existe)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS productos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(255) NOT NULL,
                precio DECIMAL(10, 2)
            )
        """)
        print("Tabla 'productos' creada o ya existe.")

        # Insertar datos
        cursor.execute("INSERT INTO productos (nombre, precio) VALUES (%s, %s)", ("Laptop", 1200.50))
        cursor.execute("INSERT INTO productos (nombre, precio) VALUES (%s, %s)", ("Mouse", 25.00))
        print("Datos insertados.")

        # 4. Confirmar cambios
        conn.commit()

        # 5. Obtener resultados
        print("\n--- Productos registrados ---")
        cursor.execute("SELECT id, nombre, precio FROM productos")
        rows = cursor.fetchall()
        for row in rows:
            print(f"ID: {row['id']}, Nombre: {row['nombre']}, Precio: {row['precio']}")

        # Actualizar datos
        cursor.execute("UPDATE productos SET precio = %s WHERE nombre = %s", (1150.00, "Laptop"))
        conn.commit()
        print("\nProducto 'Laptop' actualizado.")

        # Eliminar datos
        cursor.execute("DELETE FROM productos WHERE nombre = %s", ("Mouse",))
        conn.commit()
        print("Producto 'Mouse' eliminado.")

    except pymysql.Error as e:
        print(f"Error de MySQL: {e}")
        if conn:
            conn.rollback() # Deshacer cambios en caso de error
    finally:
        # 6. Cerrar el cursor y la conexión
        if conn:
            conn.close()
            print("\nConexión a MySQL cerrada.")

if __name__ == "__main__":
    connect_mysql()
    
# Antes de ejecutar:

# 1. Asegúrate de tener un servidor MySQL en ejecución.
# 2. Crea una base de datos llamada test_db (o el nombre que elijas) en tu servidor MySQL.
# 3. Cambia your_password en DB_CONFIG por la contraseña de tu usuario root (o el usuario 
# que uses).