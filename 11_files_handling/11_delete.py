import os
import shutil
from pathlib import Path

# Preparar entorno de prueba
os.makedirs("temp_eliminar/sub", exist_ok=True)
with open("temp_eliminar/archivo_para_eliminar.txt", "w") as f: f.write("Contenido.")
with open("temp_eliminar/sub/archivo_sub.txt", "w") as f: f.write("Contenido.")
os.mkdir("temp_eliminar/carpeta_vacia")

# Eliminar un archivo con os.remove()
os.remove("temp_eliminar/archivo_para_eliminar.txt")
print("Archivo 'archivo_para_eliminar.txt' eliminado.")

# Eliminar una carpeta vacía con os.rmdir()
os.rmdir("temp_eliminar/carpeta_vacia")
print("Carpeta 'carpeta_vacia' eliminada.")

# Intentar eliminar una carpeta no vacía con os.rmdir() (fallará)
try:
    os.rmdir("temp_eliminar")
except OSError as e:
    print(f"Error al intentar eliminar 'temp_eliminar' con os.rmdir(): {e}") # No está vacía

# Eliminar una carpeta no vacía recursivamente con shutil.rmtree()
shutil.rmtree("temp_eliminar")
print("Carpeta 'temp_eliminar' y su contenido eliminados recursivamente con shutil.rmtree().")

# Ejemplo con pathlib
path_file_pb = Path("archivo_pb.txt")
path_dir_pb = Path("dir_vacio_pb")
path_dir_pb.mkdir(exist_ok=True)
path_file_pb.touch() # Crea un archivo vacío

path_file_pb.unlink()
print(f"Archivo '{path_file_pb}' eliminado con unlink().")
path_dir_pb.rmdir()
print(f"Directorio '{path_dir_pb}' eliminado con rmdir().")