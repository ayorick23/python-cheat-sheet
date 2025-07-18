import os
from pathlib import Path

# Crear un archivo y una carpeta de prueba
if not os.path.exists("test_dir"):
    os.mkdir("test_dir")
with open("test_file.txt", "w") as f:
    f.write("Hola mundo")

print("--- Validación con os.path ---")
print(f"¿'test_dir' existe? {os.path.exists('test_dir')}")       # Salida: True
print(f"¿'test_dir' es archivo? {os.path.isfile('test_dir')}")   # Salida: False
print(f"¿'test_dir' es directorio? {os.path.isdir('test_dir')}") # Salida: True

print(f"¿'test_file.txt' existe? {os.path.exists('test_file.txt')}") # Salida: True
print(f"¿'test_file.txt' es archivo? {os.path.isfile('test_file.txt')}") # Salida: True
print(f"¿'test_file.txt' es directorio? {os.path.isdir('test_file.txt')}") # Salida: False

print(f"¿'ruta_inexistente.txt' existe? {os.path.exists('ruta_inexistente.txt')}") # Salida: False

print("\n--- Validación con pathlib.Path ---")
path_dir = Path("test_dir")
path_file = Path("test_file.txt")
path_inexistente = Path("ruta_inexistente_pb.txt")

print(f"¿'{path_dir}' existe? {path_dir.exists()}")
print(f"¿'{path_dir}' es archivo? {path_dir.is_file()}")
print(f"¿'{path_dir}' es directorio? {path_dir.is_dir()}")

print(f"¿'{path_file}' existe? {path_file.exists()}")
print(f"¿'{path_file}' es archivo? {path_file.is_file()}")
print(f"¿'{path_file}' es directorio? {path_file.is_dir()}")

print(f"¿'{path_inexistente}' existe? {path_inexistente.exists()}")

# Limpieza
os.remove("test_file.txt")
os.rmdir("test_dir")