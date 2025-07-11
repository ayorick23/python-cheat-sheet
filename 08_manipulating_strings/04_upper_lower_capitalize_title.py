saludo = "hola mundo"
titulo_libro = "la gran aventura de python"

# upper()
print(f"'{saludo}' en mayúsculas: '{saludo.upper()}'") # Salida: HOLA MUNDO

# lower()
cadena_mixta = "PyTHoN PrOGrAmAcION"
print(f"'{cadena_mixta}' en minúsculas: '{cadena_mixta.lower()}'") # Salida: python programacion

# capitalize()
print(f"'{saludo}' capitalizado: '{saludo.capitalize()}'") # Salida: Hola mundo
print(f"'{cadena_mixta}' capitalizado: '{cadena_mixta.capitalize()}'") # Salida: Python programacion

# title()
print(f"'{titulo_libro}' en formato título: '{titulo_libro.title()}'") # Salida: La Gran Aventura De Python
print(f"'{saludo}' en formato título: '{saludo.title()}'") # Salida: Hola Mundo