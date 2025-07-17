from pathlib import Path

# Creación de rutas usando el operador /
ruta_documento = Path("documentos") / "notas" / "reunion.txt"
print(f"Ruta con pathlib: {ruta_documento}")

# Acceso a componentes de la ruta
print(f"Nombre del archivo: {ruta_documento.name}")
print(f"Extensión: {ruta_documento.suffix}")
print(f"Directorio padre: {ruta_documento.parent}")
print(f"Partes de la ruta: {ruta_documento.parts}")

# Rutas absolutas
ruta_absoluta = Path("C:/Users/Usuario/Desktop/proyecto/main.py") # Windows-like
# ruta_absoluta = Path("/home/usuario/proyecto/main.py")          # Unix-like
print(f"¿Es absoluta? {ruta_absoluta.is_absolute()}")