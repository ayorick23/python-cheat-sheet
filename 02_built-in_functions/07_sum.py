# Sumar los elementos de una lista
numeros_enteros = [1, 2, 3, 4, 5]
suma_total = sum(numeros_enteros)
print(f"La suma de {numeros_enteros} es: {suma_total}") # Salida: 15

# Sumar los elementos de una tupla con un valor inicial
numeros_flotantes = (1.5, 2.5, 3.0)
suma_con_inicio = sum(numeros_flotantes, 10.0)
print(f"La suma de {numeros_flotantes} con inicio 10.0 es: {suma_con_inicio}") # Salida: 17.0

# Sumar un rango de números
suma_rango = sum(range(1, 10)) # Suma los números del 1 al 9
print(f"La suma de los números del 1 al 9 es: {suma_rango}") # Salida: 45

# Error si el iterable contiene tipos no numéricos
# lista_mixta = [1, 2, "tres"]
# print(sum(lista_mixta)) # Esto lanzaría un TypeError