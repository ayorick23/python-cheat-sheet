# Listas de ejemplo
numeros = [3, 1, 4, 1, 5, 9, 2, 6]
palabras = ["banana", "apple", "cherry", "date"]

print(f"Números originales: {numeros}")
print(f"Palabras originales: {palabras}")

# list.sort() (modifica la lista original)
numeros.sort()
print(f"Números ordenados con .sort(): {numeros}") # Salida: [1, 1, 2, 3, 4, 5, 6, 9]

palabras.sort(reverse=True) # Orden descendente
print(f"Palabras ordenadas descendente con .sort(): {palabras}") # Salida: ['date', 'cherry', 'banana', 'apple']

# sorted() (crea una nueva lista)
copia_numeros = [3, 1, 4, 1, 5, 9, 2, 6]
numeros_ordenados_copia = sorted(copia_numeros)
print(f"Números originales después de sorted(): {copia_numeros}") # Salida: [3, 1, 4, 1, 5, 9, 2, 6] (sin cambios)
print(f"Nueva lista ordenada con sorted(): {numeros_ordenados_copia}") # Salida: [1, 1, 2, 3, 4, 5, 6, 9]

# Ordenar listas de diccionarios usando 'key' y lambda
estudiantes = [
    {"nombre": "Carlos", "edad": 25, "nota": 90},
    {"nombre": "Andrea", "edad": 22, "nota": 88},
    {"nombre": "Benito", "edad": 28, "nota": 95}
]

# Ordenar por 'nota' de forma ascendente
estudiantes_por_nota = sorted(estudiantes, key=lambda est: est['nota'])
print("\nEstudiantes ordenados por nota:")
for est in estudiantes_por_nota:
    print(est)

# Ordenar por 'nombre' de forma descendente
estudiantes_por_nombre = sorted(estudiantes, key=lambda est: est['nombre'], reverse=True)
print("\nEstudiantes ordenados por nombre (descendente):")
for est in estudiantes_por_nombre:
    print(est)