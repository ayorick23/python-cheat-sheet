import re

texto = "Hola 123 Mundo 456."

# Coincidir con cualquier vocal
vocales = re.findall(r'[aeiouAEIOU]', texto)
print(f"Vocales encontradas: {vocales}") # Salida: ['o', 'a', 'o', 'u']

# Coincidir con caracteres específicos o rangos
caracteres_especiales = re.findall(r'[!@#$%^&*()]', "Mi email es test@example.com!")
print(f"Caracteres especiales: {caracteres_especiales}") # Salida: ['@', '!']

# Negación de una clase de caracteres
# Coincide con cualquier carácter que NO sea un dígito
no_digitos = re.findall(r'[^0-9]', texto)
print(f"Caracteres no dígitos: {no_digitos}") # Salida: ['H', 'o', 'l', 'a', ' ', ' ', 'M', 'u', 'n', 'd', 'o', ' ', '.']