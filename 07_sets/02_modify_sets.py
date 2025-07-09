# Set de ejemplo
frutas = {"manzana", "banana", "cereza"}
print(f"Conjunto inicial de frutas: {frutas}")

# add()
frutas.add("naranja")
print(f"Después de add('naranja'): {frutas}") # Salida: {'manzana', 'banana', 'cereza', 'naranja'} (orden desordenado)

frutas.add("manzana") # No añade nada porque 'manzana' ya existe
print(f"Después de add('manzana') de nuevo: {frutas}") # No cambia

# update()
nuevas_frutas = ["kiwi", "mango", "banana"]
frutas.update(nuevas_frutas) # 'banana' se ignora por ser duplicado
print(f"Después de update(['kiwi', 'mango', 'banana']): {frutas}") # Salida: {'manzana', 'cereza', 'kiwi', 'banana', 'mango', 'naranja'}

# remove()
frutas.remove("cereza")
print(f"Después de remove('cereza'): {frutas}")

try:
    frutas.remove("uva") # 'uva' no existe, esto lanzará un KeyError
except KeyError as e:
    print(f"Error al intentar remove('uva'): {e}")

# discard()
frutas.discard("mango")
print(f"Después de discard('mango'): {frutas}")

frutas.discard("pera") # 'pera' no existe, pero no lanza error
print(f"Después de discard('pera') (inexistente): {frutas}")

# Otros métodos de eliminación (similares a diccionarios)
# set.pop() - Elimina y devuelve un elemento arbitrario (KeyError si está vacío)
# set.clear() - Elimina todos los elementos del conjunto
conjunto_temp = {1, 2, 3}
elemento_sacado = conjunto_temp.pop()
print(f"Elemento sacado con pop(): {elemento_sacado}, Conjunto restante: {conjunto_temp}")

conjunto_temp.clear()
print(f"Conjunto después de clear(): {conjunto_temp}")