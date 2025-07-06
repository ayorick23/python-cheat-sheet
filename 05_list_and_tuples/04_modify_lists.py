# Lista de ejemplo
mi_compras = ["Pan", "Leche", "Huevos"]
print(f"Lista inicial: {mi_compras}") # Salida: ['Pan', 'Leche', 'Huevos']

# append()
mi_compras.append("Arroz")
print(f"Después de append('Arroz'): {mi_compras}") # Salida: ['Pan', 'Leche', 'Huevos', 'Arroz']

# insert()
mi_compras.insert(1, "Queso") # Inserta 'Queso' en el índice 1
print(f"Después de insert(1, 'Queso'): {mi_compras}") # Salida: ['Pan', 'Queso', 'Leche', 'Huevos', 'Arroz']

# del sentencia (por índice)
del mi_compras[0] # Elimina 'Pan'
print(f"Después de del mi_compras[0]: {mi_compras}") # Salida: ['Queso', 'Leche', 'Huevos', 'Arroz']

# del sentencia (por slice)
del mi_compras[2:] # Elimina 'Huevos' y 'Arroz'
print(f"Después de del mi_compras[2:]: {mi_compras}") # Salida: ['Queso', 'Leche']

# remove()
mi_compras.append("Queso") # Añadimos 'Queso' de nuevo para demostrar
print(f"Lista con duplicado: {mi_compras}") # Salida: ['Queso', 'Leche', 'Queso']
mi_compras.remove("Queso") # Elimina la primera aparición de 'Queso'
print(f"Después de remove('Queso'): {mi_compras}") # Salida: ['Leche', 'Queso']

# pop()
ultimo_item = mi_compras.pop() # Elimina y devuelve el último elemento ('Queso')
print(f"Después de pop() (último): {mi_compras}") # Salida: ['Leche']
print(f"Item eliminado con pop(): {ultimo_item}") # Salida: Queso

primer_item = mi_compras.pop(0) # Elimina y devuelve el elemento en el índice 0 ('Leche')
print(f"Después de pop(0): {mi_compras}") # Salida: []
print(f"Item eliminado con pop(0): {primer_item}") # Salida: Leche

# Manejo de errores con remove (si el elemento no existe)
try:
    mi_compras.remove("Tomate")
except ValueError as e:
    print(f"Error al usar remove(): {e}") # Salida: ValueError: list.remove(x): x not in list