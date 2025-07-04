import os

#Eliminar un archivo
if os.path.exists("output.txt"):
    os.remove("output.txt")
    print("Archivo eliminado")
else:
    print("El archivo no existe")