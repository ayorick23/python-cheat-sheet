# Diccionario de ejemplo
configuracion = {
    "tema": "oscuro",
    "idioma": "es"
}

print(f"Configuración inicial: {configuracion}")

# Obtener un valor existente con setdefault (no lo modifica)
tema_actual = configuracion.setdefault("tema", "claro")
print(f"Tema actual (usando setdefault): {tema_actual}") # Salida: oscuro
print(f"Configuración después de obtener tema: {configuracion}") # Salida: {'tema': 'oscuro', 'idioma': 'es'}

# Obtener un valor no existente con setdefault (lo añade)
notificaciones = configuracion.setdefault("notificaciones", True)
print(f"Notificaciones (usando setdefault): {notificaciones}") # Salida: True
print(f"Configuración después de añadir notificaciones: {configuracion}") # Salida: {'tema': 'oscuro', 'idioma': 'es', 'notificaciones': True}

# Usando setdefault para inicializar una lista de forma segura
usuarios_por_rol = {}

usuarios_por_rol.setdefault("admin", []).append("Alice")
usuarios_por_rol.setdefault("usuario", []).append("Bob")
usuarios_por_rol.setdefault("admin", []).append("Charlie") # Se añade a la lista existente

print(f"\nUsuarios por rol: {usuarios_por_rol}")
# Salida: {'admin': ['Alice', 'Charlie'], 'usuario': ['Bob']}