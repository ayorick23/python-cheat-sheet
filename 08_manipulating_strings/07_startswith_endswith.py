nombre_archivo = "documento_final.pdf"
url = "https://www.ejemplo.com/pagina"

print(f"¿'{nombre_archivo}' empieza con 'doc'? {nombre_archivo.startswith('doc')}") # Salida: True
print(f"¿'{nombre_archivo}' empieza con 'Documento'? {nombre_archivo.startswith('Documento')}") # Salida: False (sensible a mayúsculas/minúsculas)
print(f"¿'{nombre_archivo}' termina con '.pdf'? {nombre_archivo.endswith('.pdf')}")   # Salida: True

print(f"¿'{url}' empieza con 'http://'? {url.startswith('http://')}") # Salida: False
print(f"¿'{url}' empieza con 'https://'? {url.startswith('https://')}") # Salida: True

# Con tupla de prefijos/sufijos
archivos = ["imagen.jpg", "reporte.docx", "script.py", "video.mp4"]
for archivo in archivos:
    if archivo.endswith((".jpg", ".png", ".gif")):
        print(f"'{archivo}' es un archivo de imagen.")
    elif archivo.startswith(("doc", "rep")):
        print(f"'{archivo}' es un documento o reporte.")