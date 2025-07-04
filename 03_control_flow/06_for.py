# Iterar sobre una lista
print("--- Iterando sobre una lista ---")
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(f"Me gusta la {fruta}.")

# Iterar sobre una cadena de texto
print("\n--- Iterando sobre una cadena ---")
palabra = "Python"
for letra in palabra:
    print(f"Letra: {letra}")

# Iterar sobre una tupla
print("\n--- Iterando sobre una tupla ---")
coordenadas = (10, 20, 30)
for coordenada in coordenadas:
    print(f"Coordenada: {coordenada}")

# Iterar sobre un diccionario (por defecto, itera sobre las claves)
print("\n--- Iterando sobre un diccionario (claves) ---")
persona = {"nombre": "Maria", "edad": 28, "ciudad": "Madrid"}
for clave in persona:
    print(f"Clave: {clave}, Valor: {persona[clave]}")

# Iterar sobre los valores de un diccionario
print("\n--- Iterando sobre los valores de un diccionario ---")
for valor in persona.values():
    print(f"Valor: {valor}")

# Iterar sobre los pares clave-valor de un diccionario
print("\n--- Iterando sobre clave-valor de un diccionario ---")
for clave, valor in persona.items():
    print(f"{clave.capitalize()}: {valor}")

# Iterar sobre un conjunto
print("\n--- Iterando sobre un conjunto ---")
colores = {"rojo", "verde", "azul", "rojo"}
for color in colores:
    print(f"Color: {color}")