import re

texto = "Python es divertido. python es potente. PYTHON es genial."

# Sin IGNORECASE (distingue mayúsculas/minúsculas)
patron_sensible = re.compile(r'python')
print(f"Sensible a mayúsculas: {patron_sensible.findall(texto)}") # Salida: ['python']

# Con IGNORECASE (no distingue mayúsculas/minúsculas)
patron_insensible = re.compile(r'python', re.IGNORECASE)
print(f"Insensible a mayúsculas: {patron_insensible.findall(texto)}") # Salida: ['Python', 'python', 'PYTHON']