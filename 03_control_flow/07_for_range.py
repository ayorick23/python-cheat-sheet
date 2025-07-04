# Bucle for con range(stop) - de 0 hasta stop-1
print("--- Bucle for con range(5) ---")
for i in range(5):
    print(f"Número: {i}") # Salida: 0, 1, 2, 3, 4

# Bucle for con range(start, stop) - de start hasta stop-1
print("\n--- Bucle for con range(2, 7) ---")
for i in range(2, 7):
    print(f"Número: {i}") # Salida: 2, 3, 4, 5, 6

# Bucle for con range(start, stop, step) - con paso personalizado
print("\n--- Bucle for con range(1, 10, 2) (números impares) ---")
for i in range(1, 10, 2):
    print(f"Número impar: {i}") # Salida: 1, 3, 5, 7, 9

# Bucle for para contar hacia atrás
print("\n--- Bucle for contando hacia atrás con range(10, 0, -1) ---")
for i in range(10, 0, -1):
    print(f"Cuenta atrás: {i}") # Salida: 10, 9, ..., 1

# Usando for con range y break/continue
print("\n--- Bucle for con break y continue ---")
for i in range(10):
    if i % 2 != 0: # Si es impar
        continue # Salta la iteración actual
    if i > 6:
        break # Sale del bucle si es mayor a 6

    print(f"Número par menor o igual a 6: {i}")
# Salida:
# Número par menor o igual a 6: 0
# Número par menor o igual a 6: 2
# Número par menor o igual a 6: 4
# Número par menor o igual a 6: 6