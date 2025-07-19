import json
import os

# --- Simular un archivo JSON ---
json_data_file = """
{
    "nombre": "Alice",
    "edad": 30,
    "ciudad": "Nueva York",
    "intereses": ["programacion", "lectura", "senderismo"],
    "es_estudiante": false,
    "calificaciones": null
}
"""
with open("datos_ejemplo.json", "w") as f:
    f.write(json_data_file)

# --- Usando json.load() para leer desde un archivo ---
print("--- Leyendo desde archivo (json.load) ---")
try:
    with open("datos_ejemplo.json", "r") as f:
        datos_cargados = json.load(f)
        print(f"Tipo de datos cargados: {type(datos_cargados)}")
        print(f"Nombre: {datos_cargados['nombre']}")
        print(f"Intereses: {datos_cargados['intereses'][0]}")
except FileNotFoundError:
    print("El archivo 'datos_ejemplo.json' no se encontró.")
except json.JSONDecodeError as e:
    print(f"Error al decodificar JSON desde el archivo: {e}")

# --- Usando json.loads() para leer desde una cadena ---
print("\n--- Leyendo desde cadena (json.loads) ---")
json_string = '{"producto": "Laptop", "precio": 1200.50, "disponible": true}'
datos_desde_string = json.loads(json_string)
print(f"Tipo de datos desde cadena: {type(datos_desde_string)}")
print(f"Producto: {datos_desde_string['producto']}")

# Limpieza
os.remove("datos_ejemplo.json")