# Diccionario de ejemplo
perfil_usuario = {
    "nombre": "Elena",
    "email": "elena@ejemplo.com",
    "activo": True
}

# Usando get() con una clave existente
print(f"Email del usuario: {perfil_usuario.get('email')}") # Salida: elena@ejemplo.com

# Usando get() con una clave que no existe (devuelve None por defecto)
print(f"Teléfono del usuario: {perfil_usuario.get('telefono')}") # Salida: None

# Usando get() con una clave que no existe y un valor por defecto
print(f"Dirección del usuario: {perfil_usuario.get('direccion', 'No especificada')}")
# Salida: No especificada

# Un ejemplo de cómo evitar KeyError con get()
def obtener_dato_seguro(dicc, clave):
    dato = dicc.get(clave, "Dato no disponible")
    print(f"Para la clave '{clave}', el dato es: {dato}")

obtener_dato_seguro(perfil_usuario, 'nombre')
obtener_dato_seguro(perfil_usuario, 'pais')