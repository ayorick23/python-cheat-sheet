# Lambda simple: Sumar dos números
sumar_lambda = lambda a, b: a + b
print(f"Suma con lambda (5, 3): {sumar_lambda(5, 3)}") # Salida: 8

# Lambda para verificar si un número es par
es_par = lambda x: x % 2 == 0
print(f"¿Es 4 par? {es_par(4)}") # Salida: True
print(f"¿Es 7 par? {es_par(7)}") # Salida: False

# Usando lambda con la función filter()
# filter() filtra elementos de un iterable basándose en una función.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda num: num % 2 == 0, numeros))
print(f"Números pares de {numeros}: {pares}") # Salida: [2, 4, 6, 8, 10]

# Usando lambda con la función map()
# map() aplica una función a cada elemento de un iterable.
cuadrados = list(map(lambda num: num ** 2, numeros))
print(f"Cuadrados de los números: {cuadrados}") # Salida: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Usando lambda con la función sorted() para ordenar por un criterio específico
estudiantes = [
    {"nombre": "Juan", "edad": 20, "nota": 85},
    {"nombre": "Maria", "edad": 22, "nota": 92},
    {"nombre": "Pedro", "edad": 19, "nota": 78}
]

# Ordenar por edad
estudiantes_por_edad = sorted(estudiantes, key=lambda est: est['edad'])
print("\nEstudiantes ordenados por edad:")
for est in estudiantes_por_edad:
    print(est)

# Ordenar por nota (descendente)
estudiantes_por_nota = sorted(estudiantes, key=lambda est: est['nota'], reverse=True)
print("\nEstudiantes ordenados por nota (descendente):")
for est in estudiantes_por_nota:
    print(est)