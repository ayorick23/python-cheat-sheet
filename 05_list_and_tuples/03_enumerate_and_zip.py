# Listas de ejemplo
nombres = ["Alice", "Bob", "Charlie", "David"]
edades = [30, 24, 35, 29]
ciudades = ["Nueva York", "Londres", "París", "Berlín"]

# Uso de enumerate
print("--- Usando enumerate ---")
for i, nombre in enumerate(nombres):
    print(f"Índice {i}: {nombre}")
# Salida:
# Índice 0: Alice
# Índice 1: Bob
# Índice 2: Charlie
# Índice 3: David

# enumerate con un índice inicial diferente
print("\n--- Usando enumerate con índice inicial 1 ---")
for i, nombre in enumerate(nombres, start=1):
    print(f"N.º {i}: {nombre}")

# Uso de zip
print("\n--- Usando zip para emparejar nombres y edades ---")
for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años.")
# Salida:
# Alice tiene 30 años.
# Bob tiene 24 años.
# Charlie tiene 35 años.
# David tiene 29 años.

# Usando zip con tres listas
print("\n--- Usando zip con nombres, edades y ciudades ---")
for nombre, edad, ciudad in zip(nombres, edades, ciudades):
    print(f"{nombre} ({edad} años) vive en {ciudad}.")

# Cuidado con zip si las listas tienen longitudes diferentes
print("\n--- zip con listas de diferentes longitudes (se detiene en la más corta) ---")
numeros1 = [1, 2, 3]
numeros2 = [10, 20, 30, 40]
for n1, n2 in zip(numeros1, numeros2):
    print(f"{n1} y {n2}")
# Salida:
# 1 y 10
# 2 y 20
# 3 y 30