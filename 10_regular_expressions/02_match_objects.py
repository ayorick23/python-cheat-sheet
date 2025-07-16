import re

texto = "Mi número de teléfono es 123-456-7890."
patron_telefono = re.compile(r'\d{3}-\d{3}-\d{4}') # \d coincide con cualquier dígito

# Usando re.search()
coincidencia = patron_telefono.search(texto)

if coincidencia:
    print("--- Coincidencia con re.search() ---")
    print(f"Coincidencia encontrada: {coincidencia.group(0)}") # El texto que coincide
    print(f"Inicio de la coincidencia: {coincidencia.start()}")
    print(f"Fin de la coincidencia: {coincidencia.end()}")
    print(f"Rango (inicio, fin): {coincidencia.span()}")
else:
    print("No se encontró ninguna coincidencia.")

# Usando re.match()
texto2 = "123-456-7890 es mi teléfono."
coincidencia_match = patron_telefono.match(texto2)

print("\n--- Coincidencia con re.match() ---")
if coincidencia_match:
    print(f"Coincidencia encontrada (con match): {coincidencia_match.group(0)}")
else:
    print("No se encontró coincidencia al principio de la cadena con match().")