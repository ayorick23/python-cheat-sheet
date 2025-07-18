import os
from pathlib import Path

# Crear una estructura de prueba compleja
base_dir = "arbol_ejemplo"
os.makedirs(os.path.join(base_dir, "carpetaA/subA1"), exist_ok=True)
os.makedirs(os.path.join(base_dir, "carpetaB"), exist_ok=True)
with open(os.path.join(base_dir, "file1.txt"), "w") as f: f.write("1")
with open(os.path.join(base_dir, "carpetaA", "file2.txt"), "w") as f: f.write("2")
with open(os.path.join(base_dir, "carpetaA", "subA1", "file3.log"), "w") as f: f.write("3")
with open(os.path.join(base_dir, "carpetaB", "file4.csv"), "w") as f: f.write("4")

print(f"--- Recorrido del árbol de '{base_dir}' con os.walk() ---")
for root, dirs, files in os.walk(base_dir):
    nivel = root.replace(base_dir, '').count(os.sep)
    indent = ' ' * 4 * (nivel)
    print(f'{indent}[D] {os.path.basename(root)}/')
    subindent = ' ' * 4 * (nivel + 1)
    for d in dirs:
        print(f'{subindent}[D] {d}/')
    for f in files:
        print(f'{subindent}[F] {f}')

# Ejemplo de uso: buscar archivos por extensión
print("\n--- Archivos .txt encontrados ---")
for root, _, files in os.walk(base_dir):
    for filename in files:
        if filename.endswith(".txt"):
            print(os.path.join(root, filename))

# Limpieza
import shutil
shutil.rmtree(base_dir)