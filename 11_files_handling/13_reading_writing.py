import os

nombre_archivo = "mi_data.txt"

# Escritura de un archivo (modo 'w')
with open(nombre_archivo, "w") as f:
    f.write("Esta es la primera línea.\n")
    f.write("Esta es la segunda línea.\n")
    f.write("Y esta es la tercera.")
print(f"'{nombre_archivo}' ha sido creado y escrito.")

# Lectura de un archivo completo (modo 'r')
with open(nombre_archivo, "r") as f:
    contenido = f.read()
print("\n--- Contenido completo ---")
print(contenido)

# Lectura línea por línea (modo 'r')
print("\n--- Contenido línea por línea ---")
with open(nombre_archivo, "r") as f:
    for linea in f:
        print(linea.strip()) # .strip() para eliminar el salto de línea al final de cada línea

# Añadir contenido a un archivo existente (modo 'a')
with open(nombre_archivo, "a") as f:
    f.write("\nEsta es una nueva línea añadida.")
print(f"\nSe ha añadido una línea a '{nombre_archivo}'.")

# Leer después de añadir
with open(nombre_archivo, "r") as f:
    contenido_actualizado = f.read()
print("\n--- Contenido actualizado ---")
print(contenido_actualizado)

# Ejemplo de escritura y lectura binaria
nombre_archivo_bin = "imagen.png" # No lo crearemos, solo simulamos
try:
    with open(nombre_archivo_bin, "wb") as f:
        # En un escenario real, f.write(datos_binarios)
        print(f"Simulando escritura binaria en '{nombre_archivo_bin}'.")

    with open(nombre_archivo_bin, "rb") as f:
        # En un escenario real, datos = f.read()
        print(f"Simulando lectura binaria de '{nombre_archivo_bin}'.")
except FileNotFoundError:
    print(f"El archivo '{nombre_archivo_bin}' no existe para leer/escribir.")

# Limpieza
os.remove(nombre_archivo)
# if os.path.exists(nombre_archivo_bin):
#     os.remove(nombre_archivo_bin)