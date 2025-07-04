# Valor absoluto de enteros
print(f"abs(-5): {abs(-5)}") # Salida: 5
print(f"abs(10): {abs(10)}") # Salida: 10

# Valor absoluto de flotantes
print(f"abs(-3.14): {abs(-3.14)}") # Salida: 3.14
print(f"abs(7.8): {abs(7.8)}")   # Salida: 7.8

# Valor absoluto de números complejos (magnitud)
# La magnitud de un número complejo a + bi es sqrt(a^2 + b^2)
numero_complejo = 3 + 4j
print(f"abs({numero_complejo}): {abs(numero_complejo)}") # Salida: 5.0 (sqrt(3^2 + 4^2) = sqrt(9 + 16) = sqrt(25) = 5)