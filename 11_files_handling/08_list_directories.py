import os
from pathlib import Path

# Crear una estructura de prueba
os.makedirs("list_test_dir/subdir1", exist_ok=True)
os.makedirs("list_test_dir/subdir2", exist_ok=True)
with open("list_test_dir/file1.txt", "w") as f: pass
with open("list_test_dir/file2.py", "w") as f: pass

print("--- Listado con os.listdir() ---")
contenido_os = os.listdir("list_test_dir")
print(f"Contenido de 'list_test_dir': {contenido_os}")
# Nota: el orden puede variar, y solo da los nombres, no las rutas completas

print("\n--- Listado con pathlib.Path.iterdir() ---")
path_dir = Path("list_test_dir")
print(f"Contenido de '{path_dir}':")
for item in path_dir.iterdir():
    print(f"- {item} (Es directorio: {item.is_dir()}, Es archivo: {item.is_file()})")
    # item es un objeto Path, puedes usar sus métodos directamente (ej. item.name, item.suffix)

# Limpieza
import shutil
shutil.rmtree("list_test_dir")