import os
from pathlib import Path

# Usando os
directorio_os = os.getcwd()
print(f"Directorio actual (os): {directorio_os}")

# Usando pathlib
directorio_pathlib = Path.cwd()
print(f"Directorio actual (pathlib): {directorio_pathlib}")

# Puedes combinarlo con os.path.join para crear rutas absolutas
ruta_absoluta_os = os.path.join(directorio_os, 'mi_archivo_absoluto.txt')
print(f"Ruta absoluta (os): {ruta_absoluta_os}")

# Puedes combinarlo con el operador / para crear rutas absolutas
ruta_absoluta_pathlib = directorio_pathlib / 'mi_archivo_absoluto_pathlib.txt'
print(f"Ruta absoluta (pathlib): {ruta_absoluta_pathlib}")