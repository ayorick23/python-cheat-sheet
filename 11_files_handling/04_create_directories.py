import os
from pathlib import Path

# Crear un directorio simple con os.mkdir()
try:
    os.mkdir("NuevaCarpetaOs")
    print("Carpeta 'NuevaCarpetaOs' creada.")
except FileExistsError:
    print("Carpeta 'NuevaCarpetaOs' ya existe.")

# Crear directorios anidados con os.makedirs()
ruta_anidada_os = os.path.join("CarpetaPrincipalOs", "SubCarpetaOs")
os.makedirs(ruta_anidada_os, exist_ok=True)
print(f"Ruta anidada '{ruta_anidada_os}' creada (con exist_ok=True).")

# Crear directorios con pathlib
ruta_anidada_pathlib = Path("CarpetaPrincipalPathlib") / "SubCarpetaPathlib"
ruta_anidada_pathlib.mkdir(parents=True, exist_ok=True)
print(f"Ruta anidada '{ruta_anidada_pathlib}' creada (con parents=True, exist_ok=True).")

# Limpieza (opcional, para ejecutar el script varias veces sin problemas)
# os.rmdir("NuevaCarpetaOs") # Solo si está vacía
# os.rmdir(ruta_anidada_os) # Solo si está vacía, no recursiva
# import shutil
# shutil.rmtree("CarpetaPrincipalOs") # Elimina recursivamente
# shutil.rmtree("CarpetaPrincipalPathlib")