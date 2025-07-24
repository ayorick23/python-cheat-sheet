import os
import sqlite3

class BaseDeDatosConexion:
    """
    Un gestor de contexto para gestionar una conexión a una base de datos SQLite.
    Asegura que la conexión se cierra al salir del bloque 'with'.
    """
    def __init__(self, db_nombre):
        self.db_nombre = db_nombre
        self.conn = None # La conexión se establecerá en __enter__

    def __enter__(self):
        print(f"INFO: Conectando a la base de datos: {self.db_nombre}...")
        try:
            self.conn = sqlite3.connect(self.db_nombre)
            self.conn.row_factory = sqlite3.Row # Para acceder a las columnas como diccionario
            print("INFO: Conexión establecida.")
            return self.conn # Esto es lo que se asigna a 'as db'
        except sqlite3.Error as e:
            print(f"ERROR: No se pudo conectar a la base de datos: {e}")
            raise # Relanzar la excepción

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            if exc_type:
                # Si hubo una excepción, hacemos rollback y registramos
                print(f"ADVERTENCIA: Se detectó una excepción ({exc_type.__name__}). Haciendo rollback.")
                self.conn.rollback()
            else:
                # Si no hubo excepción, hacemos commit
                print("INFO: No se detectaron errores. Haciendo commit.")
                self.conn.commit()
            self.conn.close()
            print("INFO: Conexión a la base de datos cerrada.")
        # Retornar False (o no retornar nada) para que Python relance la excepción si hubo una
        return False

# Nombre del archivo de la base de datos
db_file = "mi_aplicacion.db"

print("--- Escenario 1: Operaciones exitosas en la base de datos ---")
try:
    with BaseDeDatosConexion(db_file) as db:
        cursor = db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nombre TEXT, edad INTEGER)")
        cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", ("Alice", 30))
        cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", ("Bob", 24))
        print("Datos insertados.")

        cursor.execute("SELECT * FROM usuarios")
        usuarios = cursor.fetchall()
        print("\nUsuarios en la base de datos:")
        for user in usuarios:
            print(f"  ID: {user['id']}, Nombre: {user['nombre']}, Edad: {user['edad']}")

except Exception as e:
    print(f"ERROR: Ocurrió un error inesperado durante la operación: {e}")

print("\n--- Escenario 2: Operación con error (rollback) ---")
try:
    with BaseDeDatosConexion(db_file) as db:
        cursor = db.cursor()
        cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", ("Charlie", 35))
        print("Se intentó insertar a Charlie.")
        raise ValueError("Simulando un error antes del commit.") # Esto causará un rollback
except ValueError as e:
    print(f"Excepción capturada fuera del bloque: {e}")

# Verificar que Charlie NO fue insertado debido al rollback
print("\n--- Verificando la base de datos después del error ---")
with BaseDeDatosConexion(db_file) as db:
    cursor = db.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios_despues_error = cursor.fetchall()
    print("Usuarios actuales en la base de datos:")
    for user in usuarios_despues_error:
        print(f"  ID: {user['id']}, Nombre: {user['nombre']}, Edad: {user['edad']}")

# Limpieza (eliminar el archivo de la base de datos)
if os.path.exists(db_file):
    os.remove(db_file)
    print(f"\nArchivo de base de datos '{db_file}' eliminado.")