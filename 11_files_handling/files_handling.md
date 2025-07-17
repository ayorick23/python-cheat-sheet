# Files Handling

Python proporciona módulos robustos como `os` y `pathlib` para interactuar con el sistema de archivos de tu computadora, permitiéndote crear, leer, escribir, mover y eliminar archivos y directorios.

## Rutas de Windows y Sistemas Basados en Unix

Una de las primeras cosas a tener en cuenta es cómo los diferentes sistemas operativos representan las rutas de archivos:

- **Sistemas basados en Unix (Linux, macOS, etc.):** Utilizan la barra inclinada hacia adelante (`/`) como separador de directorios.
- **Windows:** Utiliza la barra invertida (`\`) como separador de directorios.

Esta diferencia puede ser una fuente de errores si no se maneja correctamente. Afortunadamente, Python ofrece herramientas para abstraer esta disparidad.

## Módulo `os`

El módulo `os` es un pilar para interactuar con el sistema operativo. Su submódulo `os.path` contiene funciones útiles para manipular rutas. La función `os.path.join()` es fundamental porque une componentes de ruta utilizando el separador correcto para el sistema operativo en el que se ejecuta tu código, haciendo tus scripts portátiles.

```python
import os
ruta_completa = os.path.join('directorio', 'subdirectorio', 'archivo.txt')
```

## Módulo `pathlib`

Introducido en Python 3.4, el módulo `pathlib` ofrece una forma orientada a objetos de manejar rutas de archivos, lo que a menudo resulta en código más legible y robusto que el módulo `os.path`. Abstrae las diferencias del sistema operativo de forma nativa.

```python
from pathlib import Path
ruta = Path('directorio') / 'subdirectorio' / 'archivo.txt'
```

## Obtener el Directorio de Trabajo Actual

Saber dónde se encuentra tu script es crucial para el manejo de archivos relativos.

- `os.getcwd()`: Devuelve la ruta absoluta del directorio de trabajo actual.
- `Path.cwd()`: La contraparte orientada a objetos de `pathlib`.

## Creación de Nuevas Carpetas

Crear directorios es una operación común.

- `os.mkdir(ruta)`: Crea un solo directorio. Lanza un `FileExistsError` si el directorio ya existe.
- `os.makedirs(ruta, exist_ok=False)`: Crea directorios recursivamente (todos los directorios intermedios necesarios). Si `exist_ok=True`, no lanza un error si el directorio ya existe.
- `Path.mkdir(parents=False, exist_ok=False)`: La contraparte de `pathlib`. `parents=True` crea directorios intermedios. `exist_ok=True` previene el error si ya existe.

## Rutas Absolutas y Relativas

### Ruta Absoluta

Describe la ubicación completa de un archivo o directorio desde la raíz del sistema de archivos.

```bash
C:/home/usuario/documentos/mi_archivo.txt # Unix
C:\Users\Usuario\mi_archivo.txt           # Windows
```

### Ruta Relativa

Describe la ubicación de un archivo o directorio en relación con el directorio de trabajo actual.

```bash
documentos/mi_archivo.txt # si tu script está en /home/usuario/
```

### Manejo

- `os.path.abspath(ruta)`: Convierte una ruta relativa en absoluta.
- `Path.resolve()`: La contraparte de `pathlib`, devuelve la ruta absoluta y resuelve cualquier enlace simbólico.
- `os.path.relpath(ruta, start_dir)`: Calcula la ruta relativa de ruta desde `start_dir`.
- `Path.relative_to(otro_path)`: La contraparte de `pathlib`.

## Validez de Rutas de Archivos

Es crucial verificar si una ruta, un archivo o un directorio existen antes de intentar operar con ellos para evitar errores.

- `os.path.exists(ruta)`: Devuelve `True` si la ruta existe (sea archivo o directorio).
- `os.path.isfile(ruta)`: Devuelve `True` si la ruta existe y es un archivo.
- `os.path.isdir(ruta)`: Devuelve `True` si la ruta existe y es un directorio.
- `Path.exists()`, `Path.is_file()`, `Path.is_dir()`: Las contrapartes de `pathlib`.

## Obtención del Tamaño de Archivos en Bytes

- `os.path.getsize(ruta)`: Devuelve el tamaño del archivo en bytes. Lanza un `FileNotFoundError` si el archivo no existe.
- `Path.stat().st_size`: La forma equivalente con `pathlib`.

## Listado de Contenido de Directorios

- `os.listdir(ruta)`: Devuelve una lista de cadenas con los nombres de los archivos y directorios dentro de la ruta especificada. No incluye `.` ni `..`.
- `Path.iterdir()`: Devuelve un iterador de objetos `Path` para los contenidos del directorio. Más flexible, ya que devuelve objetos Path completos.

## Tamaños de Archivos de Directorio (Recorrido Básico)

Para obtener el tamaño total de un directorio (sumando el tamaño de todos sus archivos), necesitas recorrerlo recursivamente.

## Copiar Archivos y Carpetas

El módulo `shutil` (_shell utilities_) es la herramienta estándar de Python para operaciones de alto nivel con archivos y directorios, incluyendo copias.

- `shutil.copy(src, dst)`: Copia el archivo `src` al destino `dst`. `dst` puede ser un directorio (el archivo se copia dentro con su nombre original) o un nombre de archivo (el archivo se copia y se renombra).
- `shutil.copytree(src, dst)`: Copia recursivamente todo un árbol de directorios desde `src` a `dst`. `dst` no debe existir previamente.

## Mover y Renombrar Archivos/Carpetas

- `os.rename(src, dst)`: Renombra un archivo o directorio de `src` a `dst`. Si `dst` ya existe y es del mismo tipo, lo sobrescribe. Si son tipos diferentes (ej. renombrar archivo a directorio), lanza un error.
- `shutil.move(src, dst)`: Mueve un archivo o directorio completo de `src` a `dst`. Similar a renombrar si `dst` está en el mismo sistema de archivos. Si `dst` es un directorio existente, `src` se mueve dentro de él. Si `dst` es un nombre de archivo inexistente, `src` se renombra a `dst`.

## Eliminar Archivos y Carpetas

- `os.remove(ruta_archivo)`: Elimina un archivo. Lanza `FileNotFoundError` si no existe o `IsADirectoryError` si es un directorio.
- `os.rmdir(ruta_directorio)`: Elimina un directorio vacío. Lanza `OSError` si el directorio no está vacío.
- `shutil.rmtree(ruta_directorio)`: Elimina un directorio y todo su contenido recursivamente (**¡Úsalo con precaución!**).
- `Path.unlink()`: Elimina un archivo.
- `Path.rmdir()`: Elimina un directorio vacío.

## Recorrido en Árboles de Directorios (`os.walk()`)

El método `os.walk()` es una herramienta extremadamente potente para recorrer recursivamente un árbol de directorios. Genera tuplas `(ruta_actual, nombres_directorios, nombres_archivos)` para cada directorio en el árbol.

```python
for dirpath, dirnames, filenames in os.walk(directorio_raiz):
    # dirpath: ruta actual del directorio
    # dirnames: lista de nombres de subdirectorios en dirpath
    # filenames: lista de nombres de archivos en dirpath
```

## Lectura y Escritura de Archivos

Esta es la operación más fundamental: interactuar con el contenido de los archivos. El patrón más común es usar la declaración `with open(...) as f:`, que garantiza que el archivo se cierre automáticamente, incluso si ocurren errores.

### Modos de Apertura

- **`'r'` (read):** Solo lectura (por defecto). El archivo debe existir.
- **`'w'` (write):** Solo escritura. Crea el archivo si no existe, lo trunca (vacía) si existe.
- **`'a'` (append):** Añadir (escritura al final). Crea el archivo si no existe.
- **`'x'` (exclusive creation):** Creación exclusiva. Falla si el archivo ya existe.
- `'r+'`: Lectura y escritura.
- `'w+'`: Lectura y escritura (vacía el archivo si existe, lo crea si no).
- `'a+':` Lectura y escritura (escribe al final, lee desde el principio).
- **`'b'` (binary):** Modo binario (para imágenes, etc.). Usar con `rb`, `wb`, etc.
- **`'t'` (text):** Modo texto (por defecto). Usar con `rt`, `wt`, etc.
