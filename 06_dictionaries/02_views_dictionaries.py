# Diccionario de ejemplo
inventario = {
    "manzanas": 50,
    "peras": 30,
    "uvas": 40,
    "bananas": 60
}

# Obtener las claves
claves = inventario.keys()
print(f"Claves del inventario: {claves}") # Salida: dict_keys(['manzanas', 'peras', 'uvas', 'bananas'])

# Obtener los valores
valores = inventario.values()
print(f"Valores del inventario: {valores}") # Salida: dict_values([50, 30, 40, 60])

# Obtener los pares clave-valor
items = inventario.items()
print(f"Items del inventario: {items}") # Salida: dict_items([('manzanas', 50), ('peras', 30), ('uvas', 40), ('bananas', 60)])

# Demostración de que son vistas dinámicas
inventario["naranjas"] = 25 # Añadimos un nuevo elemento
print(f"\nDespués de añadir 'naranjas':")
print(f"Claves actualizadas: {claves}")
print(f"Valores actualizados: {valores}")
print(f"Items actualizados: {items}")

# Puedes convertir las vistas a listas si necesitas una copia estática
lista_claves = list(inventario.keys())
lista_valores = list(inventario.values())
lista_items = list(inventario.items())

print(f"\nClaves como lista: {lista_claves}")
print(f"Valores como lista: {lista_valores}")
print(f"Items como lista: {lista_items}")