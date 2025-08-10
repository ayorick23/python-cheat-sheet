import psycopg2
from psycopg2 import Error

# Configuración de la base de datos
DB_CONFIG = {
    'host': '127.0.0.1',      # O la IP de tu servidor PostgreSQL
    'database': 'test_db_pg', # Crea esta base de datos previamente
    'user': 'postgres',       # Tu usuario de PostgreSQL
    'password': 'your_password', # ¡Cambia esto por tu contraseña!
    'port': '5432'            # Puerto por defecto de PostgreSQL
}

def connect_postgresql():
    """Establece una conexión a una base de datos PostgreSQL y realiza operaciones básicas."""
    conn = None
    try:
        # 1. Establecer la conexión
        conn = psycopg2.connect(**DB_CONFIG)
        # Por defecto, psycopg2 abre transacciones automáticamente.
        # Para autocommit, puedes usar conn.autocommit = True
        conn.autocommit = False # Mantener el control manual de transacciones
        print(f"Conexión exitosa a PostgreSQL: {DB_CONFIG['database']}")

        # 2. Crear un cursor
        cursor = conn.cursor()

        # 3. Ejecutar consultas SQL
        # Crear tabla (si no existe)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS empleados (
                id SERIAL PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL,
                departamento VARCHAR(50)
            )
        """)
        print("Tabla 'empleados' creada o ya existe.")

        # Insertar datos
        cursor.execute("INSERT INTO empleados (nombre, departamento) VALUES (%s, %s)", ("Carlos", "Ventas"))
        cursor.execute("INSERT INTO empleados (nombre, departamento) VALUES (%s, %s)", ("Maria", "Marketing"))
        print("Datos insertados.")

        # 4. Confirmar cambios
        conn.commit()

        # 5. Obtener resultados
        print("\n--- Empleados registrados ---")
        cursor.execute("SELECT id, nombre, departamento FROM empleados")
        rows = cursor.fetchall()
        for row in rows:
            print(f"ID: {row[0]}, Nombre: {row[1]}, Departamento: {row[2]}")

        # Actualizar datos
        cursor.execute("UPDATE empleados SET departamento = %s WHERE nombre = %s", ("IT", "Carlos"))
        conn.commit()
        print("\nEmpleado 'Carlos' actualizado.")

        # Eliminar datos
        cursor.execute("DELETE FROM empleados WHERE nombre = %s", ("Maria",))
        conn.commit()
        print("Empleado 'Maria' eliminado.")

    except (Exception, Error) as e:
        print(f"Error de PostgreSQL: {e}")
        if conn:
            conn.rollback() # Deshacer cambios en caso de error
    finally:
        # 6. Cerrar el cursor y la conexión
        if conn:
            cursor.close()
            conn.close()
            print("\nConexión a PostgreSQL cerrada.")

if __name__ == "__main__":
    connect_postgresql()
    
# Antes de ejecutar:

# 1. Asegúrate de tener un servidor PostgreSQL en ejecución.
# 2. Crea una base de datos llamada test_db_pg (o el nombre que elijas) en tu servidor PostgreSQL.
# 3. Cambia your_password en DB_CONFIG por la contraseña de tu usuario postgres (o el usuario
# que uses).