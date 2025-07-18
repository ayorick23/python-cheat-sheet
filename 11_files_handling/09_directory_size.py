# ejemplo_tamano_directorio.py
import os
from pathlib import Path

# Crear una estructura de prueba con archivos de diferentes tamaños
os.makedirs("size_test_dir/nested_dir", exist_ok=True)
with open("size_test_dir/file_a.txt", "w") as f: f.write("a" * 100) # 100 bytes
with open("size_test_dir/file_b.txt", "w") as f: f.write("b" * 50)  # 50 bytes
with open("size_test_dir/nested_dir/file_c.txt", "w") as f: f.write("c" * 200) # 200 bytes

def get_directory_size(path):
    total_size = 0
    # Usamos os.walk para recorrer el árbol de directorios
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # Asegurarse de que no estamos siguiendo enlaces simbólicos que podrían causar un bucle infinito
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size

def get_directory_size_pathlib(path_obj):
    total_size = 0
    for item in path_obj.rglob('*'): # rglob para búsqueda recursiva
        if item.is_file():
            total_size += item.stat().st_size
    return total_size

dir_to_check = "size_test_dir"
print(f"Tamaño total de '{dir_to_check}' (os.walk): {get_directory_size(dir_to_check)} bytes")

dir_pathlib_to_check = Path("size_test_dir")
print(f"Tamaño total de '{dir_pathlib_to_check}' (pathlib.rglob): {get_directory_size_pathlib(dir_pathlib_to_check)} bytes")

# Limpieza
import shutil
shutil.rmtree("size_test_dir")