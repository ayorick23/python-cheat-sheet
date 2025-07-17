import re

texto_multilinea = """
Línea 1
Línea 2
Línea 3
"""

# Sin re.DOTALL, el . no coincide con \n
patron_sin_dotall = re.compile(r'Línea.*Línea')
print(f"Sin DOTALL: {patron_sin_dotall.findall(texto_multilinea)}") # Salida: [] (no coincide a través de las líneas)

# Con re.DOTALL, el . sí coincide con \n
patron_con_dotall = re.compile(r'Línea.*Línea', re.DOTALL)
print(f"Con DOTALL: {patron_con_dotall.findall(texto_multilinea)}")
# Salida: ['Línea 1\nLínea 2\nLínea']