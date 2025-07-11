texto_con_espacios = "   Hola Mundo   "
texto_con_simbolos = "---###Mensaje Importante###---"

print(f"Original: '{texto_con_espacios}'")
print(f"strip(): '{texto_con_espacios.strip()}'")     # Salida: 'Hola Mundo'
print(f"lstrip(): '{texto_con_espacios.lstrip()}'")   # Salida: 'Hola Mundo   '
print(f"rstrip(): '{texto_con_espacios.rstrip()}'")   # Salida: '   Hola Mundo'

print(f"\nOriginal: '{texto_con_simbolos}'")
# strip() con caracteres específicos
print(f"strip('-#'): '{texto_con_simbolos.strip('-#')}'") # Salida: 'Mensaje Importante'

# lstrip() con caracteres específicos
print(f"lstrip('-'): '{texto_con_simbolos.lstrip('-')}'") # Salida: '###Mensaje Importante###---'

# rstrip() con caracteres específicos
print(f"rstrip('#-'): '{texto_con_simbolos.rstrip('#-')}'") # Salida: '---###Mensaje Importante'