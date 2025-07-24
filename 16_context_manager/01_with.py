import os

nombre_archivo = "mi_documento.txt"

print("--- Usando 'with' para manejar archivos ---")

# Sin 'with' (¡No recomendado!)
try:
    f = open(nombre_archivo, "w")
    f.write("Hola, esto se escribe sin 'with'.\n")
    # Si ocurre un error aquí, f.close() nunca se llamaría
finally:
    if f:
        f.close()
print("Archivo escrito sin 'with' (con finally para cerrar).")
os.remove(nombre_archivo) # Limpiar para el siguiente ejemplo

# Con 'with' (¡Recomendado!)
print("\n--- Usando 'with' para una gestión segura ---")
try:
    with open(nombre_archivo, "w") as f:
        f.write("Hola, esto se escribe CON 'with'.\n")
        f.write("El archivo se cerrará automáticamente.\n")
        # Simular un error para ver el efecto del cierre automático
        # raise ValueError("¡Un error simulado!")
    print("Archivo escrito con 'with'.")
except ValueError as e:
    print(f"Error capturado fuera del bloque 'with': {e}")
finally:
    print("El archivo ya debería estar cerrado aquí, gracias a 'with'.")

# Leer el contenido para verificar
if os.path.exists(nombre_archivo):
    with open(nombre_archivo, "r") as f:
        print("\nContenido del archivo (verificando cierre):")
        print(f.read())
    os.remove(nombre_archivo) # Limpiar
    
"""
En este ejemplo, open() devuelve un gestor de contexto, y la declaración with se
asegura de que f.close() sea llamado automáticamente cuando el bloque with 
termina, ya sea que la ejecución sea normal o por una excepción.
"""