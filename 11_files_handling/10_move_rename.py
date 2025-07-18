import os
import shutil
from pathlib import Path

# Preparar entorno de prueba
os.makedirs("temp_mover", exist_ok=True)
with open("temp_mover/archivo_a_renombrar.txt", "w") as f: f.write("Contenido.")
os.mkdir("temp_mover/carpeta_a_renombrar")
with open("temp_mover/archivo_a_mover.txt", "w") as f: f.write("Mover este.")

# Renombrar un archivo con os.rename()
os.rename("temp_mover/archivo_a_renombrar.txt", "temp_mover/archivo_renombrado.txt")
print("Archivo 'archivo_a_renombrar.txt' renombrado a 'archivo_renombrado.txt'.")

# Renombrar una carpeta con os.rename()
os.rename("temp_mover/carpeta_a_renombrar", "temp_mover/nueva_carpeta_renombrada")
print("Carpeta 'carpeta_a_renombrar' renombrada a 'nueva_carpeta_renombrada'.")

# Mover un archivo a otra carpeta con shutil.move()
os.makedirs("destino_mover", exist_ok=True)
shutil.move("temp_mover/archivo_a_mover.txt", "destino_mover/archivo_movido.txt")
print("Archivo 'archivo_a_mover.txt' movido a 'destino_mover/archivo_movido.txt'.")

# Mover una carpeta completa con shutil.move()
# Necesitamos crear una nueva carpeta para mover
os.makedirs("otra_fuente_para_mover", exist_ok=True)
with open("otra_fuente_para_mover/file.txt", "w") as f: f.write("x")
shutil.move("otra_fuente_para_mover", "destino_mover/carpeta_movida")
print("Carpeta 'otra_fuente_para_mover' movida a 'destino_mover/carpeta_movida'.")

# Limpieza
shutil.rmtree("temp_mover")
shutil.rmtree("destino_mover")