# Diccionarios de ejemplo
datos_base = {"id": 101, "nombre": "Carlos"}
datos_contacto = {"email": "carlos@ejemplo.com", "telefono": "123-456-7890"}
datos_adicionales = {"nombre": "Carlos A.", "ciudad": "Miami", "activo": True}

print(f"Datos base: {datos_base}")
print(f"Datos contacto: {datos_contacto}")
print(f"Datos adicionales: {datos_adicionales}")

# Unión de diccionarios con el operador ** (Python 3.5+)
# Si hay claves duplicadas ('nombre'), el valor del último diccionario prevalece
perfil_completo_unpack = {**datos_base, **datos_contacto, **datos_adicionales}
print(f"\nUnión con ** (nombre prevalece de adicionales): {perfil_completo_unpack}")
# Salida: {'id': 101, 'nombre': 'Carlos A.', 'email': 'carlos@ejemplo.com', 'telefono': '123-456-7890', 'ciudad': 'Miami', 'activo': True}

# Unión de diccionarios con el operador | (Python 3.9+)
# Similar al operador **, el último valor para una clave duplicada prevalece
perfil_completo_union = datos_base | datos_contacto | datos_adicionales
print(f"Unión con | (Python 3.9+, nombre prevalece): {perfil_completo_union}")

# Actualización in-place con el operador |= (Python 3.9+)
# Modifica el diccionario original de la izquierda
diccionario_a_actualizar = {"a": 1, "b": 2}
diccionario_fuente = {"b": 20, "c": 3}
print(f"\nDiccionario a actualizar (inicial): {diccionario_a_actualizar}")
diccionario_a_actualizar |= diccionario_fuente
print(f"Después de actualizar con |=: {diccionario_a_actualizar}")
# Salida: {'a': 1, 'b': 20, 'c': 3} ('b' se actualizó)

# Método .update() (funciona en todas las versiones de Python)
# También fusiona un diccionario en otro in-place.
diccionario_viejo = {"clave1": "valor1", "clave2": "valor2"}
nuevos_valores = {"clave2": "nuevo_valor2", "clave3": "valor3"}
print(f"\nDiccionario viejo (inicial): {diccionario_viejo}")
diccionario_viejo.update(nuevos_valores)
print(f"Después de .update(): {diccionario_viejo}")
# Salida: {'clave1': 'valor1', 'clave2': 'nuevo_valor2', 'clave3': 'valor3'}