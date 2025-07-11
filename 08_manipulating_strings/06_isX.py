cadena1 = "Python"
cadena2 = "12345"
cadena3 = "Py4th0n"
cadena4 = "   "
cadena5 = "Hola Mundo"
cadena6 = "2.5" # Cuidado: float no es isdigit/isnumeric/isdecimal

print(f"'{cadena1}'.isalpha(): {cadena1.isalpha()}") # Salida: True
print(f"'{cadena2}'.isdigit(): {cadena2.isdigit()}") # Salida: True
print(f"'{cadena3}'.isalnum(): {cadena3.isalnum()}") # Salida: True
print(f"'{cadena4}'.isspace(): {cadena4.isspace()}") # Salida: True
print(f"'{cadena5}'.istitle(): {cadena5.istitle()}") # Salida: True
print(f"'{cadena6}'.isdigit(): {cadena6.isdigit()}") # Salida: False (contiene '.')
print(f"'{cadena6}'.isnumeric(): {cadena6.isnumeric()}") # Salida: False

print(f"\nCadena vacía: ''.isalpha(): {''.isalpha()}") # Salida: False (siempre False para cadenas vacías)