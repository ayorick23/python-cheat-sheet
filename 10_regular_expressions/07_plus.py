import re

texto = "ab ac abbccc a bcc"
# Coincide con 'a' seguido de una o más 'b', seguido de 'c'
patron_abc_mas = re.compile(r'ab+c')

coincidencias = patron_abc_mas.findall(texto)
print(f"Coincidencias con 'ab+c': {coincidencias}") # Salida: ['abbc']

# Nota la diferencia con * : 'ac' no coincide con 'b+' porque necesita al menos una 'b'