import re

# Patrón para validar un número de teléfono con formato opcional
# Sin re.VERBOSE sería una sola línea difícil de leer: r'^\d{3}-?\d{3}-\d{4}$'
patron_telefono_verbose = re.compile(r"""
    ^                   # Inicio de la cadena
    (\d{3})             # Grupo 1: Los primeros tres dígitos
    [-\s]?              # Un guion o espacio opcional
    (\d{3})             # Grupo 2: Los siguientes tres dígitos
    [-\s]?              # Un guion o espacio opcional
    (\d{4})             # Grupo 3: Los últimos cuatro dígitos
    $                   # Fin de la cadena
""", re.VERBOSE)

telefonos = [
    "123-456-7890",
    "987 654 3210",
    "5551234567",
    "12345",
    "abc-def-ghi"
]

print("--- Validación de teléfonos con RegEx compleja ---")
for tel in telefonos:
    if patron_telefono_verbose.match(tel):
        print(f"'{tel}': Válido")
    else:
        print(f"'{tel}': Inválido")

# Otro ejemplo: Analizar una URL simple
patron_url_verbose = re.compile(r"""
    (https?|ftp)        # Grupo 1: Protocolo (http, https, ftp)
    ://                 # Coincidir con '://'
    ([\w\-\.]+)         # Grupo 2: Dominio (letras, números, guiones, puntos)
    (/[\w\-\._~:/?#\[\]@!$&'()*+,;=.]*)? # Grupo 3: Ruta opcional
""", re.VERBOSE)

url_ejemplo = "https://www.example.com/path/to/page.html?query=test#section"
match_url = patron_url_verbose.match(url_ejemplo)

if match_url:
    print("\n--- Análisis de URL ---")
    print(f"URL completa: {match_url.group(0)}")
    print(f"Protocolo: {match_url.group(1)}")
    print(f"Dominio: {match_url.group(2)}")
    print(f"Ruta: {match_url.group(3)}")