import os
from pathlib import Path

# Crear un archivo de prueba con contenido
nombre_archivo = "mi_documento.txt"
contenido = "Este es un texto de prueba para calcular su tamaño."
with open(nombre_archivo, "w") as f:
    f.write(contenido)

# Obtener tamaño con os.path.getsize()
tamano_os = os.path.getsize(nombre_archivo)
print(f"Tamaño de '{nombre_archivo}' (os): {tamano_os} bytes")

# Obtener tamaño con pathlib.Path.stat().st_size
path_archivo = Path(nombre_archivo)
tamano_pathlib = path_archivo.stat().st_size
print(f"Tamaño de '{nombre_archivo}' (pathlib): {tamano_pathlib} bytes")

# Limpieza
os.remove(nombre_archivo)