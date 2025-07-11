# join()
palabras = ["Hola", "Mundo", "Python"]
guion = "-"
espacio = " "

cadena_guiones = guion.join(palabras)
print(f"Unido con guiones: '{cadena_guiones}'") # Salida: Hola-Mundo-Python

cadena_espacios = espacio.join(palabras)
print(f"Unido con espacios: '{cadena_espacios}'") # Salida: Hola Mundo Python

# join con un iterable de tuplas (cada elemento debe ser convertible a string)
partes_fecha = ("2025", "07", "08")
fecha_formato = "/".join(partes_fecha)
print(f"Fecha formateada: '{fecha_formato}'") # Salida: 2025/07/08

# split()
texto_largo = "Este es un ejemplo de texto para dividir."

lista_palabras = texto_largo.split() # Divide por espacios en blanco por defecto
print(f"Dividido por espacios: {lista_palabras}")
# Salida: ['Este', 'es', 'un', 'ejemplo', 'de', 'texto', 'para', 'dividir.']

csv_data = "manzana,banana,cereza,naranja"
lista_frutas = csv_data.split(",") # Divide por la coma
print(f"Dividido por comas: {lista_frutas}")
# Salida: ['manzana', 'banana', 'cereza', 'naranja']

# split() con maxsplit
cadena_ruta = "/home/user/documentos/archivo.txt"
partes_ruta = cadena_ruta.split("/", 2) # Divide solo en las primeras 2 ocurrencias
print(f"Dividido con maxsplit=2: {partes_ruta}")
# Salida: ['', 'home', 'user/documentos/archivo.txt']