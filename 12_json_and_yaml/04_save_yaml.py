import yaml
import os

# Objeto Python a serializar
datos_producto = {
    "producto": {
        "nombre": "Smartphone X",
        "marca": "GlobalTech",
        "especificaciones": {
            "pantalla": "6.1 pulgadas",
            "ram": "8GB",
            "almacenamiento": "128GB"
        },
        "precio": 799.99,
        "en_stock": True
    },
    "proveedor": "Distribuidor ABC"
}

# --- Usando yaml.dump() para escribir a un archivo ---
print("--- Escribiendo a archivo (yaml.dump) ---")
with open("producto.yaml", "w") as f:
    yaml.dump(datos_producto, f, default_flow_style=False, sort_keys=False) # sort_keys=False para mantener orden de claves
print("Datos escritos en 'producto.yaml'.")

# Verificar el contenido del archivo
with open("producto.yaml", "r") as f:
    print("\nContenido de 'producto.yaml':")
    print(f.read())

# --- Usando yaml.dump() para obtener una cadena YAML ---
print("\n--- Obteniendo cadena YAML (yaml.dump) ---")
cadena_yaml = yaml.dump(datos_producto, default_flow_style=False, sort_keys=False)
print("Cadena YAML generada:")
print(cadena_yaml)

# Limpieza
os.remove("producto.yaml")