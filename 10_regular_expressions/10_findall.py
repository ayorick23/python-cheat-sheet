import re

texto = "Los números son 123 y 456, también 789."

# Encontrar todos los números
numeros = re.findall(r'\d+', texto)
print(f"Todos los números encontrados: {numeros}") # Salida: ['123', '456', '789']

# Encontrar todas las palabras de 3 letras
palabras_3_letras = re.findall(r'\b\w{3}\b', texto) # \b es un límite de palabra
print(f"Palabras de 3 letras: {palabras_3_letras}") # Salida: ['Los', 'son', '123', '456', '789'] (Cuidado, "Los" y "son" también tienen 3 letras)