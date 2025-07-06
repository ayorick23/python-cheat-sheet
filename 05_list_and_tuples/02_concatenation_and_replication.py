# Listas de ejemplo
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

# Concatenación
lista_concatenada = lista1 + lista2
print(f"Lista concatenada: {lista_concatenada}") # Salida: [1, 2, 3, 4, 5, 6]

lista3 = ["a", "b"]
lista4 = ["c"]
nueva_lista = lista3 + lista4 + lista1
print(f"Múltiple concatenación: {nueva_lista}") # Salida: ['a', 'b', 'c', 1, 2, 3]

# Replicación
lista_replicada = [0] * 5
print(f"Lista replicada (cinco ceros): {lista_replicada}") # Salida: [0, 0, 0, 0, 0]

# Cuidado con objetos mutables anidados en la replicación
# La replicación crea múltiples referencias al MISMO objeto para objetos mutables
lista_anidada = [[0, 0]] * 3
print(f"Lista anidada replicada: {lista_anidada}") # Salida: [[0, 0], [0, 0], [0, 0]]
lista_anidada[0][0] = 99
print(f"Después de modificar un elemento anidado: {lista_anidada}") # Salida: [[99, 0], [99, 0], [99, 0]]
# ¡Todos los sub-listas fueron modificadas porque eran la misma referencia!

# Para replicar objetos mutables de forma independiente, usa una comprensión de lista
lista_anidada_correcta = [[0, 0] for _ in range(3)]
print(f"Lista anidada correcta: {lista_anidada_correcta}") # Salida: [[0, 0], [0, 0], [0, 0]]
lista_anidada_correcta[0][0] = 99
print(f"Después de modificar un elemento anidado (correcto): {lista_anidada_correcta}") # Salida: [[99, 0], [0, 0], [0, 0]]