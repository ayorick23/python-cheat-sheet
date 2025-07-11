texto_original = "El perro es un animal doméstico. El perro es leal."

# Reemplazar todas las ocurrencias
texto_modificado = texto_original.replace("perro", "gato")
print(f"Texto modificado (todas las ocurrencias): '{texto_modificado}'")
# Salida: El gato es un animal doméstico. El gato es leal.

# Reemplazar solo la primera ocurrencia
texto_reemplazo_unico = texto_original.replace("perro", "conejo", 1)
print(f"Texto modificado (solo la primera): '{texto_reemplazo_unico}'")
# Salida: El conejo es un animal doméstico. El perro es leal.

# Reemplazar espacios por guiones
frase_con_espacios = "una frase con espacios"
frase_con_guiones = frase_con_espacios.replace(" ", "-")
print(f"Frase con guiones: '{frase_con_guiones}'") # Salida: una-frase-con-espacios