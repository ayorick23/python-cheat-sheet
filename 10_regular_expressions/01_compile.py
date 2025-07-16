import re

# Compilamos el patrón
patron_saludo = re.compile(r'hola')

# Usamos el patrón compilado para buscar en una cadena
texto = "hola mundo, ¿cómo estás? un hola por aquí."
coincidencias = patron_saludo.findall(texto)

print(f"Texto original: '{texto}'")
print(f"Patrón compilado: '{patron_saludo.pattern}'")
print(f"Coincidencias encontradas: {coincidencias}") # Salida: ['hola', 'hola']
