import os

# Componentes de una ruta
dir_base = "datos"
sub_dir = "informes"
nombre_archivo = "reporte.xlsx"

# Unir componentes usando os.path.join()
ruta_completa = os.path.join(dir_base, sub_dir, nombre_archivo)
print(f"Ruta generada: {ruta_completa}")

# En Windows, la salida sería: datos\informes\reporte.xlsx
# En Linux/macOS, la salida sería: datos/informes/reporte.xlsx

# Combinando con un directorio raíz (absoluto)
ruta_raiz = os.path.join(os.sep, 'home', 'usuario', 'documentos', 'mi_proyecto')
print(f"Ruta raíz (ejemplo): {ruta_raiz}")