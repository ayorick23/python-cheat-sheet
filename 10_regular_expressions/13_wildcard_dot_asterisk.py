import re

texto_html = "<span>Contenido 1</span><p>Otro contenido</p><span>Contenido 2</span>"

# Coincidencia codiciosa: desde el primer <span> hasta el último </span>
patron_codicioso = re.compile(r'<span>.*</span>')
print(f"Coincidencia codiciosa: {patron_codicioso.findall(texto_html)}")
# Salida: ['<span>Contenido 1</span><p>Otro contenido</p><span>Contenido 2</span>']

# Coincidencia no codiciosa: encuentra cada par <span></span> por separado
patron_no_codicioso = re.compile(r'<span>.*?</span>')
print(f"Coincidencia no codiciosa: {patron_no_codicioso.findall(texto_html)}")
# Salida: ['<span>Contenido 1</span>', '<span>Contenido 2</span>']

# Ejemplo con 'cualquier caracter'
frase = "El gato saltó sobre el muro."
patron_salto = re.compile(r'gato.saltó') # El punto coincide con el espacio
print(f"Coincidencia con '.': {patron_salto.findall(frase)}") # Salida: ['gato saltó']