# Operadores de Pertenencia
# Se utilizan para verificar si un valor o una variable se encuentra en una secuencia (string, list, tuple, set, dictionary).

mi_lista = [1, 2, 3, 4, 5]
mi_cadena = "Hola Python"
mi_diccionario = {"nombre": "Juan", "edad": 30}

# in
print(f"¿3 está en mi_lista? {3 in mi_lista}")      # Salida: ¿3 está en mi_lista? True
print(f"¿6 está en mi_lista? {6 in mi_lista}")      # Salida: ¿6 está en mi_lista? False

print(f"¿'Python' está en mi_cadena? {'Python' in mi_cadena}") # Salida: ¿'Python' está en mi_cadena? True
print(f"¿'Java' está en mi_cadena? {'Java' in mi_cadena}")     # Salida: ¿'Java' está en mi_cadena? False

print(f"¿'nombre' está en mi_diccionario? {'nombre' in mi_diccionario}") # Salida: ¿'nombre' está en mi_diccionario? True
print(f"¿'Juan' está en mi_diccionario? {'Juan' in mi_diccionario}")     # Salida: ¿'Juan' está en mi_diccionario? False (solo busca claves)

# not in
print(f"¿6 no está en mi_lista? {6 not in mi_lista}")    # Salida: ¿6 no está en mi_lista? True
print(f"¿'Java' no está en mi_cadena? {'Java' not in mi_cadena}") # Salida: ¿'Java' no está en mi_cadena? True