# Diccionario de ejemplo
informacion_libro = {
    "titulo": "Cien Años de Soledad",
    "autor": "Gabriel García Márquez",
    "año_publicacion": 1967,
    "genero": "Realismo Mágico"
}

print(f"Título: {informacion_libro['titulo']}")
print(f"Autor: {informacion_libro['autor']}")
print(f"Año de Publicación: {informacion_libro['año_publicacion']}")

# Modificar un valor existente
informacion_libro['genero'] = "Novela"
print(f"Género modificado: {informacion_libro['genero']}")

# Añadir un nuevo par clave-valor
informacion_libro['editorial'] = "Editorial Sudamericana"
print(f"Editorial añadida: {informacion_libro['editorial']}")

# Intentar acceder a una clave que no existe (causa un KeyError)
try:
    print(informacion_libro['ISBN'])
except KeyError as e:
    print(f"\nError: {e} - La clave no existe en el diccionario.")