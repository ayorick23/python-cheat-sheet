# Database Connections

La interacción de Python con bases de datos relacionales se realiza principalmente a través de módulos que implementan la **API de Base de Datos de Python (_DB-API 2.0_)**. Esta API proporciona una interfaz estándar para que los desarrolladores puedan escribir código de base de datos genérico que funcione con diferentes tipos de bases de datos, siempre que el controlador específico de la base de datos lo implemente.

## Generalidades de la Conexión DB-API 2.0

Aunque cada motor de base de datos tendrá un módulo Python ligeramente diferente para la conexión, el flujo general de uso de la DB-API 2.0 es el siguiente:

1. **Importar el módulo del conector:** Cada base de datos tiene su propia librería Python.
2. **Establecer la conexión:** Usar la función de conexión del módulo para crear un objeto `Connection`. Aquí se proporcionan los detalles de la base de datos (host, puerto, usuario, contraseña, nombre de la base de datos).
3. **Crear un cursor:** El objeto `Cursor` permite ejecutar comandos SQL. Es un iterador que permite recorrer los resultados de una consulta.
4. **Ejecutar consultas SQL:** Usar el método `execute()` del cursor para enviar comandos SQL (`SELECT`, `INSERT`, `UPDATE`, `DELETE`, `CREATE TABLE`, etc.).
5. **Obtener resultados (si aplica):** Para consultas `SELECT`, usar métodos como `fetchone()`, `fetchmany()`, o `fetchall()` del cursor para recuperar los datos.
6. **Confirmar cambios (commit):** Para consultas que modifican la base de datos (`INSERT`, `UPDATE`, `DELETE`), es crucial usar `connection.commit()` para guardar los cambios permanentemente. Si no se hace, los cambios no se aplicarán.
7. **Deshacer cambios (rollback):** En caso de error o si se desea cancelar los cambios pendientes, se usa `connection.rollback()`.
8. **Cerrar el cursor y la conexión:** Liberar los recursos cerrando el cursor y luego la conexión (`cursor.close()`, `connection.close()`).

**IMPORTANTE:** Siempre usa bloques `try`...`except`...`finally` o la declaración `with` para asegurar que las conexiones y los cursores se cierren correctamente, incluso si ocurren errores.

## Conexión a Motores de Bases de Datos Específicos

Para cada motor de base de datos, primero deberás instalar su respectivo conector de Python.

## SQLite

**SQLite** es una base de datos relacional ligera, autocontenida y sin servidor. No requiere un proceso de servidor separado y los datos se almacenan en un archivo único. Es ideal para aplicaciones pequeñas, desarrollo y pruebas.

- **Módulo:** `sqlite3` (¡Viene incluido con Python!)
- **Instalación:** No se necesita instalación adicional.

## MySQL

**MySQL** es uno de los sistemas de gestión de bases de datos relacionales de código abierto más populares.

- **Módulo:** `mysql-connector-python` o `PyMySQL` (`PyMySQL` es más fácil de instalar y puro Python).
- **Instalación:** `pip install PyMySQL`
- **Servidor:** Necesitas tener un servidor MySQL en ejecución.

## PostgreSQL

**PostgreSQL** es un potente sistema de gestión de bases de datos relacionales de código abierto, conocido por su robustez, características avanzadas y cumplimiento estricto de estándares SQL.

- **Módulo:** `psycopg2` (el más popular y robusto).
- **Instalación:** `pip install psycopg2-binary` (la versión `binary` es más fácil de instalar, no requiere compilación).
- **Servidor:** Necesitas tener un servidor PostgreSQL en ejecución.

## SQL Server

**SQL Server** es el sistema de gestión de bases de datos relacionales desarrollado por Microsoft.

- **Módulo:** `pyodbc` (un conector ODBC general que funciona con SQL Server, Access, Oracle, etc.).
- **Instalación:** `pip install pyodbc`
- **Controlador ODBC:** Necesitas tener un controlador ODBC para SQL Server instalado en tu sistema (ej. Microsoft ODBC Driver for SQL Server).
- **Servidor:** Necesitas tener un servidor SQL Server en ejecución.

## Oracle Database

**Oracle Database** es un sistema de gestión de bases de datos relacionales propietario, ampliamente utilizado en entornos empresariales.

- **Módulo:** `cx_Oracle` (ahora `python-oracledb`).
- **Instalación:** `pip install python-oracledb`
- **Cliente Instantáneo de Oracle:** Necesitas tener el Oracle Instant Client instalado y configurado en tu sistema. Esto es crucial y a menudo la parte más complicada.
- **Servidor:** Necesitas tener una instancia de base de datos Oracle en ejecución.

## Bases de Datos NoSQL

Aunque no cumplen con la **DB-API 2.0**, las bases de datos NoSQL son muy relevantes. Aquí se mencionan algunos ejemplos populares y sus librerías:

- **MongoDB:** Base de datos de documentos NoSQL.

  - **Módulo:** `pymongo`
  - **Instalación:** `pip install pymongo`
  - **Ejemplo:**

    ```python
    from pymongo import MongoClient

    # Conectar a MongoDB (por defecto localhost:27017)
    client = MongoClient('mongodb://localhost:27017/')
    db = client.mydatabase # Acceder a una base de datos
    collection = db.mycollection # Acceder a una colección

    # Insertar documento
    collection.insert_one({"name": "John Doe", "age": 30})

    # Buscar documento
    user = collection.find_one({"name": "John Doe"})
    print(f"Usuario encontrado: {user}")

    client.close()
    ```

- **Redis:** Base de datos en memoria, almacén de estructuras de datos.

  - **Módulo:** `redis`
  - **Instalación:** `pip install redis`
  - **Ejemplo:**

    ```python
    import redis

    # Conectar a Redis (por defecto localhost:6379)
    r = redis.Redis(host='localhost', port=6379, db=0)

    # Setear un valor
    r.set('mi_clave', 'mi_valor_en_redis')

    # Obtener un valor
    valor = r.get('mi_clave')
    print(f"Valor de Redis: {valor.decode('utf-8')}") # Los valores son bytes

    # Manipular listas
    r.lpush('mi_lista', 'item1', 'item2')
    items = r.lrange('mi_lista', 0, -1)
    print(f"Items de la lista: {[i.decode('utf-8') for i in items]}")
    ```

## Manejo de Credenciales Seguras

**¡Advertencia de Seguridad!** En los ejemplos, las credenciales están directamente en el código. **NUNCA HAGAS ESTO EN UN ENTORNO DE PRODUCCIÓN.** Para producción, usa:

- **Variables de Entorno:** Lee las credenciales de las variables de entorno (`os.environ`).
- **Archivos de Configuración Seguros:** Usa librerías como `python-dotenv` para cargar variables de entorno desde un archivo `.env` (que no debe estar en tu control de versiones).
- **Servicios de Gestión de Secretos:** Para entornos de nube (AWS Secrets Manager, Azure Key Vault, Google Secret Manager).

### Ejemplo de uso de `.env` con `python-dotenv`

1. **Instala:** `pip install python-dotenv`
2. **Crea un archivo `.env` en la raíz de tu proyecto:**

   ```env
   MYSQL_HOST=127.0.0.1
   MYSQL_USER=root
   MYSQL_PASSWORD=your_secure_password
   MYSQL_DATABASE=test_db
   ```

3. **Modifica el script de conexión (ej. 02_mysql_connection.py):**

   ```python
   import os
   import pymysql.cursors
   from dotenv import load_dotenv

   load_dotenv() # Carga las variables del archivo .env

   # Configuración de la base de datos desde variables de entorno
   DB_CONFIG = {
       'host': os.getenv('MYSQL_HOST'),
       'user': os.getenv('MYSQL_USER'),
       'password': os.getenv('MYSQL_PASSWORD'),
       'database': os.getenv('MYSQL_DATABASE'),
       'charset': 'utf8mb4',
       'cursorclass': pymysql.cursors.DictCursor
   }
   # ... el resto de la función connect_mysql ...
   ```
