import re

texto = "abc abbc abbbc aaaaaabbbbbc"
# Coincide con 'a' seguido de cero o más 'b', seguido de 'c'
patron_abc = re.compile(r'ab*c')

coincidencias = patron_abc.findall(texto)
print(f"Coincidencias con 'ab*c': {coincidencias}") # Salida: ['abc', 'abbc', 'abbbc', 'aaaaabbbbbc']