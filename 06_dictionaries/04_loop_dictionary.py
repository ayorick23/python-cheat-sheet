# Diccionario de ejemplo
productos = {
    "laptop": 1200,
    "teclado": 75,
    "mouse": 30,
    "monitor": 300
}

# Iterar por defecto (sobre las claves)
print("--- Iterando sobre las claves (por defecto) ---")
for producto in productos:
    print(f"Producto: {producto}")
# Salida: laptop, teclado, mouse, monitor

# Iterar explícitamente sobre las claves con .keys()
print("\n--- Iterando sobre las claves con .keys() ---")
for clave in productos.keys():
    print(f"Clave: {clave}")

# Iterar sobre los valores con .values()
print("\n--- Iterando sobre los valores con .values() ---")
for precio in productos.values():
    print(f"Precio: ${precio}")

# Iterar sobre los pares clave-valor con .items() (recomendado)
print("\n--- Iterando sobre pares clave-valor con .items() ---")
for producto, precio in productos.items():
    print(f"{producto.capitalize()}: ${precio}")
# Salida:
# Laptop: $1200
# Teclado: $75
# Mouse: $30
# Monitor: $300