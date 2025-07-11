frase = "programacion en python es divertida y python es genial"

# Contar ocurrencias de una subcadena
conteo_python = frase.count("python")
print(f"La palabra 'python' aparece {conteo_python} veces.") # Salida: 2

# Contar ocurrencias de un carácter
conteo_e = frase.count("e")
print(f"El carácter 'e' aparece {conteo_e} veces.") # Salida: 5

# Contar en un rango específico
conteo_en_rango = frase.count("es", 10, 30) # Busca 'es' entre el índice 10 y 29
print(f"La subcadena 'es' aparece {conteo_en_rango} veces en el rango [10, 30].") # Salida: 1