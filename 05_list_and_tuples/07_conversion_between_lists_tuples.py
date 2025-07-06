# De lista a tupla
mi_lista_original = [10, 20, 30, 40]
mi_tupla_convertida = tuple(mi_lista_original)
print(f"Lista original: {mi_lista_original}, Tipo: {type(mi_lista_original)}")
print(f"Tupla convertida: {mi_tupla_convertida}, Tipo: {type(mi_tupla_convertida)}")

# De tupla a lista
mi_tupla_original = ("manzana", "banana", "cereza")
mi_lista_convertida = list(mi_tupla_original)
print(f"\nTupla original: {mi_tupla_original}, Tipo: {type(mi_tupla_original)}")
print(f"Lista convertida: {mi_lista_convertida}, Tipo: {type(mi_lista_convertida)}")

# Demostración de mutabilidad después de la conversión
mi_lista_convertida.append("uva")
print(f"Lista después de añadir 'uva': {mi_lista_convertida}") # La lista se puede modificar

# mi_tupla_convertida.append(50) # Esto causaría un AttributeError