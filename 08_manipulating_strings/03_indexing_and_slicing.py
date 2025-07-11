texto = "Python es divertido"

# Indexación
print(f"Primer carácter: {texto[0]}")     # Salida: P
print(f"Sexto carácter: {texto[5]}")      # Salida: n
print(f"Último carácter: {texto[-1]}")    # Salida: o
print(f"Penúltimo carácter: {texto[-2]}") # Salida: d

# Slicing
print(f"Desde el índice 7 al 9 (excl.): '{texto[7:11]}'") # Salida: es d
print(f"Los primeros 6 caracteres: '{texto[:6]}'")        # Salida: Python
print(f"Desde el índice 3 hasta el final: '{texto[3:]}'") # Salida: hon es divertido
print(f"Copia completa: '{texto[:]}'")                    # Salida: Python es divertido

# Slicing con paso
print(f"Caracteres alternos: '{texto[::2]}'")            # Salida: Pto sdvro
print(f"Cadena invertida: '{texto[::-1]}'")             # Salida: oditrevdi se nohtyP

# Inmutabilidad (intentar modificar causará un TypeError)
try:
    texto[0] = 'J'
except TypeError as e:
    print(f"\nError al intentar modificar un string: {e}") # Salida: TypeError: 'str' object does not support item assignment