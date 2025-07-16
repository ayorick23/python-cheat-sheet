import re

texto = "<h1>Título 1</h1><p>Párrafo</p><h1>Título 2</h1>"

# Patrón codicioso (greedy): * intenta coincidir con todo lo posible
# Coincidirá desde el primer <h1> hasta el último </h1>
patron_codicioso = re.compile(r'<.*>')
print(f"Coincidencia codiciosa: {patron_codicioso.findall(texto)}")
# Salida: ['<h1>Título 1</h1><p>Párrafo</p><h1>Título 2</h1>']

# Patrón no codicioso (non-greedy): *? intenta coincidir con lo mínimo
# Coincidirá con cada par de etiquetas por separado
patron_no_codicioso = re.compile(r'<.*?>')
print(f"Coincidencia no codiciosa: {patron_no_codicioso.findall(texto)}")
# Salida: ['<h1>', '</h1>', '<p>', '</p>', '<h1>', '</h1>']

# Ejemplo con un caso más específico
texto2 = "abc123def456ghi"
patron_greedy_digitos = re.compile(r'\d+') # Uno o más dígitos (codicioso)
print(f"Dígitos codiciosos: {patron_greedy_digitos.findall(texto2)}") # Salida: ['123', '456']

patron_non_greedy_digitos = re.compile(r'\d+?') # Uno o más dígitos (no codicioso)
print(f"Dígitos no codiciosos: {patron_non_greedy_digitos.findall(texto2)}") # Salida: ['1', '2', '3', '4', '5', '6']