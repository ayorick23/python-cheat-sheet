# Crear una lista de cuadrados
numeros = [1, 2, 3, 4, 5]
cuadrados = [numero**2 for numero in numeros]
print(cuadrados)  # Salida: [1, 4, 9, 16, 25]

# Crear una lista de strings en mayúsculas
palabras = ["hola", "mundo", "python"]
mayusculas = [palabra.upper() for palabra in palabras]
print(mayusculas)  # Salida: ['HOLA', 'MUNDO', 'PYTHON']

# Filtrar números pares
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)  # Salida: [2, 4, 6, 8, 10]

# Combinar iterables
letras = ["a", "b", "c"]
numeros = [1, 2, 3]
combinados = [(letra, numero) for letra in letras for numero in numeros]
print(combinados)
# Salida: [('a', 1), ('a', 2), ('a', 3), ('b', 1), ('b', 2), ('b', 3), ('c', 1), ('c', 2), ('c', 3)]