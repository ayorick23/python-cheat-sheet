import sqlite3

def connect_sqlite(db_file="my_database.db"):
    """
    Establece una conexión a una base de datos SQLite y realiza operaciones básicas.
    Si el archivo de la base de datos no existe, se crea.
    """
    conn = None
    try:
        # 1. Establecer la conexión
        conn = sqlite3.connect(db_file)
        print(f"Conexión exitosa a SQLite: {db_file}")

        # 2. Crear un cursor
        cursor = conn.cursor()

        # 3. Ejecutar consultas SQL
        # Crear tabla (si no existe)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL,
                edad INTEGER
            )
        """)
        print("Tabla 'usuarios' creada o ya existe.")

        # Insertar datos
        cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", ("Alice", 30))
        cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", ("Bob", 24))
        print("Datos insertados.")

        # 4. Confirmar cambios
        conn.commit()

        # 5. Obtener resultados
        print("\n--- Usuarios registrados ---")
        cursor.execute("SELECT id, nombre, edad FROM usuarios")
        rows = cursor.fetchall()
        for row in rows:
            print(f"ID: {row[0]}, Nombre: {row[1]}, Edad: {row[2]}")

        # Actualizar datos
        cursor.execute("UPDATE usuarios SET edad = ? WHERE nombre = ?", (31, "Alice"))
        conn.commit()
        print("\nUsuario 'Alice' actualizado.")

        # Verificar actualización
        print("\n--- Usuarios después de la actualización ---")
        cursor.execute("SELECT id, nombre, edad FROM usuarios WHERE nombre = 'Alice'")
        updated_row = cursor.fetchone()
        if updated_row:
            print(f"ID: {updated_row[0]}, Nombre: {updated_row[1]}, Edad: {updated_row[2]}")

    except sqlite3.Error as e:
        print(f"Error de SQLite: {e}")
        if conn:
            conn.rollback() # Deshacer cambios en caso de error
    finally:
        # 6. Cerrar el cursor y la conexión
        if conn:
            conn.close()
            print("\nConexión a SQLite cerrada.")

if __name__ == "__main__":
    connect_sqlite()