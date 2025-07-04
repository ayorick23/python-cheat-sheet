# Redondear al entero más cercano (sin ndigits)
print(f"round(3.14159): {round(3.14159)}")   # Salida: 3
print(f"round(3.7): {round(3.7)}")         # Salida: 4
print(f"round(2.5): {round(2.5)}")         # Salida: 2 (redondeo a la mitad par)
print(f"round(3.5): {round(3.5)}")         # Salida: 4 (redondeo a la mitad par)
print(f"round(-2.5): {round(-2.5)}")       # Salida: -2 (redondeo a la mitad par)
print(f"round(-3.5): {round(-3.5)}")       # Salida: -4 (redondeo a la mitad par)

# Redondear a un número específico de decimales
print(f"round(3.14159, 2): {round(3.14159, 2)}") # Salida: 3.14
print(f"round(123.456, 1): {round(123.456, 1)}") # Salida: 123.5
print(f"round(7.896, 2): {round(7.896, 2)}")   # Salida: 7.9
print(f"round(7.895, 2): {round(7.895, 2)}")   # Salida: 7.9 (redondeo a la mitad par)

# Redondear a un número de decimales negativo (redondea a la decena, centena, etc.)
print(f"round(12345.678, -1): {round(12345.678, -1)}") # Salida: 12350.0 (redondea a la decena más cercana)
print(f"round(12345.678, -2): {round(12345.678, -2)}") # Salida: 12300.0 (redondea a la centena más cercana)