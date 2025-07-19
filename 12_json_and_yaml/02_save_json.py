# ejemplo_json_guarda.py
import json
import os

# Objeto Python a serializar
mi_diccionario = {
    "empresa": "TechCorp",
    "empleados": [
        {"id": 1, "nombre": "Carlos", "cargo": "Ingeniero"},
        {"id": 2, "nombre": "Lucía", "cargo": "Diseñadora"}
    ],
    "activo": True
}

# --- Usando json.dump() para escribir a un archivo ---
print("--- Escribiendo a archivo (json.dump) ---")
with open("empresa.json", "w") as f:
    json.dump(mi_diccionario, f, indent=4) # indent=4 para una salida bonita
print("Datos escritos en 'empresa.json'.")

# Verificar el contenido del archivo
with open("empresa.json", "r") as f:
    print("\nContenido de 'empresa.json':")
    print(f.read())

# --- Usando json.dumps() para obtener una cadena JSON ---
print("\n--- Obteniendo cadena JSON (json.dumps) ---")
cadena_json = json.dumps(mi_diccionario, indent=2)
print("Cadena JSON generada:")
print(cadena_json)

# Limpieza
os.remove("empresa.json")