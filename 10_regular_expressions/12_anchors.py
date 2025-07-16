import re

texto1 = "Inicio de la frase."
texto2 = "Frase que termina."
texto3 = "Solo esta frase"

# Coincidir si la cadena empieza con 'Inicio'
print(f"'{texto1}' empieza con 'Inicio': {bool(re.search(r'^Inicio', texto1))}") # Salida: True
print(f"'{texto2}' empieza con 'Inicio': {bool(re.search(r'^Inicio', texto2))}") # Salida: False

# Coincidir si la cadena termina con 'termina.'
print(f"'{texto1}' termina con 'frase.': {bool(re.search(r'frase.$', texto1))}") # Salida: True
print(f"'{texto2}' termina con 'frase.': {bool(re.search(r'termina.$', texto2))}") # Salida: True

# Coincidir si la cadena es EXACTAMENTE 'Solo esta frase'
print(f"'{texto3}' es 'Solo esta frase': {bool(re.search(r'^Solo esta frase$', texto3))}") # Salida: True
print(f"'{texto1}' es 'Solo esta frase': {bool(re.search(r'^Solo esta frase$', texto1))}") # Salida: False