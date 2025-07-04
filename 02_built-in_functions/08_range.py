# range(stop) - Genera números desde 0 hasta stop - 1
print("Números del 0 al 4:")
for i in range(5):
    print(i, end=" ") # Salida: 0 1 2 3 4
print("\n---")

# range(start, stop) - Genera números desde start hasta stop-1
print("Números del 3 al 7:")
for i in range(3, 8):
    print(i, end=" ") # Salida: 3 4 5 6 7
print("\n---")

# range(start, stop, step) - Genera números con un incremento específico
print("Números pares del 2 al 10:")
for i in range(2, 11, 2):
    print(i, end=" ") # Salida: 2 4 6 8 10
print("\n---")

# range con paso negativo (para contar hacia atrás)
print("Números del 10 al 1 (descendente):")
for i in range(10, 0, -1):
    print(i, end=" ") # Salida: 10 9 8 7 6 5 4 3 2 1
print("\n---")

# Convertir un rango a una lista para ver sus elementos (no recomendado para rangos muy grandes)
lista_rango = list(range(1, 6))
print(f"Lista de range(1, 6): {lista_rango}") # Salida: [1, 2, 3, 4, 5]